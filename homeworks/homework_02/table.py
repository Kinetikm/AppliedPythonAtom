import sys

# Ваши импорты
# Импорты совершаются внутри пакетов
from homeworks.homework_02.input.get_data import getData
from homeworks.homework_02.output.output_creator import createTable

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код
    data = getData(filename)
    if data is not None:
        createTable(data)
