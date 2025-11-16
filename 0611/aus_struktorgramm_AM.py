def teiler(a,b):
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a
    if b == 0:
        return a
    else:
        return b
    
print(teiler(20,16))



