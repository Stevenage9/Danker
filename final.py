import pyautogui
import time

repeats=100000
print("Thanks for using this bot. For authorization, and program purpose, you must verify commands.")
time.sleep(1.5)

message1 = input("Type in the search command: ")
message2 = input("Type in the hunt command: ")
message3 = input("Type in the fish command: ")
message4 = input("Type in the dig command: ")
message5 = input("Type in the beg command: ")
message6 = input("Type in the crime command: ")

message7 = input("Text you type here will be used to separate sequence instances: ")

pressenter=input("Open discord window(maximised) and press enter")
print("Starting in 3 seconds...")
time.sleep(3)

for i in range(0, repeats):
    if message1 != "":
        pyautogui.typewrite(message1)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.click(390,915)
        time.sleep(9)

    if message2 != "":   
        pyautogui.typewrite(message2)
        pyautogui.press("enter")
        time.sleep(9)

    if message3 != "":
        pyautogui.typewrite(message3)
        pyautogui.press("enter")
        time.sleep(9)

    if message4 != "":
        pyautogui.typewrite(message4)
        pyautogui.press("enter")
        time.sleep(9)

    if message5 != "":
        pyautogui.typewrite(message5)
        pyautogui.press("enter")
        time.sleep(9)

    if message6 != "":
        pyautogui.typewrite(message6)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.click(390,915)
        time.sleep(9)

    if message7 != "":
        pyautogui.typewrite(message7)
        pyautogui.press("enter")
        time.sleep(2)
    else:
        pyautogui.typewrite("pls beg")
        pyautogui.press("enter")