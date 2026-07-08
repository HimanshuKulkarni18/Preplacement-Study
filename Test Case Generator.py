#Test Case Generator

import random
import csv

def generate_test_cases(num_cases, num_elements):
    test_cases = []
    for _ in range(num_cases):
        case = [random.randint(1, 100) for _ in range(num_elements)]
        test_cases.append(case)
    return test_cases

def write_test_cases_to_csv(test_cases, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Test Case'] + [f'Element {i+1}' for i in range(len(test_cases[0]))])
        for i, case in enumerate(test_cases):
            writer.writerow([f'Test Case {i+1}'] + case)    
            
if __name__ == "__main__":  
    num_cases = int(input("Enter the number of test cases to generate: "))
    num_elements = int(input("Enter the number of elements in each test case: "))
    filename = input("Enter the filename to save the test cases (e.g., test_cases.csv): ")
    
    test_cases = generate_test_cases(num_cases, num_elements)
    write_test_cases_to_csv(test_cases, filename)
    
    print(f"{num_cases} test cases with {num_elements} elements each have been generated and saved to {filename}.")

