import pyautogui as py 
import sys
import time as ti
import keyboard as key
from colorama import init, Fore
init(autoreset=True)
fast_or_slow = None
def tool_opps():
    print("what tool do you want to use")
    print("auto clicker[1]")
    print("text spammer[2]")
    print("costom spammer[3]")
    print("info[4]")
def fast_mode():
    for _ in range(How_many_times_do_you_want_to_spam):
        py.write(what_word_to_SPAM)
        ti.sleep(intervalkey)
        #very tiny hard coded break just so it picks it up
        ti.sleep(0.1)
        py.press("enter")
def slow_mode():
    for _ in range(How_many_times_do_you_want_to_spam):
        py.write(what_word_to_SPAM, interval=0.1)
        ti.sleep(intervalkey)
        #very tiny hard coded break just so it picks it up
        ti.sleep(0.1)
        py.press("enter")
def clear():
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()
tool_opps()
what_tool = input(":")
while what_tool == "":
    print(Fore.RED + "this can't be null")
    what_tool = input(":")
if what_tool == "4":
    print("mouse position")
    print(py.position())
    print("screen size")
    print(py.size())
elif what_tool == "2":
    clear()
    what_word_to_SPAM = input("what word would you like to spam:")
    while what_word_to_SPAM == "":
        clear()
        print(Fore.RED + "this can't be null")
        what_word_to_SPAM = input("what word would you like to spam:")
    clear()
    while True:
        try:
            How_many_times_do_you_want_to_spam = int(input("how many times would you like to spam:"))
            break
        except ValueError:
            clear()
            print(Fore.RED + " invaild number")
    clear()
    while True:
        try:
            intervalkey = float(input("interval between key press:"))
            break
        except ValueError:
            clear()
            print(Fore.RED + "invaild number")
    clear()
    f_or_slow = input("fast or slow mode? f/s:")
    # just trying a dif way to do this i know this isnt the cleanest way of doing it
    if f_or_slow == "f":
        fast_or_slow = True
    elif f_or_slow == "s":
        fast_or_slow = False
    if f_or_slow == "":
        print("auto set to slow mode")
    if fast_or_slow:
        print("press s to start")
        #just to be safe it dosen't get in the way in your chat box
        key.wait("s")
        py.press("backspace")
        fast_mode()
    else:
        print("press s to start")
        #just to be safe it dosen't get in the way in your chat box
        key.wait("s")
        py.press("backspace")
        slow_mode()
elif what_tool == "3":
    clear()
    what_button_to_spam = input("what button do you want to spam?")
else:
    print(Fore.RED + f"{what_tool} is not vaild")
input("\n")
