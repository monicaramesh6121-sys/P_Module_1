# Title
# Mean Value
# Short description:
# The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.

mean1 = 38
wrong_number=36
correct_number=56
total_number=40
#sum of 40 numbers
sum = mean1*total_number
print("the sum of 40 number: ",sum)

#correct sum of these numbers
num2=sum-((wrong_number)-(correct_number))
print("sum-((wrong_number)-(correct_number)): ",num2)

#the correct mean
mean2=num2/total_number
print(mean2)

# Title
# Average speed
# Short description:
# Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?
a = int(input("enter a value: "))
b = int(input("enter value 2 :"))
c = int(input("enter value 3: "))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a:
    print("%d is just higher than %d" %(avg, a))
elif avg > b:
    print("%d is just higher than %d" %(avg, b))
elif avg > c:
    print("%d is just higher than %d" %(avg, c))
else:
  print("invalid input")