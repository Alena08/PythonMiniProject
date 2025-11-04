def quadriere(x):
    return x**2

print(quadriere(5))

quad_func = lambda x: x*x
print(quad_func(5))

zahlen = [1,2,3,4,5,6,7,8,9,10]
gerade_zahlen = list(filter(lambda x: x%2==0, zahlen))

print(gerade_zahlen)