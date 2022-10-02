import math
import random
import smtplib
from login import username, password

user_name = input("Enter your name: ")

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random()*10)]
otp_msg = "Hello, " + user_name + "\n" + OTP + " is your OTP" + "\n" + "Thank you"
msg = otp_msg

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(username, password)
email_id = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&', email_id, msg)
a = ""
while a != OTP:
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("Your OTP has been Verified \n Thank you")
    else:
        print("Sorry, That is incorrect \n Please try again")
