#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version Python 3.*

import string
import signal
#import hashlib
#import md5
#import getpass
import time
import os, sys, subprocess
from lib import Fore, Back, Style

#checkpassword = os.path.exists("/tmp/test/.tmp")
checkinit = os.path.exists("version")

# subprocess.call("rm nohup.out", shell=True)

print()
print()
print()
print()
print("Creazione del Database")
print("----------------------")
print()
print()
print()
#del raw_input
input("Premere un tasto per continuare!")
subprocess.call("touch db", shell=True)
print() 
raw_input = ()
print()
print()
time.sleep(1)
subprocess.call("clear", shell=True)
print()
print("  /---------------/")
print(" /     MENU'     /")
print("/---------------/")
print()
print()
print("[1] Aggiungi Cliente")
print("[2] Ricerca Cliente")
print("[3] Elimina Cliente")
print()
#print "[4] Esporta Database"
#print "[5] Importa Database"
print()
print()
print("[9] Info")
print()
print("[0] Esci")
print()
select = eval(input("Selezionare numero: "))
if select == 1:
	print()
	del raw_input
	print()
	time.sleep(1)
	name = input("Cliente: ")
	app = input("Applicazione: ")
	number = input("Password: ")
	stamp = '|Cliente: {nome} |Applicazione: {applicazione} |Password: {passwd} |\n'.format(nome=name, applicazione=app,passwd=number)
	info = (stamp)
	with open("db","a") as f:
			write_data = f.write(str(info))
			f.close
			subprocess.call("clear", shell=True)
if select == 2:
    print()
    del raw_input
    research = input("Cliente da cercare: ")
    print()
    searchfile = open("db", "r")
    for line in searchfile:
        if research in line:
            print(line)
            print()
            back = input("Premere un tasto per continuare ")
            subprocess.call("clear", shell=True)
if select == 3:
    del raw_input
    print()
    client = input("Cliente da eliminare: ")
    delete = "sed -i '/%s/d' db"
    os.system(delete % (client))
    #moved = "cp db.db %s.db"
    #os.system(moved % (file))
    #removed = "mv %s.db ."
    #os.system(removed % (file))
    print((Fore.BLACK + Back.GREEN + " Cliente Eliminato! " + Style.RESET_ALL))
    print()
    time.sleep(3)			
    subprocess.call("clear", shell=True)
if select == 9:
    subprocess.call("clear", shell=True)
    del raw_input
    print()
    print()
    print("/----------------------------------------------------/")
    print("|                        INFO                        |")
    print("|                        ----                        |")
    print("|                                                    |")
    print("| Software creato da: Alexis                         |")
    print("| Tester: Gianluca Di Filippo                        |")
    print("| Tester: Massimiliano Polli                         |")
    print("|                                                    |")
    print("| Programma per la gestione dati sensibili           |")	
    print("| Close Source per la protezione dei dati            |")
    print("|                                                    |")
    print("| Contatti:                                          |")
    print("| Sito: https://www.alexis82.it                      |")
    print("| E-Mail: giobbia82@gmail.com                        |")
    print("|----------------------------------------------------|")
    print()
    input("Premere un tasto per uscire")
    subprocess.call("clear", shell=True)
    subprocess.call("python3 databasetest.py", shell=True)
if select == 0:
	subprocess.call("clear", shell=True)
	#os.kill(os.getppid(), signal.SIGHUP)
	os.system("exit")
	#return
