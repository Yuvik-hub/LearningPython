# ▶️ 1. Creating Variables and Assigning Values
name = "Yuvraaj"
age = 33
height = 1.73 # in meters
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)
# ✅ Task 1: Create variables for your city (string), number of kids (int), and has_pet (boolean)
city = "Surrey BC"
num_kids = 0
has_pet = True

print("Your city:", city)
print("Number of kids:", num_kids)
print("Has pet:", has_pet)
# ▶️ 2. Reassigning Variables
age = 33 # Happy birthday!
print("New age afer birthday:", age)
# ✅ Task 2: Change the value of your city variable to another city and print it
city = "Vancouver"
print("New city", city)
# ▶️ 3. Using Variables in Expressions
year_born = 2025 - age
print("Year born:", year_born)
# ✅ Task 3: Calculate the age your kids will be in 5 years and print
kids_age_in_5_years = num_kids + 5  # Assuming num_kids is the total number, change logic as needed
print("Kids' age in 5 years (assuming starting age = num_kids):", kids_age_in_5_years)
# ▶️ 4. Data Types Check
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))


# ✅ Task 4: Print the data type of your city, num_kids, and has_pet variables
print("Type of city:", type(city))
print("Type of num_kids:", type(num_kids))
print("Type of has_pet:", type(has_pet))
# ▶️ 5. String Concatenation Using Variables
greeting = "Hello, my name is " + name + " and I live in " + city + "."
print("" + greeting)

# ✅ Task 5: Create a sentence introducing yourself using your variables and print it

my_intro = f"My name is {name}, I am {age} years old, and I live in {city}."
print(my_intro)



