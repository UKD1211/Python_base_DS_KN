
# function

# def welcome():
#     """Description: this will show the welcome message
#        Return: this will return the message  
#     """
#     # print("welcome home")
#     return "welcome India"
# welcome()    

# print(welcome())

# msg = welcome()
# msg

def welcome(msg):
    return msg
msg = welcome('hello')
print(msg)


# function to add even and odd numbers
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def sum(lst):
    sum_odd = 0
    sum_even = 0
    for i in lst:
        if (i%2 ==0):
            sum_even = sum_even + i
        else:
            sum_odd = sum_odd + i
                
    return sum_odd, sum_even

lst = [78378,4774,48883]

print(sum(lst))


