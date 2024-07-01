from urllib import response

import mechanize

import os

import datetime

import sys

from time import sleep

browser = mechanize.Browser()

browser.set_handle_robots(False)

cookies = mechanize.CookieJar()

browser.set_cookiejar(cookies)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]

browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def openlink(msg4):

    r = browser.open(msg4)

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)
    print("\033[1;33;40m", end = "")
    msg1=str(input("➥✪➣T0W F4TUR3 COD3 D44L L4ND K3 T0P4 : "))
    
    print("\033[1;37;40m")

    browser.form['approvals_code'] = msg1

    r=browser.submit()

    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()
    
    
    
    
    
def poct(comment):

    browser.select_form(nr = 0)

    browser.form['comment_text'] = comment

    r = browser.submit()
    print("\033[1;32;40m", end = "")
    print ("\n[[ ࿇D3VIL-1NS1D3࿇ ]]\n")
    e = datetime.datetime.now()
    print (e.strftime("%d/%m/%Y   %I:%M:%S %p"))
    
os.system('clear')

sys.stdout.flush()

print("\033[1;33;40m", end = "")
print('===========================================================')
print('===========================================================')
print("\033[1;37;40m")
print("\033[1;33;40m", end = "")
emailx=str(input("➥✪➣T3R4 B44P DEVIL KING H EM41L D44L M4D4RCH0D : "))
print("\033[1;37;40m")
print("\033[1;33;40m", end = "")
pwx =str(input("➥✪➣P4SSW0RD D44L JH4TU : "))
print("\033[1;37;40m")

aclass()

print("\033[1;33;40m", end = "")
msg4=str(input("➥✪➣P0ST 1D D44L L0WD3 : "))
print("\033[1;37;40m")
print("\033[1;33;40m", end = "")
xxx= str(input('4PN4 N4M3 D44L G4NDU : '))
print("\033[1;37;40m")
print("\033[1;33;40m", end = "")
xx= str(input('H4T3RS K1 M4 CH0DN3 W4L3 K4 N4M3 D44L : '))
print("\033[1;37;40m")
print("\033[1;33;40m", end = "")
msg5=str(input("➥✪➣N0T3P4D3 F1L3 D44L CHUTIY3 : "))
print("\033[1;37;40m")
f=open(msg5, 'r')

lines = f.readlines()

f.close()

print("\033[1;33;40m", end = "")
msg6= int(input("➥✪➣D34LY T1M3 1N S3C D44L JH4T K3 B9L : "))
print("\033[1;37;40m")

os.system('clear')

sys.stdout.flush()

print("\033[1;33;40m", end = "")
print('===========================================================')
print("[-[ ✪✿✪✿✪ TH3 T00L P00L CR34T3D BY D3VIL INSIDE ✪✿✪✿✪ ]-]")
print('===========================================================')
print("\033[1;37;40m")

count = 0

while True:

    for line in lines:

        if len(line) > 3:

            if count != 0:

                sleep(msg6)

            openlink(msg4)

            poct(xxx+ ' ' +line + ' '+xx)

            print('Comm3nt G0n3 - ', xxx+ ' ' +line + ' '+xx)

            count += 1

            if count % 10 == 0:

                sleep(1)
