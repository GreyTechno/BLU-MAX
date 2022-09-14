# Auther    : MR.GT
# Github    : @Grey Techno
# Instagram : @grey_techno

# Random Password Generator CLI(Command Line Interface)
# BLU-MAX Random Password Generator
# Codes Section Has Been Started

# Modules
import random
import string
import time
import os 
from typing import ParamSpecArgs
import colorama
from colorama import Fore, Back

# Used Colors
blue=Fore.BLUE
red=Fore.RED
green=Fore.GREEN
magenta=Fore.MAGENTA
reset=Fore.RESET

# variables
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPRSTUVWXYZ"
numbers="1234567890"
symbols="`~!@#$%^&*()_+={}[]:;|<>?/*"
string=lower+upper+numbers+symbols

# clear
def clr():
    import os
    if os.name == 'nt':
            os.system('cls')
    else:
            os.system('clear')

# banner
def banner():
    print("\n")
    print(red," ██████╗ ██╗     ██╗   ██╗      ███╗   ███╗ █████╗ ██╗  ██╗")
    print(red," ██╔══██╗██║     ██║   ██║      ████╗ ████║██╔══██╗╚██╗██╔╝")
    print(red," ██████╔╝██║     ██║   ██║█████╗██╔████╔██║███████║ ╚███╔╝ ")
    print(red," ██╔══██╗██║     ██║   ██║╚════╝██║╚██╔╝██║██╔══██║ ██╔██╗ ")
    print(red," ██████╔╝███████╗╚██████╔╝      ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗")
    print(red," ╚═════╝ ╚══════╝ ╚═════╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝",green," v 1.0\n")
    print(" -----------------------------------------------------------",reset)
    print(green,"    <<============"+blue+"{{"+green+"  Coded By MR.GT "+blue+"}}"+green+"============>>       ")
    print(green,"  <<============"+blue+"{{"+green+"  Github: @GreyTechno "+blue+"}}"+green+"============>>    ")
    print(green," <<============"+blue+"{{"+green+" Instagram: @grey_techno "+blue+"}}"+green+"============>> ")
    print(green,"-----------------------------------------------------------"+reset)

# update
def update():
    if os.system('$HOME/blu-max'):
        print("Updating BLU-MAX......!!!")
        time.sleep(2)
        os.system('cd $HOME')
        os.system('rm -rf blu-max')
        time.sleep(1)
        os.system('git clone https://github.com/')
        os.system('cd $HOME')
        os.system('cd blu-max/core/main.py')
    else:
        print("Updating BLU-MAX......!!!")
        time.sleep(2)
        os.system('cd $HOME')
        os.system('rm -rf blu-max')
        time.sleep(1)
        os.system('git clone https://github.com/')
        os.system('cd $HOME')
        os.system('cd blu-max/core/main.py')

# About
def about():
    print(" This Blu-Max Tool Is An Python Based Script")
    print(" This Tool Made In Python Programming Language")
    print(" This Tool Make Very Hard And Very Strong Passwords")
    print(" Which Create And Generate Random Passwords In Fraction Of Seconds")
    print(" This Tool Works On Rooted Android Device And Non Rooted Device")
    print(" I Hope You Like This Script")
    print("\n Thanks For Reading..!!!\n")
    print(" <--------------( Any Error Contect Me..!!! )-------------->")
    print(" -----------------------------------------------------------")
    print(" <==============(        [1] For Back       )==============>")
    print(" <==============(        [2] For Exit       )==============>")
    print(" -----------------------------------------------------------")
    time.sleep(1)
    c=input("\n ==>>> ")
    if c=='1' or c=='01' or c=='one':
        clr()
        time.sleep(1)
        main()
    elif c=='2' or c=='02' or c=='two':
        clr()
        time.sleep(1)
        banner()
        print(" Thanks For Using This Tool !!!\n Thank You !!!\n -----------------------------------------------------------\n")
        exit()

# Restart
def restart():
    print(green+"["+blue+"*"+green+"] Restarting....")
    time.sleep(1)
    clr()
    print(green+"["+blue+"*"+green+"] Restarting....")
    time.sleep(4)
    clr()
    main()


