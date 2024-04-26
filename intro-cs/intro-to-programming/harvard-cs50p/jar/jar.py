class Jar:
    def __init__(self, capacity=12):
        invalid_capacity = (
            not isinstance(capacity, int)
            or capacity < 1
        )
        if invalid_capacity:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    def deposit(self, number):
        if self.__size_left() < number:
            raise ValueError
        self._size += number

    def withdraw(self, number):
        if self._size < number:
            raise ValueError
        self._size -= number

    def __str__(self):
        cookies = ""
        for _ in range(self._size):
            cookies +=  "🍪"
        return cookies

    def __size_left(self):
        return self._capacity - self._size
