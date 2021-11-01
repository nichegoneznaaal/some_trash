
class Worker():
    _test = {}
    def __init__(self, name, surname, position, wage, bonus, income = _test):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage":wage, "bonus": bonus }

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f"Имя сотрудника:{self.name}, Фамилия сотрудника{self.surname}")

    def get_total_income(self):
        print(f"Должность сотрудника: {self.position}")
        print("Заработная плата:",self.income["wage"])
        print("Премия:", self.income["bonus"])
work = Worker("Дмитрий", "О","Разработчик",20000,15000)
work1 = Position(Worker)
work1.get_full_name()
work1.get_total_income()
