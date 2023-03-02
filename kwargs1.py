def sum(**kwargs):
    res=0
    for k, v in kwargs.items():
        res+= v
    return round(res, 2)

print(sum(coffee= 10, tea= 5, juice= 69.69))