#!/usr/bin/env python
# coding: utf-8

import json
import csv
from enum import Enum
from com.input.encoding_identifier import encodingIdentifier


class FileFormat(Enum):
    JSON = 1
    TSV = 2


def readData(filename):
    enc = encodingIdentifier(filename)
    # try json format
    with open(file=filename, mode="r", encoding=enc) as f:
        try:
            data = json.load(f)
            if len(data) == 0:
                raise SyntaxError
            return FileFormat.JSON, data
        except json.decoder.JSONDecodeError:
            pass
    # try tsv format
    with open(file=filename, mode="r", encoding=enc) as f:
        try:
            reader = csv.reader(f, delimiter='\t')
            data = []
            for row in reader:
                data.append(row)
            if len(data) == 0:
                raise SyntaxError
            return FileFormat.TSV, data
        except csv.Error:
            pass
    raise SyntaxError
