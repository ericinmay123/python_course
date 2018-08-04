class Student:
    """This is a class."""

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


class Chef:

    def make_chiken(self):
        print("Making a chicken.")

    def make_salad(self):
        print("Making a salad.")


class ChineseChef(Chef):

    def make_fish(self):
        print("Making a fish.")

    def make_fried_rice(self):
        print("Making fried rice.")
