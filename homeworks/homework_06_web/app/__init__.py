#!/usr/bin/env python
# coding: utf-8

from flask import Flask
from .database import db
import appconfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(appconfig.currentConfig)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    import app.queries.data_handler as data_handler

    app.register_blueprint(data_handler.data_handler)

    return app
