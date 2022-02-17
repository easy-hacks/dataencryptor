from cryptography.fernet import Fernet
from time import sleep
from os import sys
import os
Granted=False
def printf(string):
  string=string+"\n"
  for letter in string:
    sleep(0.03) 
    sys.stdout.write(letter)
    sys.stdout.flush()
printf("  [1]  LOGIN\n  [2]  REGISTER\n")

abc=open("DATABASE.txt","a")
abc.close()

def register():
		print("###########################################################\n                ####    SIGN UP    ####\n###########################################################\n")
		with  open("DATABASE.txt",'r+') as x:
			Username_register=input("	--> USER NAME    :    ")
			usenames=[]
			for line in x:
				i=line.split("#")
				usenames+=i
			while Username_register in usenames:
				printf("USER NAME TAKEN")
				Username_register=input("	--> USER NAME    :    ")
			Password_register=input("	--> PASSWORD     :    ")
			x.write(Username_register+'#'+Password_register+"\n")
			x.close()


def loginu():
	global Granted
	print("###########################################################\n                ####    SIGN IN    ####\n###########################################################\n")
	Username_login=input("  --> USER NAME    :    ")
	Password_login=input("  --> PASSWORD     :    ")
	with open("DATABASE.txt",'r') as x:
		for liner in x:
			i=liner.split("#")
			user_name,pass_word=i[0],i[1][:-1]
			Granted= Username_login==user_name and Password_login==pass_word

login=input("     ")
if login=="1":
	loginu()
if login=="2":
	register()
if login=="2":
	loginu()
if Granted:
	printf("Logged in succesfully")
	printf("    [1]    ENCRYPT A TEXT FILE\n    [2]    DECRYPT A TEXT FILE")
	grad=int(input("        "))
	if grad == 1 :
		file=input("Enter file path :")
		b=file.split(".")
		x=open(file,"r")
		message=x.read()
		x.close()
		x=open(file,"w+")
		key = Fernet.generate_key()
		b=file[0]+"."+key.decode('UTF-8')
		fernet = Fernet(key)
		encMessage = fernet.encrypt(message.encode())
		encMessage=encMessage.decode('UTF-8')
		x.write(encMessage)
		x.close()
		os.rename(file,b)
		print("YOUR NEW ENCRYPTED FILE IS : \n",b)
		
		
	if grad == 2 :
		file=input("Enter file path :")
		x=open(file,"r")
		encMessage=x.read()
		x.close()
		x=open(file,"w")
		b=file.split(".")
		key = b[-1].encode('UTF-8')
		fernet = Fernet(key)
		encMessage=encMessage.encode('UTF-8')
		decMessage = fernet.decrypt(encMessage).decode()
		x.write(decMessage)
		x.close()
		v=file[0]+"."+"txt"
		os.rename(file,v)
		print("YOUR NEW DECRYPTED FILE IS :\n",v)
else:
    print("User name and password incorrect")