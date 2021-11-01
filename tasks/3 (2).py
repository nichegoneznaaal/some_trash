class Stationery():
    title = "name"

    def __init__(self):
        pass
    def draw(self):
        return ("Запуск отрисовки.")

class Pen(Stationery):
    def __init__(self):
        super(Stationery).__init__()

    def draw(self):
        print(f"{super().draw()} ручкой")

class Pencil(Stationery):
    def __init__(self):
        super(Stationery).__init__()

    def draw(self):
        print(f"{super().draw()} карандашем ")

class Handle(Stationery):
    def __init__(self):
        super(Stationery).__init__()

    def draw(self):
        return f"{super().draw()}, маркером "

cm = Stationery()
cmpen = Pen
cmpencil = Pencil
cmhandle = Handle

cmpencil.draw