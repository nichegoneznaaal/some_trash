class Car():
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
    def go(self):
        return("go")

    def stop(self):
        return("stop")

    def turn(self, direction):
        return(direction)

    def show_speed(self):
        return(self.speed)

class sport_car(Car):
    def show_speed(self):
        if self.speed > 300:
            return("d")
        else:
            return("s")

class police_car(Car):
    def __init__(self, speed, color, name, ispolice = True):
        super().__init__(speed, color, name)
        self.ispolice = ispolice
    def show_speed(self):
        if self.speed > 60:
            return("p", super().show_speed())
        else:
            return super().show_speed() 
s = police_car(200, "red", "gtr")
print(s.turn("left"))
print(s.show_speed())
s2 = sport_car(20, "red", "gtr")
print(s2.turn("right"))
print(s2.show_speed())


print(f' {s2.show_speed() } . {s.show_speed()}')