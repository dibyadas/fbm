import fbchat
import os


login_details = os.path.expanduser('~') + '/.login' 

try:
	file = open(login_details,'r')
	email = file.readline()
	pwd = file.readline()
	me = fbchat.Client(email,pwd)
	file.close()
except FileNotFoundError:
	email = input("Please enter your email-id:-")
	pwd = input("Please enter your password:-")
	file = open(login_details,'w')
	file.writelines(email)
	file.writelines("\n")
	file.writelines(pwd)
	me = fbchat.Client(email,pwd)
	file.close()



