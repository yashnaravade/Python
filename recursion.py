#recursion example
def countdown(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
countdown(3)

# how does this work?
# 1. countdown(3) is called
# 2. n is 3, so the if statement is false
# 3. print(3)
# 4. countdown(2) is called
# 5. n is 2, so the if statement is false
# 6. print(2)
# 7. countdown(1) is called
# 8. n is 1, so the if statement is false
# 9. print(1)
# 10. countdown(0) is called
# 11. n is 0, so the if statement is true
# 12. print('Blastoff!')
# 13. countdown(0) returns
# 14. countdown(1) returns

