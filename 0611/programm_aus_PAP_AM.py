a = int(input("gib eine Zahl a : "))
while True:
    b = int(input("b muss kleine als a sein: "))
    if b > a:
        continue
    break

while True:
    c = a - b
    if c == 0:
        print(a)
        break
    elif c >= b:
        a = c
    else:
        b = c
