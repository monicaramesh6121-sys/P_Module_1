a = 5   # binary: 0101
b = 3   # binary: 0011
print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~b)      # -4
print(a << b)  # 40
print(a >> b)  # 0

# Title
# Identity operator
# Short description:
#Write a program to illustrate the use of 'is' identity operator

# Python program to illustrate the use

# of 'is' identity operator


x = 5

if (type(x) is int):

    print("true")

else:

    print("false")

 
x = 5.5

if (type(x) is not float):

    print("true")

else:

    print("false")

 
x = 20

y = 20

if (x is y):

    print("x & y SAME identity")

 
y = 30

if (x is not y):

    print("x & y have DIFFERENT identity")
    

# Title
# Bitwise operator
# Short description:
# Write a program to apply the right shift and left shift bitwise operator.

a = 10

b = -10


# print bitwise right shift operator

print("a >> 1 =", a >> 1)

print("b >> 1 =", b >> 1)

 
a = 5

b = -10

 
# print bitwise left shift operator

print("a << 1 =", a << 1)

print("b << 1 =", b << 1)