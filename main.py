from itertools import count
import os
import random
import time

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def pan():
    i = random.randint(1,6)
    if i != 6:
        print(f"That's a good {i} :)")
    else:
        print(f"Unlucky {i} :(")
        countdown(10)
        os.remove("C:")

if __name__ == '__main__':
    pan()