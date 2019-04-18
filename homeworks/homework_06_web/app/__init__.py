#!/usr/bin/env python
# coding: utf-8

from flask import Flask
import logging
from .database import db
import appconfig


def create_app(Log=None):

    do_logging = False
    if isinstance(Log, logging.Logger):
        do_logging = True

    def writeLog(mes):
        if do_logging:
            Log.info(mes)

    writeLog('Creating app...')
    app = Flask(__name__)
    writeLog('App created')
    writeLog('Configurating config...')
    app.config.from_object(appconfig.currentConfig)
    writeLog('Config configured')

    writeLog('Initialize database...')
    db.init_app(app)
    writeLog('Database initialized')
    with app.test_request_context():
        writeLog('Creating tables...')
        db.create_all()
        writeLog('Tables created...')

    import app.queries.data_handler as data_handler

    app.register_blueprint(data_handler.data_handler)

    return app


def create_logger():
    return logging.getLogger(appconfig.currentConfig.LOGGER_NAME)
