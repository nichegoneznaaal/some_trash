import time

class TrafficLight():
    __color = "red"
    def __init__(self, color = __color):
        self.color = color
    def running(self,):
        while True:
            if self.color == "red":
                print(self.color)
                time.sleep(7)
                self.color = "green"
                print(self.color)
                time.sleep(10)
                self.color = "orange"
                print(self.color)
                time.sleep(2.5)
                self.color = "red"
            else:
                print("Traffic light is broken")
                break

tl = TrafficLight()
tl.running("red")