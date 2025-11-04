while True:
    jahr = input("Bitte Jahr von 1500 bis 2108: ")
    if jahr.isdigit():# and int(jahr) in range(1500, 2109):
        jahr = int(jahr)
        if 1500<=jahr<=2108:
            break
    else:
        print("Falsche Eingabe!")

# if jahr%400 == 0 or (jahr %4 == 0 and jahr%100 != 0):
#     print("Schaltjahr")
# else:
#     print("Normal Jahr")


if jahr % 4 != 0:
    print("Normal Jahr")
elif jahr % 100 == 0:
    if jahr % 400 == 0:
        print("Schaltjahr")
    else:
        print("Normal Jahr")
else:
    print("Schaltjahr")