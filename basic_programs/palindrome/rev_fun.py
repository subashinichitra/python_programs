# using built in reversed function

text = input("ENTER THE STRING: ")
reverse = ''.join(reversed(text))
if text == reverse:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")