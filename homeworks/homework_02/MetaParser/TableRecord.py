class TableRecord:
    def __init__(self, fields):
        self.fields = fields


class Table:
    def __init__(self, headers):
        self.tables = []
        self.valid = True
        self.field_count = len(headers)
        self.headers = headers

    def add_record(self, record):
        if self.field_count == len(record.fields):
            self.tables.append(record)
        else:
            self.valid = False

    def print(self):
        max_length = 0
        max_fields = [len(x) for x in self.headers]
        for rec in self.tables:
            for i in range(self.field_count):
                if (max_fields[i] < len(rec.fields[i])):
                    max_fields[i] = len(rec.fields[i])

        max_length = self.field_count*5 + 1 + sum(max_fields)
        print('-' * max_length)
        fmt = '|' + '|'.join('  {:^%d}  ' % l for l in max_fields) + '|'
        print(fmt.format(*self.headers))
        fmt = '|' + '|'.join('  {:<%d}  ' % l for l in max_fields[:-1]) + '|'
        fmt += '  {:>%d}  |' % max_fields[-1]
        for rec in self.tables:
            print(fmt.format(*rec.fields),end='\n')
        print('-' * max_length)


class MetaParser:
    def __init__(self):
        self.valid = True

    def open(self, filename):
        raise NotImplementedError

    def get_table(self):
        raise NotImplementedError
