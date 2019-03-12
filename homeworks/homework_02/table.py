import sys
import validity
import reading
import printing

if __name__ == '__main__':
    filename = sys.argv[1]

    enc = validity.get_encoding_correct_file(filename)
    if enc == 0:
        print('Файл не валиден')
    elif enc == 1:
        print('Формат не валиден')
    else:
        data = reading.read_file(filename, enc)
        print(data)
        printing.print_it(data)
