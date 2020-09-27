class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print("запуск отрисовки...")


class Pen(Stationery):
    def draw(self):
        print("Я не пишу в космосе!")


class Pencil(Stationery):
    def draw(self):
        print("А я пишу")


class Handle(Stationery):
    def draw(self):
        print("я наверное пишу в космосе")


a, b, c, d = Stationery(), Pen(), Pencil(), Handle()
a.draw()
b.draw()
c.draw()
d.draw()
