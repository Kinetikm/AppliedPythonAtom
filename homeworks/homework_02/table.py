import sys

# Ваши импорты

from encodingtype import encoding_of_file as Enc
from filetype import format_of_file as Form
from printing import printing_the_file as FilePrint

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код

if os.path.isfile(filename) is not True:
    print('Файл не валиден')
elif Enc(filename) == 'another' or Form(filename, Enc(filename)) == 'another':
    print('Формат не валиден')
else:
    form = Form(filename)
    enc = Enc(filename)
    FilePrint(filename, form, enc)
