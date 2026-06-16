#Write a program to determine whether a word is a palindrome.
s = "madam"
# s = "hello" --- IGNORE ---
if s == s[::-1]:
    print(f"{s} is a palindrome.")
else:    print(f"{s} is not a palindrome.") 