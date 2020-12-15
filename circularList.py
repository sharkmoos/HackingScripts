"""Instructions:

Take a character of the initial message and shift it to the right of the dictionary by its position in the message.

For example:
If the first character of the message is 'E' then it becomes 'F'. Second character, if it's 'n', becomes 'p'. Third character, if it's '_', becomes 'b' ETC.

If you reach the end of the message, do the whole process again.

Do it multiple times, until you are happy with the result.

Dictionary:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '<', '>', '{', '}', '[', ']', ',', '.', '-', '=', '_', '+']

~ Dr. Falken
"""
"""Scripting Nonsense"""
from itertools import cycle
dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '<', '>', '{', '}', '[', ']', ',', '.', '-', '=', '_', '+']
dictLen = len(dict)
message = "c2y.)xn5iWv]2yXK7HxOmcxq9FbS-9gXz.Nj_D"
result = []
happy = False
count = 1
for char in message:
    for i in dict:
        if char == i:
            pos = (dict.index(i)+count) % dictLen
            r = dict[pos]
            result.append(r)
            count += 1
print(''.join(result))

for i in range(100):
    for char in message:
        for i in dict:
            if char == i:
                pos = (dict.index(i)+count) % dictLen
                r = dict[pos]
                result.append(r)
                count += 1
    print(''.join(result) + "\n")
    message = ''.join(result)
    result = []
