#Count the frequency of each character in a string.
def count_characters(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

# Example usage
input_string ="Hello, World!"
result = count_characters(input_string)
print(result)