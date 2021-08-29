from P import People

class Student(People):

  def __init__(self, n, dob, c, e, sid, course, mos, school):
    super().__init__(n, dob, c, e)
    self.studentID = sid
    self.course = course
    self.modeOfStudy = mos
    self.school = school

  def print(self):
    super().print()
    print("Student ID:", self.studentID, "\tCourse:", self.course)
    print("Mode of Study:", self.modeOfStudy, "\tSchool:", self.school)
    print("------------------------------------------------")
  