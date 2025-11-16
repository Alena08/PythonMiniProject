class Person:
    def __init__(self, name,gender, eye, height, weight):
        self.name = name
        self.gender = gender
        self.eye = eye
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"Person {self.name} ist {self.gender}.\n \
            Person has {self.eye} eyes, ist {self.height} cm and {self.weight} kg."
    
# p = Person("Alena","female","braun", 170, 70)
# print(p)