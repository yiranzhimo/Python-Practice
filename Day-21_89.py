class Person:
    def gender(self):
        return "ALL"


class Male(Person):
    def gender(self):
        return "Male"

class Female(Person):
    def gender(self):
        return "Female"

male = Male()
female = Female()
print(male.gender())
print(female.gender())
