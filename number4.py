class Car:
    def __init__(self, speed=None, color=None, name=None, is_police=False):
        self.speed = speed
    def show_speed(self):
        return "Текущяя скорость -", self.speed, "км/ч"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return "This is Los Santos Police, STOP YOUR VEHICLE NOOW. Превышение скорости -", self.speed, "км/ч при 60 км/ч разрешенных, если вас поймают то штраф будет в размере -", (
                    self.speed - 60) * 100, "руб."
        else:
            return "Текущяя скорость -", self.speed, "км/ч"


class SportCar(Car):
    def show_speed(self):
        if self.speed > 1000:
            return "Keep It Up! The speed is", self.speed, "km/h"
        else:
            return ["TFW, where is your speed, my granny moves faster, I'm sad, I ain't gonna say your km/h"]


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return ["This is Los Desperatos Police, STOP YOUR VEHICLE NOOW. Превышение скорости -", self.speed,
                    "км/ч при 40 км/ч разрешенных, если вас поймают то штраф будет в размере -", (
                            self.speed - 40) * 100, "руб."]
        else:
            return "Текущяя скорость -", self.speed, "км/ч"


class PoliceCar(Car):
    is_police = True

    @property
    def show_speed(self):
        if a.speed > 60 and self.speed < a.speed:
            return ["там подальше есть один невнимательный, но нужно разогнаться до", a.speed - self.speed + 1,
                    "км/ч чтобы догнать"]
        elif d.speed > 40 and self.speed < d.speed:
            return ["там подальше есть один невнимательный, но нужно разогнаться до", d.speed - self.speed + 1,
                    "км/ч чтобы догнать"]
        elif d.speed > 40 and self.speed > d.speed:
            return "там подальше есть один невнимательный, скоро догонишь"
        elif a.speed > 60 and self.speed > a.speed:
            return "там подальше есть один невнимательный, скоро догонишь"
        else:
            return "все тихо, а как жаль"


a = WorkCar(70)
b = SportCar(8000)
d = TownCar(80)
c = PoliceCar(50)
print(*a.show_speed())
print(*b.show_speed())
print(*c.show_speed)
print(*d.show_speed())
