class People:
  def __init__(self, n, dob, c, e):
    self.__name = n
    self.dateOfBirth = dob
    self.contact = c
    self.email = e

  def getName(self):
    return self.__name

  def setName(self, newName):
    if len(newName) > 4:
      self.__name = newName
    else:
      print("Error: name must have at least 4 character")

  def print(self):
    print("---------------------------------")
    print("Name:", self.__name, "\tDOB:", self.dateOfBirth)
    print("Contact:", self.contact, "\tEmail:", self.email)
    
  