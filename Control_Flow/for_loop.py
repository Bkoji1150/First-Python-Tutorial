# Send a massage to user 3 times 

for number in range(3):
    print("Hey are you there?", number + 1, (number + 1) * ".")

print("-------------------------")
# Best practice 

for number in range(1, 4):
    print("Hey are you there?", number, number * ".")