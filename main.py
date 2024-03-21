import os
from time import sleep
import pyautogui as auto
list1 = [
    #but the phone numbers on this list in this form 0534567890
    
]

msg = input("Write your message here: ")

Phone_Numbers = input("Write phone numbers (let spaces between them Ex : 05123456789 05123456987): ").split(" ")
delay = int(input("delay between messages: "))
for i in Phone_Numbers:
    print(i)
    n = 966000000000 + int(i)
    msg = "https://web.whatsapp.com/send?phone=" + str(n) +  "&text=" + msg 
    os.startfile(msg)
    sleep(delay)
    auto.press("Enter")
    sleep(0.5)

print("Done")
