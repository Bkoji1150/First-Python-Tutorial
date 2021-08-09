

a = "Ashish"


b = "(This is my first print statement) W$#TRWEDGVDFABDFGAS G#$%T #$%#$% {} [] ()"

c = "This is line 1"
c = "This is line 2"
c = "This is line 3"



print(a)
print(b)
print(c)



"""
This code is to get file from 
s3 bucket using boto3 API



"""


#	This code is to get file from 
#	s3 bucket using boto3 API
#
#
#
#
#
#

# ""
# ''
# """
# """

a = 10
print(a)




x = 4
print(x)
x = "Ashish"
print(x)
x = 23.1 
print(x)



# Type Casting In Python
# To convert to string - use str()
# To convert to integer - use int()
# to convert to float - use float()

x = 3

print(type(x))

print(str(x))  # This should be 3 in quotes
print(int(x))  # 3 are int
print(float(x)) # 3.0 

a = "Ashish"
print(type(a))


# x = 3.645


print(str(x))  
print(int(x))  
print(float(x))


x = 3.645
y = str(x)
print(type(str(x))) # string
print(type(x))  # float

x = 3.645
print(x)
x = str(x)  # "3.645"
print(x)
x = float(x)
print(x)
x = int(x)  # 3
print(x)
x = float(x) # 3.0
print(x)

"""
x     y    z
"A", "B", "C"

"""

x = "A"
y = "B"
z = "C"
print(x)
print(y)
print(z)

x, y, z = "A", "B", "C"
print(x)
print(y)
print(z)
print(x,y,z)


age = 10
name = "Sam"

"Sam is 10 years old"

print(name + " is "+ str(age) +" years old")  # Basic

print(f"{name} is {age} years old")  # f string

x = 10

print(f"x is {x}")


x = 10
y = 20.5
z = True
a = "Ashish"


print(f"This {x} is just {a} a junk {z} statement {y} without {x} any {z} meaning")



x = 10
y = 20.5
z = True
a = "Ashish"


print(f"{x}{a}{z}{y}{x}{z}")


## String Index
# string is a list of characters



# print the first character of string

"""

s = "Hello World"



['H', 'e', 'l', 'l', 'o', 'x', 'W', 'o', 'r', 'l', 'd']
  0    1    2    3    4    5    6    7    8    9    10
  							-6	-5	-4	 -3	  -2	-1

# 0 indexing -- index starts at zero

"""


s = "Hello World"
print(s[0])
print(s[6])

print(s[0:5])


print(s[7:11])
print(s[-5:])
print(s[-5:11])




"""
# string index --    start_index(including) : end_index(excluding) : step ( how many characters)

					##  [1,5)  --  1,2,3,4
					##  (1,5]  --  2,3,4,5

					start_index : end_index-1


"""



# from this string take letters with even index

s = "Hello World"

print(s[::1])


s = "asfsdgsdg sdrterrhdfgh dfghdfhfgdh"
"Asfsdgsdg Sdrterrhdfgh Dfghdfhfgdh"


print(s.upper())

print(s.lower())

print(s.capitalize())

first = s.split(" ")[0]
second = s.split(" ")[1]
third = s.split(" ")[2]

print(first.capitalize(), second.capitalize(), third.capitalize())

x = "Ashish"

x.replace(x[3],x[3].upper())


print(x.replace("i","I"))

print(x.replace(x[5],x[5].upper(),2))

x = "Ashish"

index = x.rfind("s")

print(index)

print(x[:index] + x[index].upper() + x[index+1:])

print(x.split("i")[0] + "i" + x.split("i")[1].capitalize())





s = "   Hello World   "

print(s)
print(s.strip())


s = "Hello Iorld"
print(s)
print(s.replace("I","W"))

s = "This is a test statement for split method"

split_list = s.split(" ")

print(split_list[-1])



s = "Hello World"
print(s)
print(s.replace("o","0",1))