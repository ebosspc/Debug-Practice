# Print inputting instructions for the user
print("Welcome to the multifactor gui interface.")
print("Below you will be asked for a username and password. ")
print("Please ensure they are at least 8 and no morethan 24 characters.")
print("The password also must contain letters and numbers.")

# Define a variable that determines whether or not the entered credentials are valid according to the requirements
valid_creds = 0

# Define a function to get the user's credentials
def get_usr_credentials():
    # Globalize credential variables since they will be used in other functions
    global usr_username, usr_password

    # Get user username and password via the terminal
    usr_username = str(input("Please enter the username you want to use: "))
    usr_password = str(input("Please enter the password you want to use: "))

# Define a function to check if the user's credenitals meet the specified requirements
def check_credentials():
    # Globalize the variable that tracks whether or not the credentials are valid
    global valid_creds

    # Create tracking variables that track whether the password has numbers and letters
    password_has_letters = 0
    password_has_numbers = 0

    # Check if the username meets the character minimums and maximums
    if ((len(usr_username) >= 8) and (len(usr_username) <= 24)):
        # Check if the password meets the character minimums and maximums
        if ((len(usr_password) >= 8) and (len(usr_password) <= 24)):
            # For loop to check each character in the username for letters and numbers
            for i in usr_password:
                # Check if there are letters
                if i.isalpha():
                    password_has_letters = 1
                
                #Check if there are numbers
                if i.isdigit():
                    password_has_numbers = 1

            # Check if there are both letters and numbers
            if password_has_letters == 1 and password_has_numbers == 1:
                # Update valid credentials variable now that all credentials have passed all requirements
                valid_creds = 1
    
    # Print a message informaing the user's their credentials are invalid
    else:
        print("Sorry, those credentials are invalid. Please try again.")

# Create a while loop that will keep asking the user for valid credentials if the inputted ones don't meet the requirements
while valid_creds == 0:
    # Get the user's username and password and check if they meet the requirements
    get_usr_credentials()
    check_credentials()
