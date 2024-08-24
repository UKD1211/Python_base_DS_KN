# # positional argument
# def hello(name,age):
#     print("hello" + name + "your age is " + str(age))
# hello("uttam",88)  

  
# # keyword arguments
# def hello(name,age=33):
#     print("hello" + name + "your age is " + str(age))
# hello("uttam")  


def hello(*args, **kwargs):
    print(args)
    print(kwargs)  
    
# hello("uttam","dutta",age=22,gender="male")    

lst = list(('uttam','dutta'))

dic_val = {'age': 32, 'gender': 'male'}

hello(*lst,**dic_val)

