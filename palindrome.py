def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1
    while startIndex < endIndex:
        if str[startIndex] != str[endIndex]:
            return False
        startIndex += 1
        endIndex -= 1
    return True

def main():
    while True:
        str = input("Enter a string: ").strip()
        if isPalindrome(str):
            print(str, "is a palindrome")
        else:
            print(str, "is not a palindrome")
        answer = input("Do you want to continue? (Y/N): ").strip().upper()
        if answer != "Y":
            break

main()
