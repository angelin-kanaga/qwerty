import os
import time
import datetime

os.system("color a")
os.system('cls')

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("                                           ________    ____________  __    _______   __________________     __________")
print("                                          / ____/ /   /  _/ ____/ /_/_/   / ____/ | / /_  __/ ____/ __ \   /_  __/ __ \\")
print("                                         / /   / /    / // /   / //      / __/ /  |/ / / / / __/ / /_/ /    / / / / / /")
print("                                        / /___/ /____/ // /___/ /| |    / /___/ /|  / / / / /___/ _/_ /    / / / /_/ /")
print("                                        \____/_____/___/\____/_/ |_|   /_____/_/ |_/ /_/ /_____/_/ |_|    /_/  \____/")
print("\n")
print("                                                                   ______________    ____  ______")
print("		                                                  / ___/_  __/   |  / __ \/_  __/")
print("		                                                  \__ \ / / / /| | / /_/ / / /")
print("			                                         ___/ // / / ___ |/ _/_ / / /")
input("			                                        /____//_/ /_/  |_/_/ |_| /_/\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
os.system('cls')

time.sleep(1)
os.system("cls")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("                                                      _   _   _____ ___   _____  ____ _   _  ___   ___  _")
print("                                                     |  \/  |/ ___/ ___| / ___| / ___| | | |/ _ \ / _ \| |")
os.system("color b")
time.sleep(0.5)
print("                                                     | |\/| | |  | |     \___ \| |   | |_| | | | | | | | |")
os.system("color 1")
time.sleep(0.5)
print("                                                     | |  | | |__| |___   ___) | |___|  _  | |_| | |_| | |___")
os.system("color 5")
time.sleep(0.5)
print("                                                     |_|  |_|\____\____| |____/ \____|_| |_|\___/ \___/|_____|")
os.system("color c")
time.sleep(2)
os.system("color a")
os.system("cls")
name=''
while(name == ''):
        os.system("cls")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        name=input("                                                                       |Type your full name\n                                                                       |==> ")
        if name != '':
                res=input("                                                               PRESS \"Y\" OR \"N\" & ENTER TO CONFIRM\n                                                                              ")
                
                if res in ("n","N","No","NO","no","NO"):
                        name=''

grade = ''
while(grade == ''):
        os.system("cls")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        grade=input("                                                                     |Type your grade or class\n                                                                     |==> ")
        if grade != '':
                res=input("                                                              PRESS \"Y\" OR \"N\" & ENTER TO CONFIRM\n                                                                              ")
                if res in ("n","N","No","NO","no","NO"):
                        grade=''

inter_sch = ''
while(inter_sch == ''):
        os.system("cls")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        inter_sch=input("                                                                     |Type your School name\n                                                                     |==> ")
        if inter_sch != '':
                res_1=input("                                                              PRESS \"Y\" OR \"N\" & ENTER TO CONFIRM\n                                                                              ")
                if res_1 in ("n","N","No","NO","no","NO"):
                        inter_sch=''

os.system('cls')
start=''
while start=='':
        os.system("cls")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("                                                         |Type \'Start\' but Don't press 'Enter' untill we inform")
        start=input("                                                         |-->")
        start=start.lower()
        if start=="start":
                hour = int(datetime.datetime.now().hour)
                minute = int(datetime.datetime.now().minute)
                second = int(datetime.datetime.now().second)
        else:
                start=''


os.system("cls")
print("===========================")
print("|Started at ",hour,":",minute,":",second,"|")
print("===========================")
print('')
time.sleep(5)

end= input("\n\n\n\n\n\n\n\n                                                                Press \'Enter\' when you finished\n                                                                              ")
os.system("cls")

print("===========")
print("| Results |")
print("===========")
print("\nName:", name,"\nClass:",grade,"\nSchool Name: ",inter_sch,"\n\nstarted at ", hour,":",minute,':',second)

hour_1 = int(datetime.datetime.now().hour)
minute_1 = int(datetime.datetime.now().minute)
second_1 = int(datetime.datetime.now().second)

print("finished at",hour_1,":",minute_1,":",second_1)


os.system("rundll32.exe user32.dll, LockWorkStation")
#Questions To Append Here
