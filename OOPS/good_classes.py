class Car:
    # Constructer    
    def __init__(self,windows,tyres,engine,gear):
        
        # attributes
        self.windows = windows
        self.tyres = tyres
        self.engine = engine 
        self.gear = gear
    
    
    # methods
    def self_driving(self):
        print("the car is {} engine".format(self.engine))
    
    def gearing(self,gear):
        print("the car gear is {}".format(gear))    
        

car1 = Car(3,4,"petrol","manual")        
print(car1.tyres)
print("the no of windows of car1 is {}".format(car1.windows))

car1.self_driving()
car1.gearing('automatic')