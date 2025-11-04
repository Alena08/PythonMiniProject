age = 17
match age:
    case age if age < 18: print("minor")
    case x if x >= 65: print("Senior")
    case _ : print("Adult")
print(age)