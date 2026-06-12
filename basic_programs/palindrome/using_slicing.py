# This is for sequence types( string,list,tuple)
number = input("ENTER THE NUMBER: ")
reverse = number[::-1]
if number == reverse:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")
