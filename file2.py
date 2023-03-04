# delete a file
import os
if os.path.exists("file1.txt"):
  os.remove("file1.txt")
else:
    print("The file does not exist")
