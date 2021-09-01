counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

#temperature = int(input("what is the tempature outside? "))

#if temperature > 80:
   # print("turn on the ac")
#else:
   # print("open the windows")


print("Starting Elif Section -----------------------------------------------------")
# What is the score
# score = int(input("What is your test score? "))

# Determine the grade

#if score >= 90:
   # print('Your grade is an A')
#elif score >= 80:
    #print('Your grade is a B.')
#elif score >= 70:
   # print('Your grade is a C')
#elif score >= 60:
   # print('Your grade is a D.')
#else:
  #45
  #  print('Your grade is an F... Donkey')

print("Starting Operators Section -----------------------------------------------------")
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is in Texas... Right?")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("arapahoe or el paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the List of Counties")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

print("For Loop for Dictionary---------------------------------------------------")

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county,voters in counties_dict.items():
        print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

print("------------------------")

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


