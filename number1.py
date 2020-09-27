from time import sleep


class Trafficlights:
    __color = {"красный": 7, "желтый": 2, "зеленый": 5}

    def runnin(self):
        input("Нажмите \"Enter\" чтобы начать...")
        for i in self.__color.keys():
            print(i)
            sleep(self.__color[i])


a = Trafficlights()
a.runnin()
