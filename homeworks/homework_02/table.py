import sys

# Ваши импорты
# Импорты совершаются внутри пакетов
from homeworks.homework_02.com.input.GetData import getData
from homeworks.homework_02.com.output.OutputCreator import createTable

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код
    data = getData(filename)
    if data is not None:
        createTable(data)
