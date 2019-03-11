#!/usr/bin/env python
# coding: utf-8

from com.input.read_data import readData
from com.input.read_data import FileFormat
from com.handlers.converter_to_json import convertToJSON
from com.handlers.data_checker import checkData


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
