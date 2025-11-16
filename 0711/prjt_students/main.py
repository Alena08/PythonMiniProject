from student import Student
from schoolClass import SchoolClass

dp = SchoolClass("FDP") #Object from SchoolClass calss

s1= Student("Ali",65,70,60)# OBJ from Student class
s2= Student("Maria",75,65,80)# OBJ from Student class
s3= Student("Rayen",70,65,88)# OBJ from Student class

# Add students to class 'dp'
dp.add_student(s1)
dp.add_student(s2)
dp.add_student(s3)


print(s1.get_average_score())
print(dp.get_class_average_grade())


