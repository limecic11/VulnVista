import pyfiglet
red_circle = "\033[91m●\033[0m"
green_circle  = "\033[38;5;82m●\033[0m" 
orange_circle = "\033[38;5;202m●\033[0m"
yellow_circle = "\033[38;5;226m●\033[0m"
gray_circle = "\033[90m●\033[0m"
text = "VulnVista"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)
print ("Credits to Eng:Abdelrahman Ahmed                   Twitter:abdelrahman1190")
print (" ")
print ("Attack Vector")
print ("[A] Network")
print("[B] Adjacent")
print("[C] Local")
print("[D] Physical")
AV_Input=input("===> ")

if AV_Input=="A" or AV_Input=="a":
    AV_Input=0.85
elif AV_Input=="B" or AV_Input=="b":
    AV_Input=0.62
elif AV_Input=="C" or AV_Input=="c":
    AV_Input=0.55
elif AV_Input=="D" or AV_Input=="d":
    AV_Input=0.22
else:
    print("Invalid Option")
    print("--------------------------------------------------------------")
    exit()
print("--------------------------------------------------------------")
print(" ")
print ("Attack Complexability")
print("[A] Low")
print("[B] High")
AC_Input=input("===> ")
if AC_Input=="A" or AC_Input=="a":
    AC_Input=0.77
elif AC_Input=="B" or AC_Input=="b":
    AC_Input=0.44
else:
    print("Invalid Option")
    print("--------------------------------------------------------------")
    exit()
print("--------------------------------------------------------------")
print(" ")
print ("Privileges Required")
print("[A] None")
print("[B] Low")
print("[C] High")
PR_Input=input("===> ")
if PR_Input=="A" or PR_Input=="a":
    PR_Input=0.85
elif PR_Input=="B" or PR_Input=="b":
    PR_Input=0.65
elif PR_Input=="C" or PR_Input=="c":
    PR_Input=0.385
else:
    print("Invalid Option")
    print("--------------------------------------------------------------")
    exit()
print("--------------------------------------------------------------")
print(" ")
print("User Interaction")
print("[A] None")
print("[B] Required")
UI_Input=input("===> ")
if UI_Input=="A" or UI_Input=="a":
    UI_Input=0.85
elif UI_Input=="B" or UI_Input=="b":
    UI_Input=0.62
else:
    print("Invalid Option")
    print("--------------------------------------------------------------")
    exit()
print("--------------------------------------------------------------")
print(" ")
print("Confidentiality")
print("[A] None")
print("[B] Low")
print("[C] High")
C_Input=input("===> ")
if C_Input=="A" or C_Input=="a":
    C_Input=0.00
elif C_Input=="B" or C_Input=="b":
    C_Input=0.22
elif C_Input=="C" or C_Input=="c":
    C_Input=0.56
else:
    print("Invalid Option")
    print("--------------------------------------------------------------")
    exit()
print("--------------------------------------------------------------")
print(" ")
print("Integrity")
print("[A] None")
print("[B] Low")
print("[C] High")
I_Input=input("===> ")
if I_Input=="A" or I_Input=="a":
    I_Input=0.00
elif I_Input=="B" or I_Input=="b":
    I_Input=0.22
elif I_Input=="C" or I_Input=="c":
    I_Input=0.56
else:
    print("Invalid Option")
    print("--------------------------------------------------------------")
    exit()
print("--------------------------------------------------------------")
print(" ")
print("Availability")
print("[A] None")
print("[B] Low")
print("[C] High")
A_Input=input("===> ")
if A_Input=="A" or A_Input=="a":
    A_Input=0.00
elif A_Input=="B" or A_Input=="b":
    A_Input=0.22
elif A_Input=="C" or A_Input=="c":
    A_Input=0.56
else:
    print("Invalid Option")
    print("--------------------------------------------------------------")
    exit()
impact= 1-((1-C_Input)*(1-I_Input)*(1-A_Input))
print("Scope")
print("[A] Changed")
print("[B] Unchanged")
scope=input("===> ")
if scope=="A" or scope=="a":
    impact_score=7.52*(impact-0.029)-3.25*(impact-0.02)**15
elif scope=="B" or scope=="b":
    impact_score=6.42*impact
else:
    print("Invalid Option")
    print("--------------------------------------------------------------")
    exit()
exploitability= 8.22* AV_Input* AC_Input * PR_Input * UI_Input
if impact_score <=0:
    base_score=0.00
elif scope=="A" or scope=="a":
    base_score=min(1.08*(impact_score + exploitability), 10)
elif scope=="B" or scope=="b":
    base_score=min((impact_score + exploitability),10)
if 9.0 <= base_score <=10.0:
    print("--------------------------------------------------------------")
    print(" ")
    print("Severity:")
    print(f"Critical {red_circle}")
elif 7.0 <= base_score <=8.9:
    print("--------------------------------------------------------------")
    print(" ")
    print("Severity:")
    print(f"High {orange_circle}")
elif 4.0<=base_score <=6.9:
    print("--------------------------------------------------------------")
    print(" ")
    print("Severity:")
    print(f"Medium {yellow_circle}")
elif 0.1<= base_score <= 3.9:
    print("--------------------------------------------------------------")
    print(" ")
    print("Severity:")
    print(f"Low {green_circle}")
else:
    print("--------------------------------------------------------------")
    print(" ")
    print("Severity:")
    print(" ")
    print(f"None {gray_circle}")
