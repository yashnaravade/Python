num_list = [33, 42, 5, 66, 77, 22, 16, 79,
            36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

count = 0
for id, i in enumerate(num_list):
    if (i > 45):
        print(i , " is Over 45")
    else:
        print(i , " is Under 45")

    if (i == 36):
        print("Number found at position: " , id)

    count += 1

print(count)
