# 03. Countdown Iterator

class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.idx = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < 0:
            raise StopIteration
        index = self.idx
        self.idx -= 1
        return index


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
