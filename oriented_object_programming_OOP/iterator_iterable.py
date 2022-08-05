class MyList:
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def add(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __check_index(self, index):
        if not self._data.get(index):
            raise IndexError(f'Index {index} does not exist.')

    def __setitem__(self, index, value):
        self.__check_index(index)
        self._data[index] = value

    def __getitem__(self, index):
        self.__check_index(index)
        return self._data[index]

    def __delitem__(self, index):
        self.__check_index(index)
        self._data[index] = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        value = self._data.get(self._next_index)
        self._next_index += 1
        return value

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self._data}'


if __name__ == '__main__':
    lista1 = MyList()
    lista1.add('Vinicius', 'Beato')
    lista1.add('Carlos')
    lista1.add('Jussara')
    lista1.add('Aleatório')
