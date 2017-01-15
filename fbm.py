import fbchat
import os


login_details = os.path.expanduser('~') + '/.login' 

try:
	file = open(login_details,'r')
	email = 
except:
	email = input("Please enter your email-id:-")
	pwd = input("Please enter your password")

me = fbchat.Client(email,pwd)
