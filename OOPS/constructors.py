# class Animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species
    
#     def __init__(self,name,species,age):
#         self.name = name
#         self.species = species
#         self.age = age
        
#     def roaring(self,sound):
#         print ("the roar sound is : {}".format(sound))
            
        
# # animal1 = Animal("lion","mammel") 
# # error

# animal1 = Animal("lion","mammel",22)
# print(animal1.name) 
# print (animal1.roaring("meaw"))  




class Animal:
    def __init__(self,*args):
        if len(args) == 1:
            self.name = args[0]
        if len(args) == 2:
            self.name = args[0]
            self.species = args[1]   
        if len(args) == 3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]  

animal2 = Animal("Tiger")        
print(animal2.name)    

