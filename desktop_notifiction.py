import time
import notification
from win10toast import ToastNotifier
 
Toast = ToastNotifier()
Toast.show_toast(
    "NOTIFICATION",
    "NOTIFICATION BODY",
    duration = 30,
    icon_path = "icon.ico",
    threaded = True
)
if __name__ == "__main__":
    while True:
        notification.notify(
        title = "ALERT PATIENCE!!!!!" ,
        message = "TIME TO CODE! YOU'VE BEEN SLEEPING",
        #displaying time
        timeout=10
)
        #waiting time 
        time.sleep(3600)
    


