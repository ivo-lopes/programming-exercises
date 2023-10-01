from datetime import datetime
from time import sleep

while True:
    print(datetime.now().strftime('%H:%M:%S - %d/%m/%Y'))
    sleep(1)