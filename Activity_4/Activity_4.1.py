if 5 > 0:
    print("5 is positive")
print("This line is outside the block")

is_raining = "yes"
if is_raining == "yes":
    print("Bring an umbrella!")
    
temperature = 15
if temperature < 20:
    print("Wear a jacket")
else:
    print("Wear a t-shirt")

#Title
#Weather Outfit Picker
#Short description:
#A Weather Outfit Picker that asks about temperature, rain, wind, and puddles,
#then uses if and if-else statements to decide what outfit, umbrella, windbreaker, and shoes to wear, all while keeping every block properly indented.
# PART 1: Ask for today's temperature
temperature = int(input("Enter today's temperature in Celsius: "))

# PART 2: Decide between a jacket and a t-shirt
if temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today.")
    print("Wear a", outfit)

# PART 3: Ask whether it is raining
is_raining = input("Is it raining today? (yes/no): ")

# PART 4: Add an umbrella reminder only if it is raining
if is_raining == "yes":
    print("Bring an umbrella!")

# PART 5: Ask for the wind speed
wind_speed = int(input("Enter the wind speed in km/h: "))

# PART 6: Decide whether a windbreaker is needed
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It is windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    needs_windbreaker = "no"
    print("It is calm today.")
    print("No windbreaker needed over your", outfit)

# PART 7: Ask whether there are puddles on the ground
has_puddles = input("Are there puddles on the ground? (yes/no): ")

# PART 8: Decide between boots and sneakers
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear", shoes)

# PART 9: This message always prints, no matter what was chosen above
print("")
print("Weather check complete!")

# PART 10: Print the final outfit summary
print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature)
print("Outfit Chosen:", outfit)
print("Raining:", is_raining)
print("Windbreaker Needed:", needs_windbreaker)
print("Shoes Chosen:", shoes)
print("===================================")
