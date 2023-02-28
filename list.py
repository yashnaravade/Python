list1 = [1,2,3,4,5,6,7]

# print(list1[0])
# print(list1[1])

print(*list1, sep = " ") # * is used to unpack the list  # 1 2 3 4 5 6 7

print(list1[0:3]) # 0 is inclusive and 3 is exclusive # This will print the first 3 elements of the list. It is called as slicing # [1, 2, 3]

print(list1[0:6:2]) # This will print the first 6 elements of the list with a step of 2.  # [1, 3, 5]

list1.insert(len(list1), 8) # This will insert 8 at the end of the list. # [1, 2, 3, 4, 5, 6, 7, 8]

print(list1) # [1, 2, 3, 4, 5, 6, 7, 8]

list1.append(9) # This will append 9 at the end of the list. # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(list1))

# print(list1.insert(9, 7))  
print(list1.insert(len(list1), 10)) 
#Why is is printing none?
#Because insert() is a void method. It does not return a value. 
#It inserts the value at the specified index and returns nothing.
#So, the print statement prints the value returned by the insert() method which is None.

# Use the len() function to get the length of the list and insert the value at that index. 
list1.insert(len(list1), 10)
print(list1)

list1.extend([11, 12, 13])
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13]

list1.remove(10)
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list1.pop(0) 
print(list1) # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # This will remove the element at index 0

del list1[0] # This will remove the element at index 0
print(list1) # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list1.reverse()
print(list1) # [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]

list1.sort()
print(list1) # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list1.sort(reverse = True)
print(list1) # [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]

list1.sort(reverse = False)
print(list1) # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in list1:
    print(i, end = " ") # 3 4 5 6 7 8 9 10 11 12 13

    

list1.clear() # This will clear the list
print(list1) # []