version = "0.4"

from time import sleep
import sys
import os
os.system("cls")
print("Loading...")
sleep(3)
os.system("cls")
print("******************** eBooker v" + version + " ********************")
print("")
sleep(1)

helpString = "eBooker v" + version + " Help\n==============" + ("=" * len(version)) + "\nhelp - show this help\nexit - quit this session\nabout - read about this tool\nedit - edit a file\nclear -  clear the screen\ndebug - give you help"
aboutString = "eBooker\nA command-line tool written in Python for writing Kindle eBooks. So far, it will just execute simple commands like \"help\" and \"exit.\" It can also create a file using the \"edit\" command. Version: Windows"
while True:
	cmd = str(input("ebooker > "))
	if cmd == "help":
		print(helpString)
	elif cmd == "exit":
		exitloopBool = True
		while exitloopBool:
			exitBool = str(input("Would you like to quit? (y/n) "))
			if exitBool == "y":
				exitloopBool = False
				os.system("cls")
				sys.exit()
			elif exitBool == "n":
				exitloopBool = False
				print("OK, not exited!")
			else:
				print("Please type in \"y\" or  \"n\".")
	elif cmd == "about":
		print(aboutString)
	elif cmd == "edit":
		editloopBool = True
		while editloopBool:
			editBool = str(input("Would you like to create a new file? (y/n) "))
			if editBool == "y":
				editloopBool = False
				print("You want to create a new file.")
				nameblankBool = True
				while nameblankBool:
					newfileString = input("What would you like it to be called? ")
					if (newfileString == "") or (newfileString == None) or (newfileString == " "):
						print("You must enter a filename.")
					else:
						print("Creating file...")
						sleep(3)
						open(newfileString, "a").close()
						print("Your file is created! Opening for edits...")
						nameblankBool = False
				sleep(2)
				os.system("notepad " + newfileString)
				print("If you got an error, use the \"debug\" command.")
			elif editBool == "n":
				editloopBool = False
				print("You want to edit an existing file!")
			else:
				print("Please type in \"y\" or  \"n\".")
	elif cmd == "clear":
		print("Clearing...")
		sleep(2)
		os.system("cls")
		print("******************** eBooker v" + version + " ********************")
		print("")
		sleep(1)
	elif cmd == "debug":
		print("Debugging help for Windows version:")
		print("Email me at ebooker.support@zoho.com with the error code for the error message you encountered.")
		print("|-----------------------|--------|")
		print("|Message                |Code    |")
		print("|-----------------------|--------|")
		print("|'notepad' is not       |64485253|")
		print("|recognized as an       |        |")
		print("|internal or external   |        |")
		print("|command, operable      |        |")
		print("|program or batch file. |        |")
		print("|-----------------------|--------|")
		print("|'nano' is not          |31131613|")
		print("|recognized as an       |        |")
		print("|internal or external   |        |")
		print("|command, operable      |        |")
		print("|program or batch file  |        |")
		print("|-----------------------|--------|")
		print("|other message          |93856898|")
		print("|-----------------------|--------|")
	else:
		print("\"" + cmd + "\" is not a valid command. Type \"help\" for more options")