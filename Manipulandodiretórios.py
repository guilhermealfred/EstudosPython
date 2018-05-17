#-*- coding: utf-8 -*-
import os,os.path,time
def withoutdirs():
	x = [1 for i in os.listdir(os.getcwd()) if os.path.isdir(i)]
	if x == []:
		return True
	return False
def withoutfiles():
	x = [1 for i in os.listdir(os.getcwd()) if os.path.isfile(i)]
	if x == []:
		return True
	return False
def show(current=os.getcwd()):
	print(current)
	try:
		os.system('clear')
		print(f"Percorrendo o diretório {current}")
		for raiz,dirs,files in os.walk(current):
			for d in dirs:
				print(f"    Current dir {os.path.join(raiz,d)}")
				for l in os.listdir(os.path.join(raiz,d)):
					print(f'     /{l}') if os.path.isdir(l) else print('     ',l)
			if withoutdirs():
				for f in files:
					print(f"   File-{f}")
	except:
		print("Something went wrong!")
def acess():

	if not withoutdirs():
		show(os.getcwd())
		try:
			dirr = input("Which directory you want to acess?: ")
			os.chdir(dirr)
			print('Current Directory: ',os.getcwd())
			show(os.getcwd())
			check = True
		except:
			print("Couldn't acess the directory!")
			print("Backing to Menu!")
			time.sleep(1)
	else:
		print("The current directory has no another one inside it.")

def open_file():
	if not withoutfiles():
		show(os.getcwd())
		try:
			file = input("Which file you wanna open?: ")
			if os.path.isfile(file):
				print("Opening.....")
				time.sleep(1)
				os.system(f'kwrite {file}')
			else: 
				raise FileNotFoundError
		except:
			print("Couldn't open the file!")
	else:
		print("The current directory has no a file inside it to open.")

def info():
	if not withoutfiles():
		show(os.getcwd())
		try:
			file = input('Which file or directory you wanna load information?:')
			print("Loading information....")
			time.sleep(1)
			print("    Creation date: %s"%time.ctime(os.path.getctime(file)))
			print("    Modification date: %s"%time.ctime(os.path.getmtime(file)))
			print("    Acess date: %s"%(time.ctime(os.path.getatime(file))))
			print("    Size: ",os.path.getsize(file),'B')
			if os.path.isfile(file):
				print(f'   Format: {os.path.splitext(file)[1]}')
		except:
			print("Couldn't load file information!")
	else:
		print("The current directory has no a file inside it to display information.")

def previous():
	os.chdir('..')
	print(f"Current dir: {os.getcwd()}")
	show(os.getcwd())
def search():
	if not withoutfiles():
		show(os.getcwd())
		try:
			file = input("Enter a file name: ")
			word = input("Which word you want to search for?: ")
			with open(file) as f:
				ocorrencias = {}
				for e,i in enumerate(f.readlines()):
					en = 0
					if word in i:
						ocorrencias[f'Line: {e+1}'] = []
						while i.find(word,en) != -1:
							beg = i.find(word,en)+1
							en = beg+len(word)
							ocorrencias[f'Line: {e+1}'].append((beg,en))
			if ocorrencias == {}:
				return print(f"There is no occurrences of '{word}' in the file")
				
			return print(ocorrencias)
		except:
			print("An unexpected error has occurred!")
	else:
		print("The current directory has no a file inside it to search for words.")

def menu():
	while True:
		print("""
----------------------MENU----------------------
1 - Acess a directory
2 - Open a file using KWrite
3 - Get some information of a file or a directory
4 - List current directory
5 - Go back to the previous directory
7 - Searching word occurrences in a file
6 - Exit
------------------------------------------------""")
		try:
			option = int(input("Your choice: : "))
			if option == 6:
				print("    See you!")
				time.sleep(0.5)
				break
			elif option == 1:
				acess()
			elif option == 2: 
				open_file()
			elif option == 3: 
				info()
			elif option == 4:
				show(os.getcwd())
			elif option == 5:
				previous()
			elif option == 7:
				search()
		except:
			print("Enter a number from 1 to 7")
			time.sleep(1)
menu()
