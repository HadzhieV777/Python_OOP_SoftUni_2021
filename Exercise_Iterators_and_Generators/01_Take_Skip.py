# 01. Take Skip

class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.count:
            raise StopIteration
        index = self.start * self.step
        self.start += 1
        return index

numbers = take_skip(10, 5)
for number in numbers:
    print(number)