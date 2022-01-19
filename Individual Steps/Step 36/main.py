# a215_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restircted app
my_auth = mfg.MultiFactorAuth()

my_auth.set_authorization("administrator3","1StrongPassword4CSP")
# confirm authorization info
auth_info = my_auth.get_authorization()
print(auth_info)

# set the users authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
