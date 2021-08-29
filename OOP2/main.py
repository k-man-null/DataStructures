from P import People
from Student import Student

alice = People("Alice", "02/02/2020", "99998888", "alice@gmail.com")
bob = People("Bob", "01/01/2019", "12345678", "bob@gmail.com")

members = [alice, bob]
'''
print(alice.getName())
alice.setName("Ali")

for m in members:
  m.print()
'''

cat = Student("Catherine", "10/10/2010", "12344321", "cat@gmail.com", 999, "CU-CP", "PT", "SET")


cat.print()
cat.setName("ca")


members.append(cat)

# [alice, bob, cat]
for m in members:
  m.print()

