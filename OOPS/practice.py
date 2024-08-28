class B:
    def __init__(self,name,value):
        self.name = name
        self.value = value
    
    def edit(self):
        print("Test B")

class A(B):
    def __init__(self,name,value,nice):
        super().__init__(name,value)  
        self.nice = nice 
    
    def edit(self):
        print("Test A")  
        

        
a = A("uttam","high","good")


# print(a.name) 
a.edit()      

print(dir(A))         