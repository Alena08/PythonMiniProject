class Student:
    def __init__(self, name,homework_scores,quiz_scores, test_scores):
        self.name = name
        self.homework= homework_scores
        self.quizzes = quiz_scores
        self.tests= test_scores

    def get_average_score(self):
        return sum([self.homework, self.quizzes,self.tests])/3
    

