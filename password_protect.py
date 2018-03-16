import sys
import getpass
import platform
import os
import time

loop = True
MASTER_KEY = getpass.getpass('Enter the MASTER KEY :');
l_masterkey = len(MASTER_KEY)
while loop:
	print("\t\t\t\t******************************************")
	print("\t\t\t\t*        Choose Option[1-4]              *")
	print("\t\t\t\t*        1> Insert New Record            *")
	print("\t\t\t\t*        2> Retrieve Data                *")
	print("\t\t\t\t*        3>Update Record                 *")
	print("\t\t\t\t*        4>All appname registerd         *")
	print("\t\t\t\t*        5>Quit                          *")
	print("\t\t\t\t******************************************")
	select = raw_input("Enter your Option : ")
	DEBUG = False
	PATH = ''

	if(platform.system()=='Windows'):
		PATH = 'D:\\'
		print os.chdir(PATH)
		try:
			fopen = open('pass_gen.txt','r+')
		except:
			print "One File is missing ..!"
			print "Lets Recover it ..!! :)"
			for i in range(5):
				print "processing ..."
				print "\033c"
				time.sleep(2)
			fopen = open('pass_gen.txt','a')
# Insert New Records Here 
	if(select=='1'):
		with open('pass_gen.txt','a+') as data_file:
			app_name = raw_input("Enter tha app name/Email id :").strip()
			password = getpass.getpass('Enter password for that :')
			if DEBUG:
				print(type(MASTER_KEY),type(password))
			add_info = temp = ''
			for i in range(len(password)):
				temp += chr(ord(password[i]) + ord(MASTER_KEY[i%(l_masterkey)]))
			choice = raw_input("Any additional info for this you want to save (y/n)")
			if choice=='y' or choice=='Y':
				add_info = raw_input("Enter the info :")
			else:
				add_info = ''
			data_file.write('\n'+app_name+'||'+temp+'||'+add_info);
		print "Password has been successfully Entered for {}!!".format(app_name)
		# Retrieve Records here 
	elif select=='2':
		flag = False
		app_name = raw_input("Enter the app name/Email id : ").strip()
		with open('pass_gen.txt','r+') as data_file:
			for line in data_file.readlines():
				if(line.split('||')[0] == app_name):
					temp = ''
					password = line.split('||')[1]
					print "Printing password",password
					for i in range(len(password)-1):
						temp += chr(ord(password[i])-ord(MASTER_KEY[i%(l_masterkey)]))
						if DEBUG:
							print temp,len(password)
					print("Your password for {} is {}".format(app_name,temp))
					print("Additional Information:")
					if line.split('||')[2]=='':
						print("Nothing Saved")
					else:
						print("{}".format(line.split('||')[2]))
					flag = True
					break
		if flag == False:
			print("No such app name found !!!")
	# Update any new information about record..!!
	elif select == '3':
		app_name = raw_input("Enter the app name/Email ID: ").strip()
		print("Select what you want to update (1)App Name/(2)Password/(3)Additional Info")
		choice = raw_input("Enter your choice [1-3]: ").strip()
		if(choice == '1'):
			with open('pass_gen.txt','r+') as data_file:
				for line in data_file.readlines():
					if(line.split('||')[0]==app_name):
						updName = raw_input("Enter new App name:").strip()
						print "coming here"
						line.split('||')[0] = updName
		elif(choice == '2'):
			pass
		elif(choice == '3'):
			pass
		else:
			print("You selected Inavlid Option .!!")
	# See all the app name registered till now..!!
	elif select =='4':
		with open('pass_gen.txt','r+') as data_file:
			print "All apps registered till now ."
			count = 0
			for line in data_file.readlines():
				if line.strip() not in  ['',None]:
					print '    %d. '%(count+1)+line.split('||')[0]
				count += 1
			print "%d App's/Email's are found"%(count)
	# For Exit ..!!
	elif select == '5':
		loop = False
	# When selection is Invalid
	else:
		print "Invalid Entry"

			



