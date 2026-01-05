# revising basic Python concepts

# -----------------------------
# variables and data types

my_name = "Rahul"
my_age = 21
height = 5.8
is_student = True

print(my_name)
print(my_age)

print(type(my_name))
print(type(my_age))
print(type(height))
print(type(is_student))

print("-------------")


# -----------------------------
# string operations

line = "Learning Python is fun"

print(len(line))
print(line.lower())
print(line.upper())
print(line.title())
print(line.count("i"))
print(line.find("Python"))
print(line.replace("fun", "interesting"))
print(line.split(" "))

print("-------------")


# -----------------------------
# list operations

marks = [55, 67, 72, 80, 90]

marks.append(95)
print(marks)

marks.remove(67)
print(marks)

print(marks[0])
print(marks[1:4])

marks.sort()
print(marks)

marks.reverse()
print(marks)

print(len(marks))

print("-------------")


for m in marks:
    print(m)

for m in marks:
    print(m, "out of", 100)

print("-------------")


# -----------------------------
# tuple

subjects = ("Maths", "Physics", "Chemistry", "CS")
print(subjects)
print(type(subjects))

print(subjects[1])
print(len(subjects))
print(subjects.count("CS"))
print(subjects.index("Physics"))

for sub in subjects:
    print(sub)

for index, sub in enumerate(subjects):
    print(index, sub)

print("-------------")


# -----------------------------
# dictionary

student_info = {
    "name": "Rahul",
    "roll": 12,
    "branch": "Computer",
    "languages": ["Python", "C"]
}

print(student_info)
print(type(student_info))

print(student_info["name"])
print(student_info.get("branch"))
print(len(student_info))

student_info["roll"] = 15
print(student_info)

student_info.pop("languages")
print(student_info)

for key in student_info:
    print(key)

for key, value in student_info.items():
    print(key, ":", value)

print("-------------")


# -----------------------------
# set

ids = {101, 102, 103}
print(ids)
print(type(ids))

ids.add(104)
print(ids)

ids.remove(102)
print(ids)

print(len(ids))

for i in ids:
    print(i)

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

print("-------------")


# -----------------------------
# functions

def say_hello(name):
    return "Hello " + str(name)

print(say_hello("Rahul"))
print(say_hello(10))
print(type(say_hello))


def add_numbers(x, y):
    return x + y

total = add_numbers(8, 12)
print(total)

print("-------------")


# -----------------------------
# conditional statements

number = 7

if number > 0:
    print("positive number")
else:
    print("not positive")

print()

x = 10
y = 15

if x > y:
    print("x is greater")
elif x == y:
    print("both are equal")
else:
    print("y is greater")

print()

marks = 68

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

print("-------------")


# -----------------------------
# loops

for i in range(5):
    print(i)

print("-----")

for i in range(10):
    if i == 6:
        break
    print(i)

print("-----")

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print("-------------")


count = 0
while count < 5:
    print(count)
    count += 1

word = "Amazing"
i = 0

while i < len(word):
    if word[i] == "z":
        break
    print(word[i])
    i += 1

print("-------------")


# -----------------------------
# class and object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Name: {self.name}, Age: {self.age}"

p1 = Person("Rahul", 21)
print(p1.show_details())

print("-------------")
