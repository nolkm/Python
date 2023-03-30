
import time 
import sys 

def loadingBar(percentage): 
    sys.stdout.write('\r') 

    if percentage == 100: 
        print("SYS.MSG = PLease wait as We Process the Login... ")
        sys.stdout.write(" SUCCESSFULLY CONNECTED! \033[92m[%-20s] %d%%\033[0m" % ('\033[92m=\033[0m'*int(percentage/5), percentage))
    else: 
        sys.stdout.write("Attempting to Connect: [%-20s] %d%%" % ('='*int(percentage/5), percentage)) 
    sys.stdout.flush() 

for x in range(101): 
    loadingBar(x) 
    time.sleep(0.001)