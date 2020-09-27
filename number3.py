class Worker:
    def __init__(self, name=None, srname=None, pstion=None, wage=None, bonus=None):
        self.name = name
        self.surname = srname
        self.pstion = pstion
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def get_full_name(self):
        print(self.name + ' ' + self.surname)


a = Position("Michael", "Fury", "CEO", 1000000, 3000000)
print(a.get_total_income())
a.get_full_name()
