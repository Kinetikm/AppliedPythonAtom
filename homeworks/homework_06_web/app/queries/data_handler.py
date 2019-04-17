#!/usr/bin/env python
# coding: utf-8

from flask import Blueprint
from flask import request, abort, jsonify
from sqlalchemy import func
from app.database import db
from app.auxiliary.transaction import transaction
from app.db_entities.files_view import Files
from app.db_entities.data_view import Data
from app.auxiliary.parser import parseAndUploadData

data_handler = Blueprint('data_handler', __name__, url_prefix="/data")


# Загрузка файла
@data_handler.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files or not request.files['file'].filename:
        abort(400)

    #Добавление в бд
    file = Files(filename=request.files['file'].filename)

    with transaction():
        Files.query.add(file)
        parseAndUploadData(file.fileid, request.files['file'])

    return file.fileid, 200


# Изменение файла
@data_handler.route('/<fileid>', methods=['PUT'])
def change_file(fileid):
    if not Files.query.filtered_by(fileid=fileid).all():
        abort(404)

    if 'file' not in request.files or not request.files['file'].filename:
        abort(400)

    # Изменение в бд
    with transaction():
        Data.query.filtered_by(fileid=fileid).delete()
        Files.query.filtered_by(fileid=fileid).update({'filename': request.files['file'].filename})
        parseAndUploadData(fileid, request.files['file'])

    return '', 204


# Получение информации о загруженном файле пользователя
@data_handler.route('/<fileid>', methods=['GET'])
def file_info(fileid):
    if not Files.query.filtered_by(fileid=fileid).all():
        abort(404)

    # Соединение таблиц и получение информации
    fileinf = db.session.query(Files, func.count(Data.fileid).label('count_rows'))\
        .join(Files.data)\
        .group_by(Files.fileid)\
        .having(Files.fileid==fileid)\
        .first()

    return jsonify(
        fileid=fileid,
        filename=fileinf.filename,
        first_download=fileinf.first_download,
        last_download=fileinf.last_download,
        data_count=fileinf.count_rows
    ), 200


# Удаление файла
@data_handler.route('/<fileid>', methods=['DELETE'])
def delete_file(fileid):
    if not Files.query.filtered_by(fileid=fileid).all():
        abort(404)

    # Удаление из бд
    with transaction():
        Data.query.filtered_by(fileid=fileid).delete()
        Files.query.filtered_by(fileid=fileid).delete()

    return '', 204
