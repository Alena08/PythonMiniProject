def fib_number(n):

    a = 0
    b = 1
    if n == 0:
        print("The Fibonacci-number is  0")
    elif n ==1:
        print("The Fibonacci-number is  1")
    for i in range(2, n+1):
        n_fib = a + b
        a = b
        b = n_fib 
    return b


n = int(input("Give me a number: "))
print(fib_number(n))
# except:
#     print("I need an integer number")