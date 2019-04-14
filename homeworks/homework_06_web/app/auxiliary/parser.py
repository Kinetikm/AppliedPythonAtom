#!/usr/bin/env python
# coding: utf-8

from app.auxiliary.transaction import transactional
from app.database import db

@transactional
def parseAndUploadData(fileid: int, file):
    pass