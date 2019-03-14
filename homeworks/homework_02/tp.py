class TablePrint:
    input_date = {}
    caption = []
    sizes = []

    def __init__(self, d: list):
        if d:
            self.input_date = d
            if isinstance(d[0], dict):
                self.caption = list(d[0].keys())
            elif isinstance(d[0], list):
                self.caption = d[0]
                self.input_date.pop(0)

    def sizing(self):
        self.sizes = [len(x) for x in self.caption]
        for line in self.input_date:
            i = 0
            for cap in self.caption:
                if isinstance(line, dict):
                    ls = len(str(line[cap]))
                else:
                    ls = len(line[i])
                if ls > self.sizes[i]:
                    self.sizes[i] = ls
                i = i + 1

    def header(self):
        width = sum(self.sizes)+len(self.sizes)*5 + 1
        print(self.hline(width))
        i = 0
        tmp = "|"
        for cap in self.caption:
            tmp = tmp + "  " + cap.center(self.sizes[i]) + "  |"
            i = i + 1
        print(tmp)

    def body(self):
        width = sum(self.sizes) + len(self.sizes) * 5 + 1
        for line in self.input_date:
            i = 0
            tmp = "|"
            for cap in self.caption:
                if isinstance(line, dict):
                    tmp = tmp + "  " + self.justify(line[cap],
                                                    self.sizes[i]) + "  |"
                else:
                    tmp = tmp + "  " + self.justify(line[i],
                                                    self.sizes[i]) + "  |"
                i = i + 1
            if tmp:
                print(tmp)
        print(self.hline(width))

    def hline(self, length: int):
        res = "-"
        return res.center(length, res)

    def justify(self, val: object, width: int):
        if str(val).isnumeric():
            res = str(val).rjust(width)
        else:
            res = str(val).ljust(width)
        return res
