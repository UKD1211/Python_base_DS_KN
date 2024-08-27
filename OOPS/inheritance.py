# inheritance
#  car class blueprint

class Car:
    def __init__(self,windows,doors,engine):
        self.windows = windows
        self.doors = doors
        self.engine = engine
        
    def driving(self):
        print("car is used for driving") 
        
         
# Audi car is inheriting from the Car class         
class Audi(Car):
    def __init__(self,windows,doors,engine,horsepower):
             super().__init__(windows,doors,engine) 
             self.horsepower = horsepower
             
    def self_driving(self):
             print("car is used for selfdriving")    
             
audi1 = Audi(3,4,"petrol",200)      

print(audi1.windows) 

audi1.driving()  
audi1.self_driving()

car1 = Car(2,4,"diesel")  

print(car1)  
print(audi1)

print(dir(audi1))
print(dir(car1))