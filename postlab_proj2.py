import random

class Student(object): 
    """Represents a student."""
    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
    def getName(self):
        """Returns the student's name."""
        return self.name
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score
    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __eq__(self, student):
        return self.name == student.name
    def __lt__(self, student):
        return self.name < student.name
    def __ge__(self, student):
        return self.name >= student.name
    def __str__(self):
        """Returns the string representation of the student."""
        return "Student: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    print("\nShowing Student List: ")
    
    print("\nStudent 1")
    student = Student("A", 5)
    for i in range(1, 6):
        student.setScore(i, 100-i)
    print(student)

    print("\nStudent 2")
    student2 = Student("B", 5)
    for j in range(1, 6):
        student2.setScore(j, 95-j)
    print(student2)

    print("\nStudent 3")
    student3 = Student("C", 5)
    for k in range(1, 6):
        student3.setScore(k, 90-k)
    print(student3)

    sd1 = student
    sd2 = student2
    sd3 = student3

    studentList = [sd1, sd2, sd3] 
    random.shuffle(studentList)
    print("\n\nBefore Sorting:")
    for i in range(0, len(studentList)):
        print(studentList[i], "\n")
    
    studentList.sort()
    print("\n\nAfter Sorting:")
    for i in range(0, len(studentList)):
        print(studentList[i], "\n")

if __name__ == "__main__":
    main()




