import pyautogui as pag
import time as t
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw()

# Made by Efendo

options = [
    "Generic Spammer",
    "Spam from a sillyScript",
    "Quit"
]

def parse(file):
    text=[]
    f=open(file, "r")
    for x in f:
            x = x.rstrip("\n")
            text.append(x)
    return text

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
        _ _ _     _____         _ 
    __(_) | |_  |_   _|__  ___| |
    (_-< | | | || || |/ _ \/ _ \ |
    /__/_|_|_|\_, ||_|\___/\___/_|
            |__/ 
    """, end="")
    print("         By Efendo")
    for i in range(0,len(options)):
        print(f"{i}) {options[i]}")
    print("")
    selected = input("What do you want to do: ")
    try:
        if int(selected) == 0:
            try:
                GenericSpammer()
            except:
                print("Something went wrong! Going back to main menu!")
                t.sleep(1)
                main()
        elif int(selected) == 1:
            try:
                SpamFromFile()
            except:
                print("Something went wrong! Going back to main menu!")
                t.sleep(1)
                main()
    except ValueError:
        print("Selection must be an Integer!")
        t.sleep(1)
        main()

def GenericSpammer():
    os.system('cls' if os.name == 'nt' else 'clear')
    message=input("Message: ")
    beforesend=input("Key to send before typing message (leave empty for nothing): ")
    delay=float(input("Delay: "))
    interval=float(input("Interval between letters: "))
    beforeStart=int(input("Time before start: "))
    repeat=int(input("How many messages: "))
    t.sleep(beforeStart)
    for i in range(0, repeat):
        pag.press(beforesend)
        pag.write(message, interval=interval)
        pag.press("enter")
        print(f"Sent message! {repeat-i} messages left.")
        t.sleep(delay)
    print("Finished!")
    main()

def SpamFromFile():
    os.system('cls' if os.name == 'nt' else 'clear')
    file=askopenfilename()
    messages=parse(file)
    beforesend=input("Key to send before typing message (leave empty for nothing): ")
    delay=float(input("delay: "))
    interval=float(input("Interval between letters: "))
    beforeStart=int(input("Time before start: "))
    t.sleep(beforeStart)
    for message in messages:
        pag.press(beforesend)
        pag.write(message, interval=interval)
        pag.press("enter")
        t.sleep(delay)
    print("Finished!")
    main()
    
main()