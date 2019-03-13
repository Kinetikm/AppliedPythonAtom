import sys
# Ваши импорты
import file_proper
import file_parser
import data_format

if __name__ == '__main__':
    # блок проверки наличия файла и соответствие кодировки
    # (utf8, utf16, cp1251)
    # filename = "files/posts-utf8.json"
    # filename = "files/posts-cp1251.tsv"

    filename = sys.argv[1]
    file = file_proper.file_properties(filename)
    file.open()

    data = file_parser.parse_json_tsv(filename, file.encoding)
    d_form = data_format.convert(data)

    if d_form is not None:
        for i in range(len(d_form)):
            print(d_form[i])
    else:
        print('формат не валиден')
