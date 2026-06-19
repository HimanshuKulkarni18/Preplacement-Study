# 8. Prime Number Checker
s = [39, 17, 23, 45, 67, 89, 12, 34, 56, 78]

def is_prime(num):
    if num <2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# Check which numbers in the list are prime
prime_numbers = [num for num in s if is_prime(num)]
print("Prime numbers in the list:", prime_numbers)