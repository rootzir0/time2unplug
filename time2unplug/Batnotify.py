import psutil
import time
from plyer import notification

#Notification Function
def notification(title,message):
    notification.notify(
        title=title
        message=message
        app_name='Time2Unplug',
        timeout=20
    )

#Main
def main():
    unplugged_threshold = 80 #Percentage to notify for unplugging
    plugged_threshold = 20 #Percentage for when to plugg your machines