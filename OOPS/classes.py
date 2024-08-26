# bad process

class Car:
    pass

car1 = Car()
car2 = Car()

print(car1)

car1.windows = 4
car1.tyres = 4
car1.engine = "diesel"



car2.windows = 6
car2.tyres = 6
car2.engine = "petrol"


# print(car1.engine)
# print(car2.windows)

print(dir(car1))