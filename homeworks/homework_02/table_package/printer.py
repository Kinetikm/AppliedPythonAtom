class Print_JSON():

    def __init__(self, json_file):

        self.json_file = json_file

        self.line_counts = len(json_file)
        self.column_counts = len(json_file[0])

        self.column_size = [0] * self.column_counts
        self.key_list = []

        # initalize size of tables by keys
        i = 0
        for k in json_file[0]:
            tmp = k
            if isinstance(k, int):
                tmp = str(k)
            self.column_size[i] = len(tmp)
            self.key_list.append(tmp)
            i += 1

        for dict in json_file:  # every line in json
            i = 0
            for _, v in dict.items():
                if isinstance(v, int):
                    v = str(v)
                if len(v) > self.column_size[i]:
                    self.column_size[i] = len(v)
                i += 1

    def print_line(self):
        # count sum of headers lens
        sum_len_names = 0
        for i in self.column_size:
            sum_len_names += i

        # table horizontal len
        len_of_table = 1 + (2 + 2 + 1) * self.column_counts + sum_len_names

        # first line
        for i in range(len_of_table):
            print('-', end="")
        print()

    def print_head(self):

        # tipa func kotoraya otrisovivaet header s nazvaniyamni

        print("|", end="")
        i = 0
        for k in self.key_list:
            len_k = len(k)
            len_c = self.column_size[i]

            # fg = False
            # if len_c - len_k % 2 != 0:
            #     fg = True

            r_space = int((len_c - len_k) / 2)
            l_space = len_c - len_k - r_space

            for _ in range(l_space + 2):
                print(" ", end="")

            print(k, end="")

            for _ in range(r_space + 2):
                print(" ", end="")

            print("|", end="")
            i += 1

        print()

    def print_body(self):

        for dict in self.json_file:  # every line in json
            i = 0
            print("|", end='')
            for _, v in dict.items():
                tmp = str(v)
                len_v = len(tmp)
                len_c = self.column_size[i]

                r_space = 2
                l_space = len_c - len_v

                for _ in range(l_space + 2):
                    print(" ", end="")

                print(tmp, end="")

                for _ in range(r_space):
                    print(" ", end="")

                print("|", end="")
                i += 1

            print()
