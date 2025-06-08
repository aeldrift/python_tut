# understanding time concept 

import time
lc_time=time.localtime()
# print(time)
print(lc_time.tm_hour)
print(lc_time.tm_min)

# To format local time ibnto readable string

for_time=time.strftime( "%y-%m%d %H:%M:%S")
print(for_time)
import time
time_stamp=time.time()
print(time_stamp)

# write a program to print the current time since epoch(i.e. January 1, 1970) in seconds

import time
c_time=time.time()
print("current time since epoch \(in sec\ is:")
print(c_time)

# To pause program for a few spoecified seconds like
 # time.sleep(5) will pauses yhe program for 5 sec after printing play1
import time 
print("play1")
time.sleep(5)   # It's like a blocking call.
print("play2")

# Exampes wity  half- second pauses
 
import time
for i in range(5):   #This program prints "Tick 1" to "Tick 5", with a 0.5 second delay between each print. 
    print("tick", i+1)       
    time.sleep(0.5)  

# program:
''' Writ a program to greet user according to the time of the day.'''

import time
current_time=time.localtime()
current_hour= current_time.tm_hour  # import time has a time model which further 
if (current_hour<12):               # has struct_time object which includes all year, hour, day etc. 
    print("Good Morning!")
elif (current_hour<17):
    print("Good Afternoon!")
elif(current_hour<20):
    print("Good evening!")
else:
    print("good night!")

# modified version of the above user greeting program

name=input("Enter user name:")
import time
current_time=time.localtime()
current_hour=current_time.tm_hour
if  current_hour<12:
    print("Good Morning!",name)
elif current_hour<17:
    print("Good Afternoon!",name)
elif current_hour<20:
    print("Good Evening!",name)
else:
    print("Good Night!",name)
    




