import time
from plyer import notification

while True:
    print("Please drink some water")
    notification.notify(title = "Drink Water Reaminder", message = "You need to drink some water!")
    time.sleep(60*60)