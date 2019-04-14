#!/usr/bin/env python
# coding: utf-8

from sqlalchemy import text
from app.database import db
from datetime import datetime

class DataTable(db.Model):
    __tablename__ = "Data"
    
    fileid = db.Column(db.Integer, db.ForeignKey('Files.fileid'))
    ticker = db.Column(db.String(80), nullable=False)
    per = db.Column(db.Integer())
    dateAndTime = db.Column(db.DateTime)
    openT = db.Column(db.Float)
    highT = db.Column(db.Float)
    lowT = db.Column(db.Float)
    closeT = db.Column(db.Float)
    vol = db.Column(db.Integer)
    
    created = db.Column(db.DateTime, default=datetime.now, server_default=text('now()'))
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, server_default=text('now()'))

    def __repr__(self):
        return f'{type(self).__name__} <{self.fileid}>=<{self.ticker}>'