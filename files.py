with open("README.md") as f:
    content = f.read()
    print(content)


employee_file = open("employees.txt","r")

# for line in employee_file:
#     print(line)

# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

