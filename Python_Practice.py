counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

temperature = int(input("what is the tempature outside? "))

if temperature > 80:
    print("turn on the ac")
else:
    print("open the windows")


print("Starting Elif Section -----------------------------------------------------")
# What is the score
score = int(input("What is your test score? "))

# Determine the grade

if score >= 90:
    print('Your grade is an A')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F... Donkey')


if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is in Texas... Right?")