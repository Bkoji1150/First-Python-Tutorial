letters = ["a", "b", "c"]
"""unpacking a list"""
first = letters[0]
second = letters[1]
third = letters[2]

first, second, third = letters


"""append to *other list"""
letters_send = ["a", "b", "c", "d", "f"]
first, second, third, *other = letters_send
print(first)
print(second)
print(other)