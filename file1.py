# Create a file
f = open("file2.txt", "w")
f.write("Hello World")
f.close()

# # Open the file
# f = open("file1.txt", "r")
# print(f.read())

# store the file contents in a variable
f = open("file2.txt", "r")
file_contents = f.read()
print(file_contents)