# Options
def main():
    clr()
    banner()
    print(green,"<===============("+blue+"  ["+green+"*"+blue+"]"+red+" Choose An Option"+green+"  )===============>")
    print(" -----------------------------------------------------------")
    print(green+" [ "+magenta+"01"+green+" ]  Start")
    print(green+" [ "+magenta+"02"+green+" ]  Update")
    print(green+" [ "+magenta+"03"+green+" ]  About")
    print(green+" [ "+magenta+"04"+green+" ]  Restart")
    print(green+" [ "+magenta+"05"+green+" ]  More")
    print(green+" [ "+magenta+"06"+green+" ]  Github")
    print(green+" [ "+magenta+"07"+green+" ]  Follow")
    print(green+" [ "+magenta+"08"+green+" ]  Chat")
    print(green+" [ "+magenta+"09"+green+" ]  Contact")
    print(green+" [ "+magenta+"10"+green+" ]  Exit",reset)
    a=input(green+" =====> "+blue)
# Conditions
    if a=='1' or a=='01' or a=='one':
        start(string)
    elif a=='2' or a=='02' or a=='two':
        update()
    elif a=='3' or a=='03' or a=='three':
        clr()
        time.sleep(1)
        banner()
        about()
    elif a=='4' or a=='04' or a=='four':
        restart()
    elif a=='5' or a=='05' or a=='five':
        time.sleep(1)
        os.system("termux-open-url https://github.com/GreyTechno/")
        main()
    elif a=='6' or a=='06' or a=='six':
        time.sleep(1)
        os.system("termux-open-url https://github.com/GreyTechno/")
        main()
    elif a=='7' or a=='07' or a=='seven':
        time.sleep(1)
        os.system("termux-open-url https://instagram.com/grey_techno/")
        main()
    elif a=='8' or a=='08' or a=='eight':
        time.sleep(1)
        os.system("termux-open-url https://instagram.com/grey_techno/")
        main()
    elif a=='9' or a=='09' or a=='nine':
        clr()
        time.sleep(1)
        banner()
        print("\n Contact Me On Instagram...")
        print("\n https://instagram.com/grey_techno/")
        time.sleep(1)
        os.system("termux-open-url https://instagram.com/grey_techno/")
        main()
    elif a=='10' or a=='ten':
        clr()
        time.sleep(1)
        banner()
        print(" I Hope You Like This Script....")
        print(" Thanks For Using This Tool !!!\n -----------------------------------------------------------\n")
        exit()
    else:
        print("Invalid Option ("+a+") !!!")
        time.sleep(2)
        clr()
        return main()

# Option [1]
def start(string):
    clr()
    time.sleep(1)
    banner()
    input(green+" Press Enter To Continue:\n =====> "+blue)
    clr()
    time.sleep(1)
    banner()
    print(green+" Enter The Length Of Password GraterThan(5):"+reset)
    a=input(green+" =====> "+blue)
    # a=int(a)
    if int(a)>88:
        print(green+"Maximum Limit Is (88)!!!"+reset)
        time.sleep(2)
        clr()
        return main(string)
    elif int(a)>4 :
        length=int(a)
        password="".join(random.sample(string,length))
        b=str(a)
        clr()
        print(green+"["+blue+"*"+green+"]"+red+" Generating Password...."+reset)
        time.sleep(2)
        clr()
        banner()
        print(green+" <================"+blue+"("+green+"    Enter To Restart    "+blue+")"+green+"===============>")
        print(green+" <================"+blue+"("+green+"      ["+magenta+"1"+green+"] For Exit      "+blue+")"+green+"===============>")
        print(green+" <================"+blue+"("+green+"   Generated Password   "+blue+")"+green+"===============>")
        print(green+" -----------------------------------------------------------",reset)
        time.sleep(1)
        print(green+" ==>>> "+blue,password)
        c=input(green+"\n ==>>> "+reset)
        if c=='':
            clr()
            time.sleep(1)
            main()
        elif c=='1' or c=='01' or c=='one':
            clr()
            time.sleep(1)
            banner()
            print(green+" I Hope You Like This Script....")
            print(" Thanks For Using This Tool !!!\n -----------------------------------------------------------\n"+reset)
            exit()
        else:
            clr()
            time.sleep(1)
            main()
    elif int(a)<5 :
        print(green+" Enter The Password GraterThan(5)!!!"+reset)
        time.sleep(2)
        clr()
        return start(string)
    else:
        print(green+"Invalid Option ("+a+") !!!"+reset)


main()

# Thanks For Reading....!!!
