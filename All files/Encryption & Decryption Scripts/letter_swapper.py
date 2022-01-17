#   a212_letter_swapper.py
#   Implementation of RSA cryptography 
#   using samples of large numbers

input_string = input("Enter the string to analyze: ")
new_string = input_string
temp_string = input_string
replace_letter = input("What letter in the orignal would you like to replace (qq to quit): ")


while (replace_letter != "qq"):
  replace_with = input("What letter would you like to replace it with (qq to quit): ")
  temp_string = input_string
  for i in range(0,len(temp_string)):
    if (replace_letter == input_string[i]):
      temp_string = temp_string[:i] + replace_with  +temp_string[i+1:]
      new_string = new_string[:i] + replace_with  +new_string[i+1:]
       
  print("")
  print ("Orginal String:" + input_string)
  print("")
  print ("New String:" + new_string)
  print("")

  replace_letter = input("What letter in the orignal would you like to replace (qq to quit): ")
