def sum(*args):
    res=0
    for x in args:
        res+=x
    return res
    
print(sum(4,5,6,8,9,7,1,19,10))