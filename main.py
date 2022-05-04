
class Employee:
    def __init__ (self,name,salary):
        self.name=name
        self.salary=salary
employees = [
    Employee("prude",60000),
    Employee("Joan",50000),
    Employee("Judith",40000),
    Employee("John",30000),
    Employee("Joy",20000),
]
for e in employees:
    if e.name=="prude":
      print(f"{e.name},${e.salary},Manager")
    if e.name=="Joan":
        print(f"{e.name}.${e.salary},Assistant Manager")
    if e.name=="Judith":
        print(f"{e.name},${e.salary},Product manager")
    if e.name=="John":
        print(f"{e.name},${e.salary},Consultant")
    if e.name=="Joy":
        print(f"{e.name},${e.salary},Cook")



