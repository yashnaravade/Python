#what are dictionaries?
#dictionaries are a collection of key-value pairs
#dictionaries are mutable
#dictionaries are unordered
#dictionaries are indexed by keys
#dictionaries are defined by curly braces
#dictionaries are accessed by keys
#dictionaries are iterated over by keys
#dictionaries are not sequences
#dictionaries are not hashable
#dictionaries are not sorted
#dictionaries are not unique

#Example 1

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dict1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(type(dict1)) # <class 'dict'>

print(dict1['a']) # 1

print(dict1['b']) # 2

# print(dict1['f']) # KeyError: 'f'

print(dict1.get('f')) # None

# operations on dictionaries

print(len(dict1)) # 5

print('a' in dict1) # True

print('f' in dict1) # False

print('a' not in dict1) # False

print('f' not in dict1) # True

