from pprint import pprint
sentence = "This is a common interview question"
char_frequency = {}
k = v

for char  in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=2) 

"""more readable format"""

char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)

print(char_frequency_sorted[0])