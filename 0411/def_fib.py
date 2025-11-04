def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
 
    elem_1 = 0
    elem_2 = 1
    the_sum = 0
    for i in range( n- 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum 
    return the_sum
for i in range(0,11):
    print(i, fib(i))