from datetime import datetime
import time

def send_email():
    for i in range(10000):
        pass 


start = time.time() 
send_email()       
endtime = time.time() 
duration = endtime - start
print(duration)