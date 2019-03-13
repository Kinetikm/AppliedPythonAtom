from chardet.universaldetector import UniversalDetector


def hello():
    print('hello')


class FileProperties:
    def __init__(self, filename, file_state=None, encoding=None):
        self.filename = filename
        self.file_state = file_state
        self.encoding = encoding

    def open(self):
        detector = UniversalDetector()
        try:
            with open(self.filename, 'rb') as file:
                self.file_state = "exist"
                for line in file:
                    detector.feed(line)
                    if detector.done:
                        break
                detector.close()
                result = detector.result['encoding']
                if result == "utf-8":
                    self.encoding = result
                elif result == "utf-16":
                    self.encoding = result
                elif result == "windows-1251":
                    self.encoding = result
                else:
                    result = "other"
                    self.encoding = result
        except FileNotFoundError:
            self.file_state = None
            self.encoding = None
            self.file_state = None