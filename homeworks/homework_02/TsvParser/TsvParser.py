from MetaParser import TableRecord as tr

class TsvParser(tr.MetaParser):
    def get_table(self):

        if not self.valid:
            return None
        else:
            tb = tr.Table(self.lineParts[0])
            for i in range(1, len(self.lineParts)):
                tb.add_record(tr.TableRecord(self.lineParts[i]))
            return tb


    def __init__(self):
        super().__init__()
        self.lineParts = []

    def parse_file(self, f):
        for line in f.read().splitlines():
            parts = line.split('\t')
            if len(parts)!=4:
                self.valid=False
            else:
                self.lineParts.append(parts)

    def open(self, filename):
        try:
            with open(filename,"r", encoding="utf8") as f:
                self.parse_file(f)
        except UnicodeDecodeError:
            self.valid=False

        if not self.valid:
            self.valid=True
            with open(filename,"r", encoding="cp1251") as f:
                self.parse_file(f)


