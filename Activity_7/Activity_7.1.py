v, w, x, y = 4, 5, 8, 2
z = (v + w) * x / y
print(z)   # 36.0
name = "Alex"
age = 0
print(name == "Alex" or name == "John" and age >= 2)
# True - and is checked before or

numn = int(input())
numd = int(input())
if numn % numd == 0:
    print(str(numn) + " is divisible by " + str(numd))
else:
    print(str(numn) + " is not divisible by " + str(numd))
    
mean1 = 38
wrong_number = 36
correct_number = 56
total_number = 40
sum = mean1 * total_number
# sum = 1520 (the original, wrong total)
num2 = sum - ((wrong_number) - (correct_number))
# num2 = 1540 (the corrected total)
mean2 = num2 / total_number
# mean2 = 38.5 (the corrected mean)

# Title
# Operator precedence
# Short description:
# Write a program to understand how the operator precedence works

v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;   
print("Value of (v+w) * x/ y is ",  z)



name = "Alex"
age = 0
  
if name == "Alex" or name == "John" and age >= 2 : 
  print("Hello! Welcome.")
else :
  print("Good Bye!!")
  

# Title
# Divisible Number
# Short description:
# Write to check a number is divisible by another number.

print("Enter a Number (Numerator): ")
numn = int(input())
print("Enter a Number (denominator): ")
numd = int(input())

if numn%numd==0:
  print("\n" +str(numn)+ " is divisible by " +str(numd))
else:
  print("\n" +str(numn)+ " is not divisible by " +str(numd))