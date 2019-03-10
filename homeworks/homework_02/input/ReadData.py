#!/usr/bin/env python
# coding: utf-8

import json
import csv
from enum import Enum
from homeworks.homework_02.input.EncodingIdentifier import encodingIdentifier


class FileFormat(Enum):
    JSON = 1
    TSV = 2


def readData(filename):
    enc = encodingIdentifier(filename)
    # try json format
    with open(file=filename, mode="r", encoding=enc) as f:
        try:
            data = json.load(f)
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
            return FileFormat.TSV, data
        except csv.Error:
            pass
    raise SyntaxError
