# 1. Variables and Data Types
# Python supports various data types: integers, floats, strings, booleans
integer_var = 10        # Integer
float_var = 3.14        # Float
string_var = "Hello!"   # String
boolean_var = True      # Boolean

# Print variables
print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)

# 2. Lists (Array-like structure)
# Lists are commonly used to store multiple items
data_list = [1, 2, 3, 4, 5]

# Accessing elements in a list (index starts from 0)
print("First item in list:", data_list[0])

# Modifying a list
data_list.append(6)  # Adding an item to the end of the list
print("Modified list:", data_list)

# 3. For Loops (Iteration)
# Loop through each item in the list
for num in data_list:
    print("Current number:", num)

# 4. Functions
# Functions are blocks of reusable code
def multiply(x, y):
    return x * y

# Call function
result = multiply(4, 5)
print("Multiplication Result:", result)

# 5. Simple Data Science Concept: Mean Calculation (List of Numbers)
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Example usage:
numbers = [10, 20, 30, 40, 50]
mean = calculate_mean(numbers)
print("Mean of numbers:", mean)

# 6. Conditional Statements (if-else)
# These are used to make decisions in your code
if mean > 25:
    print("The mean is greater than 25!")
else:
    print("The mean is less than or equal to 25.")
