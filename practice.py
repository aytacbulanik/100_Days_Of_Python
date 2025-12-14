import random
# name = "aytaç bulanık"
# if "a" not in name:
#     print("The letter 'a' is present in the name.")

# number = 12.753
# rounded_number = round(number,2)
# print("Rounded number:", rounded_number)

# newList = [1, 2, 3, 4, 5]
# newList.append(6)
# print("Updated list:", newList)

# newDict = {
#     "name": "aytaç",
#     "age": 25,
#     "city": "istanbul"
# }
# print(type(newDict["age"]))
# newDict["gender"] = "Fmale"
# print("Updated dictionary:", newDict)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.salary = 100000.0
    
#     def greet(self):
#         print(f"Merhaba {self.name}")

#     def updateSalary(self,point):
#         self.salary *= point

# class Employee(Person):
#     def __init__(self,name,age,position):
#         super().__init__(name,age)
#         self.position = position
# person1 = Person("aytaç",44)
# emp1 = Employee("kamil",44,"developer")
# emp1.updateSalary(0.6)
# person1.updateSalary(1.2)

# print(person1.salary)
# print(emp1.salary)

# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# newNumbers = [ n for n in numbers if n%2 == 0]
# print(newNumbers)
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# intList = [ int(n) for n in list_of_strings ]
# oddList = [n for n in intList if n%2 == 0]
# print(oddList.)

# names = ["ali","hülya","ahmet","mehmet","nimet"]
# newDict = { name : random.randint(1,100) for name in names}
# print(newDict)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weatherF = { day : (degrees*0.2)+273 for (day,degrees) in weather_c.items()}
print(weatherF)