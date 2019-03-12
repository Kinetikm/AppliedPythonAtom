import json
import csv
import reader


def depars(file):
    try:
        input_sting = reader.read(file)
        try:
            return (json.loads(input_sting), "JSON")
        except ValueError:
            input_data = input_sting.split("\n")
            deparsedData = []
            for string in input_data:
                deparsedData.append(string.split("\t"))
            return (deparsedData, "TSV")
    except ValueError:
        raise ValueError
