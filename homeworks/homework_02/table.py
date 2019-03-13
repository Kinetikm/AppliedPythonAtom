import sys
# Ваши импорты
import property
import parser
import data_convert

if __name__ == '__main__':
    # блок проверки наличия файла и соответствие кодировки
    # (utf8, utf16, cp1251)
    # filename = "files/posts-utf8.json"
    # filename = "files/posts-cp1251.tsv"

    filename = sys.argv[1]
    file = property.FileProperties(filename)
    file.open()

    data = parser.parse_json_tsv(filename, file.encoding)
    data_format = data_convert.convert(data)

    if data_format is not None:
        for i in range(len(data_format)):
            print(data_format[i])
    else:
        print('формат не валиден')
