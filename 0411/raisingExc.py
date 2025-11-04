
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")

    if age < 0 or age > 150:
        #raise ValueError("Age range is invalid")
        raise Exception("Age range is invalid")
        #raise
        #raise ("Age range is invalid")

except ValueError as ex:
    print(ex)
    print("Invalid age was entered")

#except:
except Exception as e:
    print(e)
    print("Other exceptions occurred")

print("End")