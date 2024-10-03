from operator import truediv

from unicodedata import digit

password = input("Password?")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False

for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

if all(result) == True:
    print("good password")
else:
    print("shit password")
