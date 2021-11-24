# 04. Sequence Repeat

class sequence_repeat:
    def __init__(self, sequence: str, count: int):
        self.sequence = sequence
        self.count = count
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.count:
            index = self.current_index
            self.current_index += 1
            return self.sequence[index % len(self.sequence)]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')