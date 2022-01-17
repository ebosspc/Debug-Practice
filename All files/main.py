#####-Security Checker-#####

# Output intro message for the user
print("Let's check your security. Answer y or n to each of the questions.")

# Store string variables for the user's responses to the following questions
phish = input("Can you recognize phishing emails? ")
pw = input("Is your passord strong? ")
auth = input("Do you use multi-factor authentication? ")
enc = input("Do you know how to encrypt sensitive information? ")

# Determine if the user has good security habits and output a message informing the user if they don't have good habits
if (phish=='n' or pw=='n' or auth=='n' or enc=='n'):
    print("You can improve your security habits.")

# Output a message informing the user they have good security habits
else:
    print("You have good security habits.")
