# Title
# Membership operator
# Short description:
# Write a program to show students’ grades by entering marks for five subjects, calculating the average, and checking the grade range using membership operators in and not in. For example, use in to check whether the average is in the range 91 to 100, 81 to 90, and so on, and use not in to validate marks outside the allowed range.

print("Enter Marks Obtained in 5 Subjects:")

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot / 5)

validRange = range(0, 101)

if avg not in validRange:
    print("Invalid Input!")

elif avg in range(91, 101):
    print("Your Grade is A1")

elif avg in range(81, 91):
    print("Your Grade is A2")

elif avg in range(71, 81):
    print("Your Grade is B1")

elif avg in range(61, 71):
    print("Your Grade is B2")

elif avg in range(51, 61):
    print("Your Grade is C1")

elif avg in range(41, 51):
    print("Your Grade is C2")

elif avg in range(33, 41):
    print("Your Grade is D")

elif avg in range(21, 33):
    print("Your Grade is E1")

elif avg in range(0, 21):
    print("Your Grade is E2")