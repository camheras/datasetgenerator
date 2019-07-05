import random


class Parameter:
    _value = None

    def __init__(self, type, range=None, book=None):
        if type == "INT":
            start = range[0]
            end = range[1]
            _range = start - end
            print(f"start : {start} \n"
                  f"end : {end}")
            self._value = random.random() * _range + start
        elif type == "STRING":
            print(book)
            self._value = book[int(random.random() * len(book))]
