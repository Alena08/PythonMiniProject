class SchoolClass:

    def __init__(self, class_name):
        self.class_name=class_name
        self.students = []

    def add_student(self,student):
        self.students.append(student)
    
    def get_class_average_grade(self):
        return sum([student.get_average_score() for student in self.students])/len(self.students)
        