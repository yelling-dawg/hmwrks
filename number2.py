class Road:
    def __init__(self, length=None, width=None, weight=None, thefat=None):
        self._length, self._width = length, width
        self.weight, self.thefat = weight, thefat

    def TheMeth(self):
        return self._length * self._width * self.thefat * self.weight // 1000, "t"


a = Road(20, 5000, 25, 5)
print(*a.TheMeth())
