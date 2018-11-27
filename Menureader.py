import os
from datetime import datetime
currdir = os.getcwd()
monthname = datetime.now().strftime('%B')
currday = datetime.now().day
currtime = datetime.now().hour
filenm = monthname+'.txt'
thefile = os.path.join(currdir, filenm)
try:
    with open(thefile) as f:
        text = f.readlines()
        if currtime > 13:
            pass  # Read tomorrow's menu
        else:
            pass  # Read today's menu
except FileNotFoundError:
    print("This month's file is not yet on here!")
