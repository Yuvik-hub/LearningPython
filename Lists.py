# ▶️ 1. Create a List
fruits = ["apple", "banana", "cherry", "mango"]
print("initial List:", fruits)
# ✅ Task 1: Add "orange" to the list and print the updated list
fruits.append("orange")
print("After adding 'orange':", fruits)
# ▶️ 2. Accessing List Elements
print("First fruit:", fruits[0])  # index starts at 0
print("Last fruit:", fruits[-1])  # negative index starts from end
# ✅ Task 2: Print the second and third fruits using slicing
print("Second and third fruits:", fruits[1:3])
# ▶️ 3. Modifying Elements
fruits[1] = "blueberry"  # Changing banana to blueberry
print("After modification:", fruits)
# ✅ Task 3: Change "cherry" to "pineapple"
index_cherry = fruits.index("cherry")
fruits[index_cherry] = "pineapple"
print("After changing 'cherry' to 'pineapple':", fruits)
# ✅ Task 4: Add "lemon" at the beginning of the list
fruits.insert(0, "lemon")
print("After adding 'lemon' at beginning:", fruits)
# ▶️ 5. Removing Items
fruits.remove("apple")        # Removes first occurrence of "apple"
popped_fruit = fruits.pop()    # Removes first occurrence of "apple"
print("After removing 'apple' and popping last item:", fruits)
print("Popped fruit:", popped_fruit)
# ✅ Task 5: Remove "mango" and print the list
fruits.remove("mango")
print("After removing 'mango':", fruits)

# ▶️ 6. Sorting and Reversing
fruits.sort()
print("Sorted list:", fruits)

fruits.reverse()
print("Reversed list:", fruits)

# ✅ Task 6: Sort in reverse alphabetical order without changing original list
sorted_reversed = sorted(fruits, reverse=True)
print("Reverse-sorted (new list):", sorted_reversed)
print("Original list remains:", fruits)

# ▶️ 7. Iterating Over a List
print("Fruits one by one:")
for fruit in fruits:
    print("Fruit:", fruit)

# ✅ Task 7: Print each fruit in uppercase
print("Fruits in uppercase:")
for fruit in fruits:
    print(fruit.upper())

# ▶️ 8. List Comprehension
fruit_lengths = [len(fruit) for fruit in fruits]
print("Lengths of each fruit name:", fruit_lengths)

# ✅ Task 8: New list with fruits containing the letter 'e'
fruits_with_e = [fruit for fruit in fruits if 'e' in fruit]
print("Fruits with 'e':", fruits_with_e)



