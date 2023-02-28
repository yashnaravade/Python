set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10}

print(set1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(type(set1)) # <class 'set'>

set1.add(11) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

print(set1 & set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

print(set1 - set2) # set() # empty set

print(set2 - set1) # {12, 13, 14, 15, 16, 17, 18, 19, 20}

print(set1 ^ set2) # {12, 13, 14, 15, 16, 17, 18, 19, 20} # symmetric difference of set1 and set2 (elements that are in either set1 or set2 but not in both) 

print(set1 <= set2) # True

print(set1 >= set2) # False

print(set1 < set2) # True

print(set1 > set2) # False

print(set1 == set2) # False

print(set1 != set2) # True

print(set1.issubset(set2)) # True

print(set1.issuperset(set2)) # False

print(set1.isdisjoint(set2)) # False # returns True if two sets have a null intersection (no common elements) 

print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20} # returns a new set with elements from both sets

print(set1.intersection(set2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} # returns a new set with elements that are common to both sets

print(set1.difference(set2)) # set() # returns a new set with elements in the set that are not in the others

print(set2.difference(set1)) # {12, 13, 14, 15, 16, 17, 18, 19, 20} # returns a new set with elements in the set that are not in the others
 
print(set1.symmetric_difference(set2)) # {12, 13, 14, 15, 16, 17, 18, 19, 20} # returns a new set with elements in either the set or other but not both 

print(set1.copy()) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} # returns a shallow copy of the set 

print(set1.pop()) # 1 # removes and returns an arbitrary set element