# Breaking out of a loop 


'''
for number in range(1, 4):
    print("Attempt", number, number * ".")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")  
'''    

def login_attempt(successful):
    for number in range(1, 4):
        # return "Attempt", number, number * "."
        if successful:
            return "Successful"
            break
    else:
        return "Attempted 3 times and failed"

login = login_attempt(True)
print(login)