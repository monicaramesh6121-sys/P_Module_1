#Activity — Smart School Day Planner

#You will build a Python program that takes three inputs — day, weather, and homework status — and uses if-elif-else, AND, OR, NOT, and combined conditions to print a personalised plan for the day.

# Title
# Smart School Day Planner
# Short description:
# A Python program that asks the user three questions. It classifies the day using if-elif-else. It uses AND to check sunny weather and homework done together. It uses OR to check rainy or cloudy weather. It uses NOT to catch homework not done. It combines all three operators to print the best plan for the day.

# Smart School Day Planner

print("=== Smart School Day Planner ===")
print("Answer 3 quick questions and I will plan your day!\n")

day      = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather  = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
homework = input("Is your homework done? (yes / no): ").strip().lower()

print()
print(f"=== Your Plan for {day} ===")
print("-" * 35)

# Topic 1 -- if-elif-else: classify the day
if day in ("Saturday", "Sunday"):
    print("Day type    : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type    : First day of the week. Pack your weekly planner.")
elif day == "Friday":
    print("Day type    : Last school day. Return library books today.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type    : Regular school day. Stay focused!")
else:
    print("Day type    : Day not recognised. Please check the spelling.")

# Topic 2 -- AND operator: sunny AND homework done
if weather == "sunny" and homework == "yes":
    print("After school: Head to the park - great weather and homework is done!")

# Topic 3 -- OR operator: rainy OR cloudy
if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Pack your umbrella - it may get wet outside.")

# Topic 4 -- NOT operator: homework NOT done
if not (homework == "yes"):
    print("Homework    : Not done yet. Finish it before going out!")

# Topic 5 -- Combining AND + OR + NOT together
if weather == "rainy" and not (homework == "yes"):
    print("Best plan   : Stay in, finish homework, then watch your favourite show.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : All set for a great school day - you are prepared!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")

print()
print("Plan complete! Have a wonderful day!")
