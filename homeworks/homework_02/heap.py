class Heap(object):

    def __init__(self, array):
        self.data = array[:]
        self.build_heap()

    def move_down(self, i):
        while True:
            first = 2 * i + 1
            largest = i
            if (first < len(self.data)) \
                    and comparator_d(self.data[first], self.data[largest]):
                largest = first
            if (first+1 < len(self.data)) \
                    and comparator_d(self.data[first+1], self.data[largest]):
                largest = first+1
            if largest == i:
                break
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest

    def add(self, elem_with_priority):
        self.data.append(elem_with_priority)
        self.build_heap()

    def build_heap(self):
        length = len(self.data) // 2
        for i in range(length, -1, -1):
            self.move_down(i)


class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)

    def extract_maximum(self):
        result = self.data.pop(0)
        self.build_heap()
        return result


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
