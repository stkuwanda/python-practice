# numeric types: all are immutable

# int
num = 10
print(num, type(num))

# float
num1 = 10.5
print(num1, type(num1))

# complex
num2 = 10j
print(num2, type(num2))

# sequence type datatypes

# string
# is immutable
str1 = "hello world"
print(str1, type(str1))

# list
# is mutable
names = ["Simba", "Chichie", "Michel-nav"]
print(names, type(names))
print(names[2], type(names[2]))

# tuple
# is immutable
names = ("Simba", "Chichie", "Michel-nav", "Kuda")
print(names, type(names))
print(names[3], type(names[3]))

# dictionary
# is mutable
employee = {
    "name": "Michel-nav Kuwanda",
    "age": 22,
    "city": "San Jose",
    "country": "United States",
    "salary": 20000,
    "siblings": ("Christiana", "Kudakwashe")
}
print(employee, type(employee))
print(employee["siblings"], type(employee["siblings"]))

# set
# is mutable
employeeData = {'Simba', 34, 'Software Engineer', True}
print(employeeData, type(employeeData))
