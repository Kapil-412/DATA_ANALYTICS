# Conversion of one datatype to another is called as Type-Casting
name = "Kapil"
age = 22
height = 159.3

c = age + height

# type function give the datatype of variables
print(type(name))
print(type(age))

# 2 Types

# 1st Implicit ---> Conversion by python itself
print(c)
print(type(c))

# 2nd Explicit ---> User covnvert
a = int(name)
print("After Conversion", type(a))