"""
Multiple tasks or a big Tasks break down into  small task called thread
Every Execution has one Thread --> Main Thread
need to change  everry class to --> sub class of main thread 
For simultanious execution of two  or more methods --> Need to sleep for sometime like one sec..
at some time COLLISION may Happen to avoid that  --> sleep in b/w that [ specific thread.start() ] methods
To Execote the rest code after the Threads Exicution we need to tell the Main THREAD that the both threads join 1st --> thread1.Join( ) and thread2.join()


"""

from time import sleep
from threading import *


class Hello(Thread): # Sub thread class 
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread): # sub thread class
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1=Hello() # Obj of the class 
t2=Hi()

t1.start()  # way to call sub thread class insted of t1.run..!

sleep(0.2) # to AVOID COLLISION(interchange of sequencial printing) b/w two Threads in Between the Thread Execution

t2.start()

t1.join() # wait for t1 to execute by the MAIN THREAD
t2.join()  # wait for t2 to execute by the MAIN THREAD
print("THE END ..!")
