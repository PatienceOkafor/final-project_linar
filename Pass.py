# to emulate android lockscreen
from time import sleep
from getpass import getpass

#30 seconds waiting time
#5 available trials

password = "QWERTYUIOP"
waiting_time = 30
retries = 5

#on a successful login trials
def login():
    print("login successful, Welcome to Dashboard")


#loop goes on continously
while True:
    pwd = getpass("enter password:")
    
    if pwd == password:
        login()
        break
    else:
        print(f"login failed, You've {retries}  chances left")
    

    if retries == 1:
        retries = 5
        sleep(30) #sleep for 30 seconds

    retries -= 1
