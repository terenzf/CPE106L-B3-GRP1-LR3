"""
File: student.py
Resources to manage a student's name and test scores.
"""

"""
* Group Members: Flores, Gim, Muyot, Ramos, Louella
* Course & Section: CPE106L - B3
* Group Number: 1
* Date: March 28, 2022
* Filename: student1.py
"""

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
        return sum(self.scores) / len(self.scores)
   
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))


    #Method to compare two students studetns can be comapared based on the average marks
    #First method to check the equality .
    def isEqual(self,student):
      #Check if average are euqal if yes then students are equal
      if(self.getAverage() == student.getAverage()):
        return True
      else:
        return False
    #Method to check for less than
    def isLessThan(self,student):
      #Check if average of 1st student is less than the other
      if(self.getAverage()<student.getAverage()):
        return True
      else:
        return False
    #Method to check for greater than or equal to
    def isGreaterThanOrEqualTo(self,student ):
      #Check if the first one is greater than or equal to the other
      if(self.getAverage()>student.getAverage() or self.getAverage == student.getAverage()):
        #If yes then return true
        return True
      else:
        #If no then return false
        return False


def main():
    """A simple test."""
    student = Student("Renzo", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)
    print(student.getAverage())

    """A simple test 2 for the comparison functions"""
    #create two studetns
    student1 = Student("Terenz",6)
    student2 = Student("Louella",7)

    """Set their marks"""
    for i in range(1, 6):
        student1.setScore(i, 10*i+5)

    for i in range(1, 6):
        student1.setScore(i, 10*i+10)
   
    """Now call the comparison function"""

    #Should give false as they are not equal
    print(student1.isEqual(student2))
    #Should give false as student1 is not less than 2
    print(student1.isLessThan(student2))

    #should give true as student 1 is greater than 1
    print(student1.isGreaterThanOrEqualTo(student2))

if __name__ == "__main__":
    main()