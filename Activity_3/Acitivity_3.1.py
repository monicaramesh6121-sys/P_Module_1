result = 3 + 4   # + is the operator
                 # 3 and 4 are the operands
print(result)    # Output: 7

total    = 120 + 85 + 150 + 95 + 110  # addition
earnings = total * 15                  # multiplication
average  = total / 5                   # division (float)
print(total, earnings, average)
# Output: 560  8400  112.0

total    = 560       # total harvest in kg
bag_size = 25        # each bag holds 25 kg

bags     = total // bag_size  # 560 // 25 = 22 full bags
leftover = total % bag_size   # 560 % 25  = 10 kg left over

print("Full bags:", bags)      # Output: 22
print("Leftover:", leftover)   # Output: 10

total     = 560
last_year = 500

print(total > last_year)   # True  — 560 is greater than 500
print(total == last_year)  # False — 560 is not equal to 500
print(total >= last_year)  # True  — 560 is at least as good
print(total < 400)         # False — 560 is not less than 400


total = 560        # = stores 560 into total
total += 30        # same as: total = total + 30
print(total)       # Output: 590
total -= 15        # same as: total = total - 15
print(total)       # Output: 575
bags = total // 25 # recalculate bags after update
print(bags)        # Output: 23


