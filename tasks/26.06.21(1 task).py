class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents
    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) == True:
            if value > 0:
                self.total_cents = self.total_cents % 100 + value * 100
            else:
                print("Error dollars")
        else:
            print("Error dollars")
    
    @property
    def cents(self):
        return self.total_cents % 100
    
    @cents.setter
    def cents(self, value):
        if isinstance(value, int) == True:
            if value < 100 and value > 0:
                self.total_cents = (self.total_cents - self.total_cents % 100) + value
            else:
                print("Error cents")
        else:
            print("Error cents")
     
    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов"



class Vector:
    def __init__(self, *args):
        self.values = args
        for i in self.values:
            if not isinstance(i,int):
                self.values.pop(i)
    def __str__(self):
        if len(self.values) > 0:
            self.values = ' '.join(self.values)
            self.values = self.values.split(" ")
            print(f"Вектор({str(', '.join(self.values))})")
            
        else:
            print("Пустой вектор")
            
        
        

           