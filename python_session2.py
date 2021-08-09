
## Data Types
"""
string
int
float
"""

# a = 10
# b = 20

# comp = a > b

# print(type(comp))


## Operators

"""
+
-
*
/
%
**
//
=
+=
-=
*=
/=
==
>=
<=
>
<
!=
and
or
"""

# a = 5 
# b = 12
# print(b%a)


# a = 2
# b = 3
# print(a**b)


# a = 5 
# b = 17
# print(b//a)

# // %

# 17/5 = 3,2


# a = 19
# b = 5
# print(round(a/b))


# a = 10

# print(a <= 10)


# a = 10

# a /=2

# a += 1
# a = a + 1


# a -= 1
# a = a - 1

# a *= 1
# a = a * 1

# a /= 1
# a = a / 1



# print(a)



# 2^3 = 2*2*2

# 2^4 = 2*2*2*4

# 17 // 5 = 3

# a = 10
# c1 = a == 10
# c2 = a > 20
# print(c1 and c2)

# True and False --> False
# True and True --> True
# True or False --> True
# True or True  --> True

# a = 17

# print(a>=10 or a>=20)


# a = "Hello World"

# print(a)

# a = 10 

# print(a)
# print(10)
# print(True)
# print(5.2)
# print("Ashish")

##
##List
##


b = ["Ashish", "SAFSDF", "GFHFGH"]

a = [1,2,3,4,5,6,7, "Ashish", True, 4.26, 1,2,3,4,5,6,7, 1,2,3,4,5,6,7]

# print(lst2)

# print(type(True))

# print(type("True"))

# print(len(lst2))

# print(type([]))

# print(a[])

# a = "Ashish"

# lst_a = ["A", "S", "H", "I", "S", "H"]



# a = [1, 2, 3, [2, 4, 6], True, 4.5, "Ashish"]

## write a code to get length of all the items -- 14

# print(len(a[-1]))


# a = [1, 2, 3, 4]

## check if 3 is in the list

# b = 6
# if b in a:
# 	print(f"{b} is in the list")
# else:
# 	print(f"{b} is not in the list")


## append --> add items in the list

# a.append(6)
# print(a)

# a.append("Ashish")
# a.append(True)
# a.append(5.3434)
# print(a)

# x = a[4]
# print(x)
# a[4] = 5
# print(a)
# a.append(x)

# print(a)

# print(a[1])

#	 0  1  2  3  4
# a = [1, 2, 3, 4, 6]
# ## [1, 2, 3, 4, 5, 6]
# #   0  1  2  3  4  5
# print(a)
# t1 = a[4]
# print(t1)
# a[4] = 5
# a.append(t1)

# print(a)


## INSERT 

# a = [1, 2, 3, 4, 6]

# print(a)
# a.insert(4,5)

# print(a)


## EXTEND

# a = [1,2,3,4]

# b = [5,6,7,8]

# # print(a+b)

# # a = a + b
# print(a)

# a.extend(b)
# print(a)

# b.extend(a)
# print(b)


## REMOVE and POP 

# a = [1,2,3,4]

# print(a)

# # a.pop()   -- removes last item

# a.pop(0)

# print(a)


# a = [1,2,3,4,5,6,2,4,8,1,5,7,20]

# print(a)

# a.remove(2)
# print(a)
# a.remove(2)

# ## This is to remove an item from a list -- all occurences
# item_to_remove = 2
# try:
# 	while True:
# 		a.remove(item_to_remove)
# except ValueError:
# 	pass

# print(a)


## CLEAR

# a = [1,2,3,4]

# print(a)

# a.clear()

# print(a)

## DEL

# a = [1,2,3,4]
# print(a)
# del a
# print(a)

# a = [1,2,3,4]
# print(a)
# del a[1]
# print(a)

# a = [1,[2],3,4]
# a[1].clear()
# print(a)


## Looping Lists, List Comprehensions, Sorting Lists, Copy, Join, Filter, sort, map


## While
## For

"""

while condition:
	do something


"""

# x = 1
# while x < 10:
# 	print(x)
# 	x +=1
	

# 1. what code I need inside the loop
# 2. what should be the condition to enter the loop
# 3. how do I exit the loop


#    0 1 2 3 4 5 6 7 8 9
# a = [1,2,3,4,5,6,7,8,9,10]

## Loop through the items using while loop and then break as soon as you get 6 otherwise print items

	# if a[index] == 6:
	# 	break

# x = 0
# while x < len(a):
# 	print(a[x])
# 	x += 1




# start_index = 0
# last_index = len(a)-1
# print(start_index)
# print(last_index)

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# print(a[7])
# print(a[8])
# print(a[9])

#    0 1 2 3 4 5 6 7 8 9
a = [1,2,3,4,5,6,7,8,9,10]

x = 0

while x < len(a):
	print(a[x])
	x += 2


# x = 0
# 0 < 10 --> True
#   print(a[0]) --> 1

# x = 2
# 2 < 10 --> True
#  print(a[2]) --> 3

# x = 4
# 4 < 10 --> True
#  print(a[4]) --> 5

#    0 1 2 3 4 5 6 7 8 9
# a = [1,2,3,4,5,6,7,8,9,10]

# x = 2

# while x < len(a):
# 	print(a[x])
# 	x += 1

# x = 2
# 2 < 10 --> True
#  print(a[2]) --> 3

# x = 3
# 3 < 10 --> True
#  print(a[3]) --> 4



  











































