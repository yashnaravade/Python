def find_fact(num):
    if num == 1:
        return 1
    else:
        return num * find_fact(num-1)

print(find_fact(6))

