from flask import Flask, request, abort, redirect
import time
from help_funcs import parsing, make_response
from logger import log


app = Flask(__name__)
database = {}


@app.route('/post', methods=["POST"])
def post():
    start = time.time()
    rawdata = request.data.decode('utf-8')
    if rawdata != '':
        data = rawdata.replace(' ', '+')
        if database.get(rawdata) is None:
            database[rawdata] = parsing(
                'https://stackoverflow.com/search?q=' + data)
            stop = time.time()
            log('POST', 201, stop - start)
            return "", 201
        else:
            stop = time.time()
            log('POST', 200, stop - start)
            return '', 200
    stop = time.time()
    log('POST', 400, stop - start)
    return abort(400)


@app.route('/get', methods=["GET"])
def get():
    start = time.time()
    if request.args['title'] is None:
        stop = time.time()
        log('GET', 400, stop - start)
        return abort(400)
    title = request.args['title']
    if database.get(title) is None:
        stop = time.time()
        log('GET', 404, stop - start)
        return abort(404)
    answers = make_response(database.get(title))
    stop = time.time()
    log('GET', 200, stop - start)
    return answers, 200


@app.route('/put', methods=["PUT"])
def put():
    start = time.time()
    rawdata = request.data.decode('utf-8')
    if request.args['title'] is None:
        stop = time.time()
        log('PUT', 400, stop - start)
        return abort(400)
    title = request.args['title']
    if rawdata == '':
        stop = time.time()
        log('PUT', 400, stop - start)
        return abort(400)
    if database.get(title) is None:
        database[title] = rawdata
        stop = time.time()
        log('PUT', 201, stop - start)
        return 'OK', 201
    database[title] = rawdata
    stop = time.time()
    log('PUT', 200, stop - start)
    return 'OK', 200


@app.route('/delete', methods=["DELETE"])
def delete():
    start = time.time()
    if request.args['title'] is None:
        return abort(400)
    title = request.args['title']
    if database.get(title) is None:
        stop = time.time()
        log('DELETE', 204, stop - start)
        return '', 204
    database.pop(title)
    stop = time.time()
    log('DELETE', 200, stop - start)
    return '', 200


if __name__ == "__main__":
    app.run()
