username_has_letters = 0
password_has_numbers = 0
inputstr = "Hello123"

# For loop to check each character in the username for letters and numbers
for i in inputstr:
    # Check if there are letters
    if i.isalpha():
        has_letters = 1
    
    #Check if there are numbers
    if i.isdigit():
        has_numbers = 1

if has_letters == 1 and has_numbers == 1:
    print("works")

else:
    print("doesn't work")