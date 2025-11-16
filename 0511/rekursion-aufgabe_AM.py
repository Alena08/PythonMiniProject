def digitalSum(n):
    if n < 10:
        return n
    else:
     return n%10 + digitalSum(n // 10)
    
#print(digitalSum(2019))

def hailstone(n):
    if n == 1:
      return [1]
    
    elif n%2 == 1:
        next = 3*n+1
    else:
        next = n//2
    return [n] + hailstone(next)

print(*hailstone(5), sep="\n")  

