#!/usr/bin/env python
# coding: utf-8

DB_CONFIG = {
    'username': 'root',
    'password': 'trading_pass',
    'host': '127.0.0.1',
    'dbname': 'trading_db',
}


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_CONFIG['username']}:{DB_CONFIG['password']}" \
                              f"@{DB_CONFIG['host']}/{DB_CONFIG['dbname']}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

currentConfig = DevelopmentConfig
