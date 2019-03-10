#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_02.input.ReadData import readData
from homeworks.homework_02.input.ReadData import FileFormat
from homeworks.homework_02.handlers.ConverterToJSON import convertToJSON
from homeworks.homework_02.handlers.DataChecker import checkData


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
