import time
timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
timestamp = (int(time.strftime('%H'))+5)%24
# print(timestamp)
if(timestamp>=12 and timestamp<18):
    print("Good Afternoon!!")
elif(timestamp>=5 and timestamp<12):
    print("Good Morning!!")
elif(timestamp>=18 and timestamp<21):
    print("Good Evening!!")
else:
    print("Good Night!!")
timestamp = int(time.strftime('%M'))+30
# print(timestamp)
timestamp = time.strftime('%S')
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
