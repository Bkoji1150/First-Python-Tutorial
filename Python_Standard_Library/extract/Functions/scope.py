""" Scope is region of the code where a variable is define """
# Bello
'''
def fizz_buzz(input):
    if (input % 3 and input % 5)==0:
        print("FizzBuzz") 
    if input % 5==0:
        print("Buzz")     
    # if input %3==0:
    #     print("Fizz")
    else:
        print(input)  

fizz_buzz(15)        
'''

# Mosh solution

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"  
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return  "Buzz"  
    return input
input = int(input("Enter: "))     
output = fizz_buzz(input)    
print(output)