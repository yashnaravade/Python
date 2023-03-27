def reversal(str):
    if len(str) == 0:
        return str
    else:
        return reversal(str[1:]) + str[0]

str = input("Enter a string to reverse: ")
print("The original string is: ", str)
print("The reversed string is: ", reversal(str))

# Output:
# Enter a string to reverse: Yash Naravade
# The original string is:  Yash Naravade
# The reversed string is:  edavaraN hsaY

# How it works:
# The function reversal() takes a string as an argument and returns the reversed string.
# The base case is when the length of the string is 0, then it returns the string.
# The recursive case is when the length of the string is not 0, then it returns the reversal of the string by slicing the string from index 1 to the end and adding the first character of the string to the end of the sliced string.

# Step 1: reversal("Yash Naravade")
# Step 2: reversal("ash Naravade") + "Y"
# Step 3: reversal("sh Naravade") + "a" + "Y"
# Step 4: reversal("h Naravade") + "s" + "a" + "Y"
# Step 5: reversal(" Naravade") + "h" + "s" + "a" + "Y"
# Step 6: reversal("Naravade") + " " + "h" + "s" + "a" + "Y"
# Step 7: reversal("aravade") + "N" + " " + "h" + "s" + "a" + "Y"
# Step 8: reversal("ravade") + "a" + "N" + " " + "h" + "s" + "a" + "Y"
# Step 9: reversal("avade") + "r" + "a" + "N" + " " + "h" + "s" + "a" + "Y"
# Step 10: reversal("vade") + "a" + "r" + "a" + "N" + " " + "h" + "s" + "a" + "Y"
# Step 11: reversal("ade") + "v" + "a" + "r" + "a" + "N" + " " + "h" + "s" + "a" + "Y"
# Step 12: reversal("de") + "a" + "v" + "a" + "r" + "a" + "N" + " " + "h" + "s" + "a" + "Y"
# Step 13: reversal("e") + "d" + "a" + "v" + "a" + "r" + "a" + "N" + " " + "h" + "s" + "a" + "Y"
# Step 14: "e" + "d" + "a" + "v" + "a" + "r" + "a" + "N" + " " + "h" + "s" + "a" + "Y"


