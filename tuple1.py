myTuple = ("yash", 23, True, 4.5)
print(myTuple)
print(type(myTuple))
print(myTuple[0])
print(myTuple.count('yash'))

for i in myTuple:
    print(i)

# myTuple[1] = 24 # TypeError: 'tuple' object does not support item assignment

myTuple.append(5) # AttributeError: 'tuple' object has no attribute 'append'

myTuple = ("yash", 23, True, 4.5, 5)
print(myTuple)  # ('yash', 23, True, 4.5, 5)


