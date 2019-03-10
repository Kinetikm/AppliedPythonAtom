#!/usr/bin/env python
# coding: utf-8

from .ReadData import readData
from .ReadData import FileFormat
from ..handlers.ConverterToJSON import convertToJSON
from ..handlers.DataChecker import checkData


def getData(filename):
    try:
        fileFormat, data = readData(filename)
        if fileFormat != FileFormat.JSON:
            data = convertToJSON(data)
        checkData(data)
        return data
    except FileNotFoundError:
        print("Файл не валиден")
    except UnicodeError:
        print("Формат не валиден")
    except SyntaxError:
        print("Формат не валиден")
    return None
