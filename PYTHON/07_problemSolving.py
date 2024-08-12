"""
Problems

1. Write a program to display a person's name, age and address in three different lines
2. Write a program to swap two variables.
3. Write a program to convert a float into integer.
4. Write a program to take details from a student for ID-Card and the print it in different lines.
5. Write a program to take an user input as integer the convert to float.
"""

# 1. Write a program to display a person's name, age and address in three different lines
name = "Kapil"
age = 22
address = "Pune"

print(name)
print(age)
print(address)


# 2. Write a program to swap two variables.
x = 12
y = 15

# Swapping Method 1
temp = x
x = y
y = temp

print(x)
print(y)

# Swapping Method 2
x, y = y, x


# 3. Write a program to convert a float into integer.
z = 12.4
print(type(z))

z = int(z)
print(type(z))


# 4. Write a program to take details from a student for ID-Card and the print it in different lines.
print("Student ID-Card Details")
studentName = input("Enter Student Name: ")
studentAge = int(input("Enter Student Age: "))
studentGrade = input("Enter Grade: ")
studentEmail = input("Enter Email: ")
studentPhoneNo = input("Enter Phone Number: ")
print("Student Identity Card")
print("Name: ", studentName)
print("Age: ", studentAge)
print("Grade: ", studentGrade)
print("Email: ", studentEmail)
print("PhoneNumber: ", studentPhoneNo)


# 5. Write a program to take an user input as integer the convert to float.
num = int(input("Enter a Number: "))
print(num)
print(type(num))

num = float(num)
print("After Conversion", type(num))
print(num)