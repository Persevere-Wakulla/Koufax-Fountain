# daemon thread = A thread that runs in the background, not important for the program to run
#                 your program will not wait for daemon threadsto complete before exiting
#                 non-daemon threads connot normally be killed, stay alive until task is complete

#                ex. background tasks, garbage collection, waiting for input, long runiing processes

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")
        
x = threading.Thread(target=timer, daemon=True
                     )
x.start()




answer = input("Do you wish to exit?")