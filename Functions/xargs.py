"""Built a function to take more than one arq (colection)"""
def multiply(*numbers):
    total = 1
    for number in numbers:
        total += number
    return total    

# print(multiply(1,2,3,4,5))    

"""Collection of object with key and value"""

def save_user(**user):
    return user

user_info = save_user(id=1, name="koji", age=25, amaount=1234)  
print(user_info)

