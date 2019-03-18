import sys
import checking as ch
import converting as con
import printing as pr

if __name__ == '__main__':
    filename = sys.argv[1]
    try:
        open(filename, 'r')
    except FileNotFoundError:
        print('Файл не валиден')
        raise SystemExit
    try:
        code = ch.enc(filename)
        form = ch.format(filename, code)
        conv_inf = con.read_file(filename, code, form)
        pr.print_table(conv_inf)
    except SystemExit:
        print("Формат не валиден")
