#PYTHON PROGRAM FOR CLAIRE
import os
import pyttsx3
import getpass
import time
os.system("cls")
time.sleep (1)
print("--------------------------------------")
print("WELCOME TO MY TERMINAL USER INTERFACE ")
print("--------------------------------------")
pyttsx3.speak("welcome to my terminal user interface")
print("\n")
time.sleep(2)
print("------------------------------------------------------")
print("Execute any command of the system as per your choice")
print("------------------------------------------------------")
pyttsx3.speak("execute any command of the system as per your choice")
print("\n")
time.sleep(2)
pyttsx3.speak("Enter the password to get the access of the code")
print("======================================================")
access_password=getpass.getpass("To use the program, enter the password for the access: ")
if access_password == "redhat":	
	time.sleep(2)
	print("\n")
	print("---------------")
	print("ACCESS GRANTED")
	print("---------------")
	pyttsx3.speak("access granted")
	time.sleep(2)
	os.system("cls")
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("HELLO, MY NAME IS 'C.L.A.I.R'. HOPE YOU ARE DOING WELL")	
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	pyttsx3.speak("HELLO, MY NAME IS CLAIR. HOPE YOU ARE DOING WELL")
	time.sleep(1)
	print("\n")
	print("+++++++++++++++++++++++++++++++++++++++++++")
	print("GIVE YOUR ORDER, WHAT YOU WANT TO DO")
	print("+++++++++++++++++++++++++++++++++++++++++++")
	pyttsx3.speak("GIVE YOUR ORDER, WHAT YOU WANT TO DO")
	time.sleep(1)
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("THIS IS A BETA VERSION. SO, THE COMMANDS AVAILABLE RIGHT NOW ARE:- ")
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	pyttsx3.speak("THIS IS A BETA VERSION. SO, THE COMMANDS AVAILABLE RIGHT NOW ARE")
	time.sleep(1)
	print("1. Launching Chrome")
	time.sleep(1)
	print("2. Launching FireFox")
	time.sleep(1)
	print("3. Launching Control Panel")
	time.sleep(1)
	print("4. Launching Notepad")
	time.sleep(1)
	print("5. Launching Command Prompt")
	time.sleep(1)
	print("6. Launching Microsoft Paint")
	def main():
		while True:
			pyttsx3.speak("what are your orders")
			time.sleep(1)	
			print("++++++++++++++++++++++++++++")
			print("So, what do you wish to do: ", end="")
			your_order=input()
			if (('introduce' in your_order) or ('Introduce' in your_order) or ('INTRODUCE' in your_order)) and (('yourself' in your_order) or ('YOURSELF' in your_order) or ('Yourself' in your_order)):
				pyttsx3.speak("My name is clair. I am a program created to interact with your machine on your commands")
			elif (('run' in your_order) or ('Run' in your_order) or ('RUN' in your_order) or ('start' in your_order) or ('Start' in your_order) or ('START' in your_order)) and (('notepad' in your_order) or ('NOTEPAD' in your_order) or ('Notepad' in your_order)):
				pyttsx3.speak("Sure, executing the process right now")
				time.sleep(1)
				os.system("start notepad")   
			elif (('run' in your_order) or ('Run' in your_order) or ('RUN' in your_order) or ('start' in your_order) or ('Start' in your_order) or ('START' in your_order)) and (('chrome' in your_order) or ('CHROME' in your_order) or ('Chrome' in your_order)):
				pyttsx3.speak("No Problem. Executing the demand")
				time.sleep(1)
				os.system("start chrome")
			elif (('run' in your_order) or ('Run' in your_order) or ('RUN' in your_order) or ('start' in your_order) or ('Start' in your_order) or ('START' in your_order)) and (('control panel' in your_order) or ('CONTROL PANEL' in your_order) or ('Control Panel' in your_order)):
				pyttsx3.speak("starting control panel")
				time.sleep(1)
				os.system("start control panel")
			elif (('run' in your_order) or ('Run' in your_order) or ('RUN' in your_order) or ('start' in your_order) or ('Start' in your_order) or ('START' in your_order)) and (('firefox' in your_order) or ('FIREFOX' in your_order) or ('Firefox' in your_order)):
				pyttsx3.speak("ok then. Starting Firefox browser")
				time.sleep(1)
				os.system("start firefox")
			elif (('run' in your_order) or ('Run' in your_order) or ('RUN' in your_order) or ('start' in your_order) or ('Start' in your_order) or ('START' in your_order)) and (('MS PAINT' in your_order) or ('MS Paint' in your_order) or ('ms paint' in your_order)):
				pyttsx3.speak("Sure, starting MS paint right now")
				time.sleep(1)
				os.system("start mspaint")
			elif (('run' in your_order) or ('Run' in your_order) or ('RUN' in your_order) or ('start' in your_order) or ('Start' in your_order) or ('START' in your_order)) and (('command prompt' in your_order) or ('COMMAND PROMPT' in your_order) or ('Command Prompt' in your_order)):
				pyttsx3.speak("Gladly. Opening the command prompt in a moment")
				time.sleep(1)
				os.system("start cmd")
			elif ('exit' in your_order) or ('Exit' in your_order) or ('EXIT' in your_order) or ('quit' in your_order) or ('QUIT' in your_order) or ('Quit' in your_order):
				time.sleep(1)
				pyttsx3.speak("are you sure you want to exit the program")
				print("-------------------------------------------------------------")
				print("Are you sure you want to exit the program(Y/N): ", end="")
				choice=input()
				if ('y' in choice) or ('Y' in choice) or ('Yes' in choice) or ('YES' in choice) or ('yes' in choice):
					time.sleep(1)
					print("----------------------------------------------------------------------------------------")
					print("OK, IT's BEEN A FUN TIME WITH YOU. LET's HOPE TO MEET AGAIN")
					print("----------------------------------------------------------------------------------------")
					pyttsx3.speak("OK, IT's BEEN A FUN TIME WITH YOU. LET's HOPE TO MEET AGAIN")
					time.sleep(2)
					exit()
				else:
					main()		
			else:
				time.sleep(1)
				print("Sorry, I couldn't understand what you desire")
				pyttsx3.speak("Sorry, I couldn't understand what you desire")
	main()
else:
	print("\n")
	time.sleep(1)
	print("-----------------------------------------------------")
	print("OOPS......IT SEEMS LIKE THE PASSWORD IS INCORRECT")
	print("-----------------------------------------------------")
	pyttsx3.speak("oops, it seems like the password is incorrect")
	time.sleep(1)
	print("---------------------------------------")
	print("EXITING THE PROGRAM..........")
	print("---------------------------------------")
	pyttsx3.speak("EXITING THE PROGRAM")
	time.sleep(1)
	print("------------------------------------------")
	print("TRY TO EXECUTE THE PROGRAM AGAIN")
	print("------------------------------------------")
	pyttsx3.speak("TRY TO EXECUTE THE PROGRAM AGAIN")
	time.sleep(1)
	os.system("exit")







	


