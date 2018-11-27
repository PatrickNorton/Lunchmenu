import os
from datetime import datetime
currdir = os.getcwd()
monthname = datetime.now().strftime('%B')
currtime = datetime.now().hour
filenm = monthname+'.txt'
thefile = os.path.join(currdir, filenm)
with open(thefile) as f:
    text = f.readlines()
