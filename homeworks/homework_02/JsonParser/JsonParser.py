import json
from MetaParser import TableRecord as tr

class JsonParser(tr.MetaParser):


    def get_table(self):
        if not self.valid:
            return None
        headers=None
        for rec in self.jsonObj:
            if headers is None:
                headers=[]
                for key, value in rec.items():
                    headers.append(key)
                table = tr.Table(headers)
            params=[]
            for header in headers:
                params.append(str(rec[header]))
            table.add_record(tr.TableRecord(params))
        return table

    def open(self, filename):
        try:
            with open(filename,"r", encoding="utf8") as f:
                self.jsonObj=json.loads(f.read())
        except UnicodeDecodeError:
            self.valid=False
        except json.decoder.JSONDecodeError:
            self.valid=False
            return

        if not self.valid:
            try:
                with open(filename,"r", encoding="cp1251") as f:
                    self.jsonObj=json.loads(f.read())
                self.valid=True
            except json.decoder.JSONDecodeError:
                self.valid=False

    def __init__(self):
        super().__init__()
        self.jsonObj=None


