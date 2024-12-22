# 1. Importing Libraries
import pandas as pd
import numpy as np

# 2. Creating a DataFrame (similar to a table in a database)
# Data can be loaded from various sources, such as CSV files
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 55000, 60000, 65000, 70000]
}

df = pd.DataFrame(data)  # Creating a DataFrame from a dictionary
print("DataFrame:")
print(df)

# 3. Accessing and Manipulating Data in a DataFrame
# Accessing columns
print("\nAccessing the 'Age' column:")
print(df['Age'])

# Filtering rows based on a condition
print("\nRows where Age is greater than 30:")
filtered_data = df[df['Age'] > 30]
print(filtered_data)

# 4. Adding a new column to the DataFrame
# Let's calculate a 'Bonus' based on salary
df['Bonus'] = df['Salary'] * 0.1  # 10% bonus based on salary
print("\nDataFrame with Bonus column:")
print(df)

# 5. Using NumPy for mathematical operations on data
# Let's calculate the mean, standard deviation, and other statistics using NumPy
salary_mean = np.mean(df['Salary'])
salary_std = np.std(df['Salary'])
print("\nSalary Mean:", salary_mean)
print("Salary Standard Deviation:", salary_std)

# 6. Working with CSV files (Reading and Writing Data)
# Writing the DataFrame to a CSV file
df.to_csv('employee_data.csv', index=False)  # Save the DataFrame to a CSV file

# Reading the data back from the CSV file
df_from_csv = pd.read_csv('employee_data.csv')
print("\nData read from CSV:")
print(df_from_csv)

# 7. Grouping Data and Aggregation (using Pandas)
# Grouping by 'Age' and calculating the average salary (just for demonstration)
grouped_data = df.groupby('Age')['Salary'].mean()
print("\nAverage Salary grouped by Age:")
print(grouped_data)
