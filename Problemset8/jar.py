class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

        if self.capacity < 0:
            raise ValueError("Non negative number is not allowed")

    def __str__(self):
        if self.size == 0:
            return ""
        else:
            number_of_cookies = "🍪" * self.size
        return f"{number_of_cookies}"

    def deposit(self, n):
        if (self.size + n) <= self.capacity:
            self.size += n
            return f"{n} cookies has been added successfully"
        else:
            raise ValueError("Cookies exceed maximum capacity")

    def withdraw(self, n):
        if (self.size - n) >= 0:
            self.size -= n
            return f"{n} cookies has been removed successfully"
        else:
            raise ValueError("Cookie jar cannot be negative")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

