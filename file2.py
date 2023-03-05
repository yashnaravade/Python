# # delete a file
# import os
# if os.path.exists("file1.txt"):
#   os.remove("file1.txt")
# else:
#     print("The file does not exist")

# edit a file 
f = open("file2.txt", "a")
# write on new line
f.write("\nThis is a new line")

# open and read the file after the appending:
f = open("file2.txt", "r")
print(f.read())

# escape characters 
# \n - new line
# \t - tab
# \\ - backslash
# \' - single quote
# \" - double quote



