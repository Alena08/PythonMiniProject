class Person:
    def __init__(self, name, gender, eyeColor, height, weight):
        self.__name = name
        self.__gender = gender
        self.__eyeColor = eyeColor
        self.__height = height
        self.__weight = weight

    def __str__(self):
        return f"Name: {self.__name}\n\
            Gender: {self.__gender}\n\
            Eye Color: {self.__eyeColor}\n\
            Height: {self.__height}\n\
            Weight: {self.__weight}"

# p = Person("Ali","Male","Braun",173,90)
# print(p)