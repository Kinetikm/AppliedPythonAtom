from homeworks.homework_03.hw3_hashmap.py import HashMap


class HashSet(HashMap):

    def __init__(self):
        super().__init__()

    def get(self, key, default_value=None):
        return super().__contains__(key)

    def put(self, key, value=None):
        return super().put(key, value)

    def __len__(self):
        return super().__len__()

    def values(self):

    return super().keys()

    def intersect(self, another_hashset):
        raise NotImplementedError
        new_HashSet = HashSet()
        united_values = self.values() + another_hashset.values()
        for item in united_values:
            if item in another_hashset.values() and item in self.values():
                new_HashSet.put(item)
        return new_HashSet
