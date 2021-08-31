print("Hello Word")
counties = ["Arapahoe","Denver","Jefferson"]

# Add El Paso to the second position in the list. 

counties.insert(1, "El Paso")

# Remove Arapahoe from the list. 

counties.remove("Arapahoe")

# Make Denver the third item in the list, but keep Jefferson the second item in the list.  

counties.remove("Denver") 

counties.insert(2,"Denver")

# Add Arapahoe to the list. 

counties.append("Arapahoe")

print(counties)

counties.append("El Paso")

counties.insert(2,"El Paso")

counties.remove("El Paso")

counties.pop(3)

counties[2] = "El Paso"

print(counties)

# Lists and list comands
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
print("Starting Tuple Section ........")
counties_tuple = ("Arapahoe","Denver","Jefferson")
print(len(counties_tuple))
print(counties_tuple[:-1])

# Tuples
# ^^^^^^^^^^^^^^^^^^^^^^^^
print("Starting Dictionary Section .............")
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.values())
print(counties_dict.get("Arapahoe"))
print(counties_dict['Arapahoe'])


#Dictionaries
#^^^^^^^^^^^^^^^^^^^^^^^^^