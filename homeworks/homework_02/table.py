import sys


# Ваши импорты
from .tp import TablePrint
from .wwf import WorkWithFile

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код
    a = WorkWithFile(filename)
    b = TablePrint(a.parsing())
    b.sizing()
    b.header()
    b.body()
