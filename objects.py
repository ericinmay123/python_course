import class_and_object

Tom = class_and_object.Student("Tom", "History", 3.4, True)
Pam = class_and_object.Student("Pam", "Art", 4.0, True)
Kate = class_and_object.Student("Kate", "Marketing", 3.9, False)
print(Tom.gpa)
print(Kate.major)

print(Tom.on_honor_roll())
print(Pam.on_honor_roll())

myChineseChef = class_and_object.ChineseChef()
myChineseChef.make_chiken()
myChineseChef.make_fried_rice()
