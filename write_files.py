employee_file = open("employees.txt","r")

print(employee_file.read())

employee_file.close()

employee_file = open("employees.txt","a")

employee_file.write("\nToby")

employee_file.close()