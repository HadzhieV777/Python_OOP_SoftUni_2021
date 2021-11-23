# 02. Dictionary Iterator

# first way
class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = list(dictionary.items())
        self.current_index = 0

    def __iter__(self):
        # self.index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.dictionary):
            raise StopIteration
        idx = self.current_index
        self.current_index += 1
        return self.dictionary[idx]


# second way

class dictionary_iter:
    def __init__(self, dictionary: dict) -> None:
        self.dictionary = dictionary
        self.items = iter(self.dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.items)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

for x in result:
    print(x)
