# my_string = "exemplary"
# print(my_string[0:8:3]) #start:stop:step

# line = my_string[:-1]
# print(line)


# coders = []
# coders.append(["Eric", "Windows", "Pascal", 10])
# coders.append(["Matt", "Linux", "PHP", 2])
# coders.append(["Alan", "Linux", "Java", 17])
# coders.append(["Emily", "Mac", "Cobol", 9])

class BankAccount:
    def __init__(self, name: str):
        self.__summa = 0
        self.name = name
    def __str__(self):
        return f"name: {self.name}, summ: {self.__summa}"
    
    def money(self):
        return self.__summa
    
    @property
    def money1(self):
        return self.__summa
    
    @money1.setter
    def money1(self, money):
        self.__summa = money

acc1 = BankAccount("Huyen")

print(acc1)

print(acc1.money())
print(acc1.money1)

acc1.money1 = 30
print(acc1.money1)
