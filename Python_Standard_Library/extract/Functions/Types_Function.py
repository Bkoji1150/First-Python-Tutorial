# There are 2 types of functions 
# 1- Perform a task
# 2- Return a value 

""" The greeting function perform a task"""
def greeting(name):
    print(f"Hello {name}\nWelcome onboard")


# greet("philo")

""" The greeting function Return a value """
def get_greeting(name):
    return f"Hello {name}\nWelcome onboard"


massage = get_greeting("philo")


# or we can write this massge to a file.
with open("content.txt", "w") as f:
    f.write(massage)
