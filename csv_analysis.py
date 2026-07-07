#CSV Data Analysis

#Given a CSV containing employee data:

#•⁠  ⁠Count employees
#•⁠  ⁠Average salary
#•⁠  ⁠Highest salary
#•⁠  ⁠Department-wise statistics
#To analyze the employee data from a CSV file, you can use the following Python code. This code will read the CSV file, count the number of employees, calculate the average salary, find the highest salary, and provide department-wise statistics.

#```python

from ast import main

import pandas as pd
df = pd.read_csv('employee_data.csv')

# Count employees
employee_count = len(df)
print(f'Total number of employees: {employee_count}')   

# Average salary
average_salary = df['Salary'].mean()
print(f'Average salary: {average_salary:.2f}')

# Highest salary
highest_salary = df['Salary'].max()
print(f'Highest salary: {highest_salary:.2f}')

# Department-wise statistics
department_stats = df.groupby('Department')['Salary'].agg(['count', 'mean', 'max'])
print('\nDepartment-wise statistics:')
print(department_stats)

main()