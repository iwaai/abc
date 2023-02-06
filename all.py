
################## FORK OR ZOMBIE , ORPHAN BAZZI ###################################################################################
####################################################################################################################################



#=========================  simple child process ===============================================

import os
retval = os.fork()
if retval == 0:
    print("child process is running")
    print("child prcoess ended"+ os.pid())
else:
    os.wait()
    print("child process ended")
    print("parent process now running")


#================================= zombie process 10 second wait ===============================================

# Using either a Linux system, write a program that forks a child process that ultimately becomes a zombie process. 
# This zombie process must remain in the system for at least 10 seconds.

import os
import time

pid = os.fork()

if pid == 0:
    # This is the child process
    print("Child process, pid =", os.getpid())
    # Exit immediately, becoming a zombie process
    os._exit(0)
else:
    # This is the parent process
    print("Parent process, pid =", os.getpid())
    # Wait for 10 seconds
    time.sleep(10)
    # Check the status of the child process
    pid, status = os.waitpid(pid, os.WSTOPSIG | os.WEXITED)
    print("Child process has finished with status:", status)



#================================== child k 2 child ===============================================

#  Write a program that creates a child process which further creates its two child processes. Store the process id of 
# each process in an array called Created Processes. Also display the process id of the terminated child to 
# understand the hierarchy of termination of each child process.


import os,time

created_process = []
ret = os.fork()

if ret == 0:
	print("Super master child process")
	created_process.append(os.getpid())
	
	c1 = os.fork()
	
	if c1 == 0:
		print("super wale ka bacha number 1")
		created_process.append(os.getpid())
		
	else:
		created_process.append(os.getpid())
		c2 = os.fork()
		created_process.append(os.getpid())
		
		if c2 == 0:
			print("super wale ka bacha number 2")
			created_process.append(os.getpid())
		else:
			created_process.append(os.getpid())
			os.wait()
			os.wait()
else:
	created_process.append(os.getpid())
	os.wait()
	
	
print(created_process)


#============ array create in parent , sort in child =============================================

# . Write a program in which a parent process will initialize an array, and child process will sort this array. Use wait() 
# and sleep() methods to achieve the synchronization such that parent process should run first.


import os,time

created_process = []
ret = os.fork()

if ret == 0:
	print("Super master child process")
	created_process.append(os.getpid())
	
	c1 = os.fork()
	
	if c1 == 0:
		print("super wale ka bacha number 1")
		created_process.append(os.getpid())
		
	else:
		created_process.append(os.getpid())
		c2 = os.fork()
		created_process.append(os.getpid())
		
		if c2 == 0:
			print("super wale ka bacha number 2")
			created_process.append(os.getpid())
		else:
			created_process.append(os.getpid())
			os.wait()
			os.wait()
else:
	created_process.append(os.getpid())
	os.wait()
	
	
print(created_process)



################## THREADING ###################################################################################
##############################################################################################################

#============  2 thread aik sey name aik sey roll no===============================

# Modify Example 1 to display strings via two independent threads: 
# thread1: “Hello ! StudentName___”, thread 2: “Student roll no is :__________”

import threading
def name_fun(name):
    print(f"hello studentName{name}")
def roll_fun(roll):
    print(f"student roll no is",roll)


t1 = threading.Thread(target=name_fun,args=("name",))
t2 = threading.Thread(target=roll_fun,args=(1,));
t1.start()
t2.start()
t2.join()
t2.join()


#============  no of threads by user ==============

# Create threads message as many times as user wants to create threads by using array of threads and loop. 
# Threads should display message that is passed through argument.

def create_tr(n):
    print(f"hello \n thread number : {n}")


n = int(input("enter no of thread :  "))
thread_li = []
for i in range(n):
    t1 =threading.Thread(target=create_tr,args = (i,))
    t1.start()
    thread_li.append(t1)

for i in thread_li:
    i.join()





################## SEMAPHORE ##################################################################################
##############################################################################################################

#============ PRODUCER CONSUMER =================================

# Write a python program that demonstrates the synchronization of Consumer producer Bounded Buffer 
# Problem using semaphores

import threading 
import random 
import time 

buf = [] 
empty = threading.Semaphore(5) 
full = threading.Semaphore(0) 
mutex = threading.Lock() 


def producer(): 
    nums = range(5) 
    global buf 
    num = random.choice(nums) 
    empty.acquire() # EMPTY ME -1
    mutex.acquire() # LOCK KARDIA SHARED RESOURCE KO 
    #TAKE KOI OR ACCESS NA KAR SAKE
    buf.append(num) 
    print("Produced", num, buf) 
    mutex.release() # added 
    full.release()  # FUL ME +1


def consumer(): 
    global buf 
    full.acquire() 
    mutex.acquire() # added 
    num = buf.pop(0) 
    print("Consumed", num, buf) 
    mutex.release() # added 
    empty.release() 



consumerThread1 = threading.Thread(target=consumer)
producerThread1 = threading.Thread(target=producer) 
consumerThread2 = threading.Thread(target=consumer)
producerThread2 = threading.Thread(target=producer) 
producerThread3 = threading.Thread(target=producer) 
producerThread4 = threading.Thread(target=producer) 
producerThread5 = threading.Thread(target=producer) 
producerThread6 = threading.Thread(target=producer)



consumerThread1.start() 
consumerThread2.start() 
producerThread1.start() 
producerThread2.start()
producerThread3.start()
producerThread4.start()
producerThread5.start()
producerThread6.start()


consumerThread1.join() 
consumerThread2.join() 
producerThread1.join() 
producerThread2.join()
producerThread3.join()
producerThread4.join()
producerThread5.join()
producerThread6.join()


#============ READ WRITE BINARY SEMAPHORE============================

# Write a python program that demonstrates the synchronization of Readers and Writer Problem using 
# semaphores.

import threading
import time

readers_count = 0 # kitne reader hein db me


db = threading.Semaphore(1)
mutex = threading.Lock() 

def reader(id):
    global readers_count
    mutex.acquire()
    readers_count += 1
    if readers_count == 1:
        db.acquire()
    mutex.release()

    # Reading is taking place
    print("Reader %d is reading the database." % id)
    time.sleep(1)

    mutex.acquire()
    readers_count -= 1
    if readers_count == 0:
        db.release()
    mutex.release()

def writer(id):
    db.acquire()
    # Writing is taking place
    print("Writer %d is writing to the database." % id)
    time.sleep(1)
    db.release()

reader_threads = [threading.Thread(target=reader, args=(i,)) for i in range(5)]
writer_threads = [threading.Thread(target=writer, args=(i,)) for i in range(2)]
for t in writer_threads + reader_threads :
    t.start()

for t in reader_threads + writer_threads:
    t.join()






###################### INTERPROCESS COMMUNCITON PIPE  ##################################################################
##############################################################################################################

import os

r,w = os.pipe()
ret = os.fork()

if ret > 0:
	os.close(r)
	
	print("parent")
	text = "hello child ".encode()
	
	os.write(w,text)
	os.close(w)	
	
else:
	os.close(w)
	print("child")
	cr = os.fdopen(r)
	
	print(cr.read())


# ================ LAB 11 PARENT CHILD KI COMMUNICATION THROUGH MULTIPROCESSING =====================

try:
	from multiprocessing import Process,Pipe
except:
	os.system("pip install multiprocessing")


def f(child_conn):
	print(child_conn.recv())
	child_conn.send("hello parent")
	child_conn.close()
	
p_conn,c_conn = Pipe()
p_conn.send("hello child")

p1 = Process(target = f,args= (c_conn,))

p1.start()
p1.join()

print(p_conn.recv())
p_conn.close()



#======================== LAB 11 PARENT LIST BANA RAH CHILD SORT KARRAH ============================

from multiprocessing import Process, Array, Value,Pipe

def child_process(arr,n,c):
	arr = sorted(arr[:],reverse = True)
	print(arr[:])
	for i in range(len(arr)):
		arr[i] = -arr[i]
	n = n.value + 1.1
	
	print("abba ne ye bola ",c.recv())
	c.send((arr,n))
	c.close()
	
p_conn,c_conn = Pipe()
p_conn.send("chal shaba reverse sort kar ke de or value me +1")

arr = Array('i',range(10))
print(arr[:])
n = Value('d',2.0)
p1 = Process(target = child_process, args = (arr,n,c_conn,))

p1.start()
p1.join()
print(p_conn.recv())
p_conn.close()



#======================== Lab 11 os.pipe se do pipe bana raahe=========================


import os

r,w = os.pipe()
r2,w2 = os.pipe()
pid = os.fork()

if pid > 0:
	os.close(w2) #un-necessary chezon ko pehle band kro
	os.close(r)
	print('Parent process is writing')	
	text = 'Hello child proces'.encode()
	os.write(w,text)
	os.close(w)
	pr = os.fdopen(r2)
	print('Child has sent ',pr.read()) 
	
else:
	os.close(w) #un-necessary chezon ko pehle band kro
	os.close(r2)
	print('\nChild process ')
	cr = os.fdopen(r)
	print('Read', cr.read())
	print('\nChild process is sending regards')
	text = 'Thankyou'.encode()
	os.write(w2,text)
	os.close(w2)


##LAB 11 5 FUNCTIONS ME SHARED VALUE JA RAHI OR +1 HO RAH

from multiprocessing import Process,Value

def t1(value):
	
	value.value +=1
def t2(value):
	
	value.value +=1
def t3(value):
	
	value.value +=1
def t4(value):
	
	value.value +=1
def t5(value):
	
	value.value +=1
v = Value('i',0)
print(v.value)
p1 = Process(target = t1,args = (v,))
p2 = Process(target = t2,args = (v,))
p3 = Process(target = t3,args = (v,))
p4 = Process(target = t4,args = (v,))
p5 = Process(target = t5,args = (v,))


p1.start()
p2.start()
p3.start()
p4.start()
p5.start()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()

print(v.value)


#========================LAB 12==================== 2 PROCESSES BAN RAHE DONO ME ADHI ADHI LIST JA  RAHI OR SQUARE HO RAH

from multiprocessing import Process,Array
import random
def square(arr,i,j):
	print(arr[i:j])
	for i in range(i,j):
		arr[i] = arr[i] **2

arr = Array('i',[0,1,2,3,4,5,6,7,8,9]) 
print(arr[:])
p1 = Process(target = square,args = (arr,0,len(arr[:])//2,))
p2 = Process(target = square,args = (arr,(len(arr[:])//2),len(arr[:]),))

p1.start()
p2.start()
p1.join()
p2.join()
print(arr[:])



# =========COMMAND LINE SE INPUT LE RAHE

import sys
from multiprocessing import Process,Pipe

def parent(conn,name):
	print("parent")
	conn.send(name)
	conn.close()
def child(conn):
	print("child")
	print(conn.recv())
	conn.close()
	
name= sys.argv[1]
p_conn,c_conn = Pipe()
p = Process(target = parent, args = (p_conn,name,))
c = Process(target = child, args = (c_conn,))


p.start()
c.start()

p.join()
c.join()



###################### MULTIPROCESS INTERPROCESS SHARED MEMORY ##################################################################
##############################################################################################################




# LAB 12 =================================== 2 PROCESSES BAN RAHE DONO ME ADHI ADHI LIST JA  RAHI OR SQUARE HO RAH =======================

from multiprocessing import Process,Array
import random
def square(arr,i,j):
	print(arr[i:j])
	for i in range(i,j):
		arr[i] = arr[i] **2

arr = Array('i',[0,1,2,3,4,5,6,7,8,9]) 
print(arr[:])
p1 = Process(target = square,args = (arr,0,len(arr[:])//2,))
p2 = Process(target = square,args = (arr,(len(arr[:])//2),len(arr[:]),))

p1.start()
p2.start()
p1.join()
p2.join()
print(arr[:])



# ============================ COMMAND LINE SE INPUT LE RAHE ======================================================


import sys
from multiprocessing import Process,Pipe

def parent(conn,name):
	print("parent")
	conn.send(name)
	conn.close()
def child(conn):
	print("child")
	print(conn.recv())
	conn.close()
	
name= sys.argv[1]
p_conn,c_conn = Pipe()
p = Process(target = parent, args = (p_conn,name,))
c = Process(target = child, args = (c_conn,))


p.start()
c.start()

p.join()
c.join()


###################### SCHEDULING  ALGORITHM  ##################################################################
##############################################################################################################

import os
try:
    from rich.console import Console
    from rich.table import Table
    import pyfiglet as pyg
    from operator import attrgetter
except ImportError:
    os.system("pip install rich")
    os.system("pip install pyfiglet")
    os.system("pip install operator")
    from rich.console import Console
    from rich.table import Table
    import pyfiglet as pyg  

os.system("cls") 

# res= pyg.figlet_format("SJF Algorithm", font = "slant")   
# print(res)  

class Process:
    def __init__(self, pid=0, arrival_time=0, burst_time=0,priority=0):
        self.pid:int = pid
        self.arrival_time:int = arrival_time
        self.burst_time:int = burst_time
        self.waiting_time:int = 0
        self.turnaround_time:int = 0
        self.completion_time:int = 0
        self.priority:int = priority
           
class Algorithems:
    
    def __init__(self):
        
        self.console = Console()

        self.table = Table(show_header=True, header_style="bold magenta")
        self.table.add_column("Process")
        self.table.add_column("Arrival Time")
        self.table.add_column("Burst Time")
        self.table.add_column("Completion Time")
        self.table.add_column("Turn Around Time")
        self.table.add_column("Waiting Time")
        self.table.add_column("Priority")
        
        
    def priority(self):
        processes = []
        n = int(input("Enter the number of processes: "))
        for i in range(0,n):
            burst_time = int(input("Enter the burst time: "))
            at = int(input("Enter the Arrival time time: "))
            priority = int(input("Enter the Priority: "))
            processes.append(Process(i+1,arrival_time=at, burst_time=burst_time,priority = priority))
            
        processes.sort(key=attrgetter("priority"))
        
        for i in range(len(processes)):
            try:
                #processes[i].completion_time = processes[i-1].completion_time + processes[i].burst_time
                if processes[i].arrival_time <= processes[i-1].completion_time:
                    processes[i].completion_time = processes[i-1].completion_time + processes[i].burst_time
                else:
                    
                    processes[i].completion_time = processes[i].arrival_time + processes[i].burst_time
                processes[i].turnaround_time = processes[i].completion_time - processes[i].arrival_time
                processes[i].waiting_time = processes[i].turnaround_time - processes[i].burst_time
            except:
                pass
        self.draw(processes)
        
        
    def SJF_beta(self):
        processes = []
        n = int(input("Enter the number of processes: "))
        for i in range(0,n):
            burst_time = int(input("Enter the burst time: "))
            at = int(input("Enter the Arrival time time: "))
            processes.append(Process(i+1,arrival_time=at, burst_time=burst_time))
            
        processes.sort(key=attrgetter("arrival_time"))
        processes2 = processes.copy()
        timer = processes[0].arrival_time
        completed = []
        while True:
            if len(processes2) == 0:
                break
            arrived = []
            for i in processes2:
                if i.arrival_time <= timer:
                    arrived.append(i)
                    
            minimum_burst = min(arrived, key=attrgetter("burst_time"))
            minimum_burst.completion_time = minimum_burst.burst_time + timer
            timer = minimum_burst.completion_time
            minimum_burst.turnaround_time = minimum_burst.completion_time - minimum_burst.arrival_time
            minimum_burst.waiting_time = minimum_burst.turnaround_time - minimum_burst.burst_time
            completed.append(minimum_burst)
            processes2.remove(minimum_burst)
            
            
        self.draw(completed)
        
 
        
        
    

    def priority_pre_beta(self):
            processes = []
            processes2 = []
            n = int(input("Enter the number of processes: "))
            for i in range(0,n):
                burst_time = int(input("Enter the burst time: "))
                at = int(input("Enter the Arrival time time: "))
                priority = int(input("Enter the Priority: "))
                processes.append(Process(i+1,arrival_time=at, burst_time=burst_time,priority = priority))
                processes2.append(Process(i+1,arrival_time=at, burst_time=burst_time,priority = priority))
                
            processes.sort(key=attrgetter("arrival_time"))
            processes2.sort(key=attrgetter("arrival_time"))
        

            timer = processes[0].arrival_time
            completed = []
            while True:
                if len(processes2) == 0:
                    break
                arrived = []
                for i in processes2:
                    if i.arrival_time <= timer:
                        arrived.append(i)
                minimum_prority = min(arrived,key=attrgetter("priority"))
                minimum_prority.burst_time = minimum_prority.burst_time - 1
                minimum_prority.completion_time = timer + 1
                if minimum_prority.burst_time <= 0:
                    arrived.remove(minimum_prority)
                    completed.append(minimum_prority)
                    processes2.remove(minimum_prority)   
                timer +=1
            completed.sort(key=attrgetter("arrival_time"))
            for z,item in enumerate(completed):
                item.burst_time = processes[z].burst_time
                item.turnaround_time = item.completion_time - item.arrival_time
                item.waiting_time =  abs(item.turnaround_time - item.burst_time)
            self.draw(completed)
    def SJF_pre_beta(self):
            processes = []
            processes2 = []
            n = int(input("Enter the number of processes: "))
            for i in range(0,n):
                burst_time = int(input("Enter the burst time: "))
                at = int(input("Enter the Arrival time time: "))
                processes.append(Process(i+1,arrival_time=at, burst_time=burst_time))
                processes2.append(Process(i+1,arrival_time=at, burst_time=burst_time))
                
            processes.sort(key=attrgetter("arrival_time"))
            
            processes2.sort(key=attrgetter("arrival_time"))

            timer = processes[0].arrival_time
            completed = []
            while True:
                if len(processes2) == 0:
                    break
                arrived = []
                for i in processes2:
                    if i.arrival_time <= timer:
                        arrived.append(i)
                minimum_burst = min(arrived,key=attrgetter("burst_time"))
                minimum_burst.burst_time = minimum_burst.burst_time - 1
                minimum_burst.completion_time = timer + 1
                if minimum_burst.burst_time <= 0:
                    arrived.remove(minimum_burst)
                    completed.append(minimum_burst)
                    processes2.remove(minimum_burst)   
                timer +=1
            completed.sort(key=attrgetter("arrival_time"))
            for z,item in enumerate(completed):
                item.burst_time = processes[z].burst_time
                item.turnaround_time = item.completion_time - item.arrival_time
                item.waiting_time =  abs(item.turnaround_time - item.burst_time)
            self.draw(completed)
    
        
    def draw(self,processes):
        
        for process in processes:
            self.table.add_row(
                f"P{process.pid}",
                f"{process.arrival_time}",
                f"{process.burst_time}",
                f"{process.completion_time}",
                f"{process.turnaround_time}",
                f"{process.waiting_time}",
                f"{process.priority}"
            )

        self.console.print(self.table)
        sum_of_waiting_time = sum([process.waiting_time for process in processes])
        sum_of_turnaround_time = sum([process.turnaround_time for process in processes])
        
        print(f"Average waiting time: {sum_of_waiting_time/len(processes)}")
        print(f"Average turnaround time: {sum_of_turnaround_time/len(processes)}")
        
        
   
            
    def FCFS(self):
        processes = []
        n = int(input("Enter the number of processes: "))
        for i in range(0,n):
            burst_time = int(input("Enter the burst time: "))
            at = int(input("Enter the Arrival time time: "))
           
            processes.append(Process(i+1,arrival_time=at, burst_time=burst_time))

        processes.sort(key=attrgetter("arrival_time"))
        
        time = 0
        for i in processes:
            i.completion_time = (i.arrival_time + i.burst_time) + time
            i.turnaround_time = i.completion_time - i.arrival_time
            i.waiting_time = i.turnaround_time - i.burst_time
            time = i.completion_time
        
        self.draw(processes)    
        
    def RR_beta(self):
        
        ready_stack = []
        runing_stack = []
        processes = []
        processes3 = []
        processes2 = []
        
        n = int(input("Enter the number of processes: "))
        for i in range(0,n):
            burst_time = int(input("Enter the burst time: "))
            at = int(input("Enter the Arrival time time: "))
           
            processes.append(Process(i+1,arrival_time=at, burst_time=burst_time))
            processes2.append(Process(i+1,arrival_time=at, burst_time=burst_time))
        TQ = int(input("Enter the Time Quantum: "))
        processes.sort(key=attrgetter("arrival_time"))
        processes2.sort(key=attrgetter("arrival_time"))
        


        time_spent = processes[0].arrival_time
        index = -1
        while True:
            if len(processes2) == 0:
                break
            for i in processes2:
                if i.arrival_time <= time_spent and i not in ready_stack and i not in processes3:
                    
                    ready_stack.append(i)
                    # print("-----------------------Adding in ready stack--------------------------------")
                    # print(f"READY STACK {[i.pid for i in ready_stack]}")
                    # print(f"Process3 STACK {[i.pid for i in processes3]}")
            

            for r in runing_stack:
                ready_stack.append(r)
            
            # if len(ready_stack) >1:
            #      if ready_stack[0] == ready_stack[-1]:
            #         ready_stack.pop(0)
           

            ready_stack = ready_stack[index+1:] 
            # print(f"Ready stack after slicing {[c.pid for c in ready_stack]}")     
                
            # print("-----------------------Before--------------------------------")
            # print(f"READY STACK {[i.pid for i in ready_stack]}")
            # print(f"RUNNING STACK {[i.pid for i in runing_stack]}")
            # print(f"PROCESS2 STACK {[i.pid for i in processes2]}")
            runing_stack = []
            
            for index,i in enumerate(ready_stack):
                if len(processes2) == 0:
                    break

                
                print(f"\nNOW RUNNING {i.pid}\n")
                
                if True:

                    if i.burst_time > TQ:
                        i.burst_time -= TQ
                        runing_stack.append(i)
                        time_spent += TQ
                        
                        # try:
                        #     a = ready_stack.pop(0)
                        #     print(f"Popping the first element from ready stack {a.pid}")
                        #     print(f"Ready stack after popping {[c.pid for c in ready_stack]}")
                        # except:
                        #     pass

                        
                    else:
                        runing_stack.append(i)
                        
                        time_spent += i.burst_time
                        i.completion_time = time_spent
                        #print(f"Removing process {i.pid} having completion time {i.completion_time}")
                        processes3.append(i)
                        processes2.remove(i)
                        
                        runing_stack = [value for value in runing_stack if value != i]
                        # ready_stack = [value for value in ready_stack if value != i]
                        
                        
                        # print("-----------------------After--------------------------------")
                        # print(f"READY STACK {[i.pid for i in ready_stack]}")
                        # print(f"RUNNING STACK {[i.pid for i in runing_stack]}")
                        # print(f"PROCESS2 STACK {[i.pid for i in processes2]}")
             
                        
        for i in processes3:
            for j in processes:
                if j.pid == i.pid:
                    i.burst_time = j.burst_time
                    # print(f"P {[(c.pid,c.burst_time) for c in processes]}")
                    # print(f"P3 {[(c.pid,c.burst_time) for c in processes3]}")
                    break
            i.turnaround_time = i.completion_time - i.arrival_time
            i.waiting_time = abs(i.turnaround_time - i.burst_time)
        self.draw(processes3)
                
                      
   
    
if __name__ == "__main__":
    obj = Algorithems()
    #obj.priority_pre_beta() #https://www.geeksforgeeks.org/preemptive-priority-cpu-scheduling-algortithm/
    #obj.FCFS()
    #obj.SJF_pre_beta() #https://prepinsta.com/operating-systems/shortest-job-first-scheduling-preemptive-example/#:~:text=SJF%20Preemptive%20Example&text=It's%20the%20only%20process%20so,and%20P2%20process%20starts%20executing.
                        #https://www.tutorialandexample.com/shortest-job-first-sjf-scheduling
    #obj.SJF_beta()
    #obj.RR_beta() #https://www.gatevidyalay.com/round-robin-round-robin-scheduling-examples/
    obj.priority_beta() #https://www.javatpoint.com/os-non-preemptive-priority-scheduling#:~:text=In%20the%20Non%20Preemptive%20Priority,the%20priority%20of%20the%20process.
   
    
    

###################### BANKER ALGORITHM  ##################################################################
##############################################################################################################

def is_safe_state(processes, avail, need, allot):
    """
    Check if the system is in a safe state
    :param processes: Number of processes
    :param avail: Available resources
    :param need: Need matrix for each process
    :param allot: Allocation matrix for each process
    :return: True if safe state, False otherwise
    """
    # Mark all processes as infeasible
    finish = [False] * processes

    # To store safe sequence
    safe_seq = [0] * processes

    # Make a copy of available resources
    work = [0] * len(avail)
    for i in range(len(avail)):
        work[i] = avail[i]

    # While all processes are not finished or system is not in safe state
    count = 0
    while count < processes:
        # Find a process which is not finish and whose needs can be satisfied with current work[]
        found = False
        for p in range(processes):
            if finish[p] == False and need[p][:len(work)] <= work:
                # Add the allocated resources of current P to the available/work resources i.e. free the resources
                for j in range(len(work)):
                    work[j] += allot[p][j]

                # Add this process to safe sequence.
                safe_seq[count] = p
                count += 1

                # Mark this p as finished
                finish[p] = True
                found = True

        # If we could not find a next process in safe sequence.
        if found == False:
            print("System is not in safe state")
            return False

    # If system is in safe state then safe sequence will be as below
    print("System is in safe state.\nSafe sequence is: ", end=" ")
    print(*safe_seq)

    return True

# Driver code
if __name__ == '__main__':
    processes = 5
    avail = [3, 3, 2]
    max_res = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    allot = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

    # Calculate the need matrix
    need = []
    for i in range(processes):
        n = [max_res[i][j] - allot[i][j] for j in range(len(avail))]
        need.append(n)

    # Check system is in safe state or not
    is_safe_state(processes, avail, need, allot)



################################n lab quiz wala question

#!/bin/bash

function count_lines_type() {
  file=$1
  if [ ! -f $file ]; then
    echo "Error: File $file does not exist."
    return 1
  fi
  lines=$(wc -l < $file)
  type=$(file $file | awk '{print $2}')
  echo "The number of lines in $file is $lines and its type is $type."
}

function edit_file() {
  file=$1
  if [ ! -f $file ]; then
    echo "Error: File $file does not exist."
    return 1
  fi
  if [ ! -w $file ]; then
    echo "The file is not editable. Changing its permissions..."
    chmod +w $file
  fi
  nano $file
}

function copy_folder() {
  folder=$1
  backup_folder="backup/$folder"
  if [ ! -d $folder ]; then
    echo "Error: Folder $folder does not exist."
    return 1
  fi
  if [ ! -d "backup" ]; then
    echo "Creating backup folder..."
    mkdir backup
  fi
  echo "Copying $folder to $backup_folder..."
  cp -r $folder $backup_folder
}

function remove_file() {
  file=$1
  if [ ! -f $file ]; then
    echo "Error: File $file does not exist."
    return 1
  fi
  lines=$(wc -l < $file)
  if [ $lines -gt 1000 ]; then
    echo "The number of lines in $file is greater than 1000. Removing file..."
    rm $file
  fi
}

if [ $# -lt 2 ]; then
  echo "Usage: $0 <option> <file/folder>"
  echo "Options:"
  echo "  a - Count the number of lines and type of file"
  echo "  b - Edit file"
  echo "  c - Copy folder to backup folder"
  echo "  d - Remove file if number of lines is greater than 1000"
  exit 1
fi

option=$1
file_or_folder=$2

case $option in
  a) count_lines_type $file_or_folder;;
  b) edit_file $file_or_folder;;
  c) copy_folder $file_or_folder;;
  d) remove_file $file_or_folder;;
  *) echo "Error: Invalid option.";;
esac











################################################################################################################bash/shell

###############roll number ka average (less than or equal to)
#!/bin/bash

# Prompt the user for the roll number
read -p "Enter your roll number: " roll_number

# Initialize the sum and count of even numbers
sum=0
count=0

# Loop through all numbers less than or equal to the roll number
for i in $(seq 0 $roll_number); do
  # Check if the number is even
  if [ $(($i % 2)) -eq 0 ]; then
    # Add the even number to the sum
    sum=$((sum + i))
    # Increment the count of even numbers
    count=$((count + 1))
  fi
done

# Calculate the average of all even numbers
average=$(echo "scale=2; $sum / $count" | bc)

# Print the result
echo "The average of all even numbers less than or equal to $roll_number is $average"


####################### parameter number with while
#!/bin/bash

# Initialize the minimum and maximum values
min=1
max=$#

# Loop through all the parameters
while [ $min -le $max ]; do
  # Display the parameter number and value
  echo "Parameter $min = ${!min}"
  # Increment the minimum value
  min=$((min + 1))
done



#######################with unitl
#!/bin/bash

# Initialize the minimum and maximum values
min=1
max=$#

# Loop through all the parameters
until [ $min -gt $max ]; do
  # Display the parameter number and value
  echo "Parameter $min = ${!min}"
  # Increment the minimum value
  min=$((min + 1))
done


#########################quiz (3 quiz thy deklena yehi ha ya koi or)
#!/bin/bash

function count_lines_type() {
  file=$1
  if [ ! -f $file ]; then
    echo "Error: File $file does not exist."
    return 1
  fi
  lines=$(wc -l < $file)
  type=$(file $file | awk '{print $2}')
  echo "The number of lines in $file is $lines and its type is $type."
}

function edit_file() {
  file=$1
  if [ ! -f $file ]; then
    echo "Error: File $file does not exist."
    return 1
  fi
  if [ ! -w $file ]; then
    echo "The file is not editable. Changing its permissions..."
    chmod +w $file
  fi
  nano $file
}

function copy_folder() {
  folder=$1
  backup_folder="backup/$folder"
  if [ ! -d $folder ]; then
    echo "Error: Folder $folder does not exist."
    return 1
  fi
  if [ ! -d "backup" ]; then
    echo "Creating backup folder..."
    mkdir backup
  fi
  echo "Copying $folder to $backup_folder..."
  cp -r $folder $backup_folder
}

function remove_file() {
  file=$1
  if [ ! -f $file ]; then
    echo "Error: File $file does not exist."
    return 1
  fi
  lines=$(wc -l < $file)
  if [ $lines -gt 1000 ]; then
    echo "The number of lines in $file is greater than 1000. Removing file..."
    rm $file
  fi
}

if [ $# -lt 2 ]; then
  echo "Usage: $0 <option> <file/folder>"
  echo "Options:"
  echo "  a - Count the number of lines and type of file"
  echo "  b - Edit file"
  echo "  c - Copy folder to backup folder"
  echo "  d - Remove file if number of lines is greater than 1000"
  exit 1
fi

option=$1
file_or_folder=$2

case $option in
  a) count_lines_type $file_or_folder;;
  b) edit_file $file_or_folder;;
  c) copy_folder $file_or_folder;;
  d) remove_file $file_or_folder;;
  *) echo "Error: Invalid option.";;
esac
















    #sahi wala sort multiprocessing
from multiprocessing import Pipe,Array,Process, Value
    
def child(arr,c_conn,v):
    print(arr[:])
    print(v.value)
    
    v = value+2.1
    arr = sorted(arr[:])
    print(arr,v)
    c_conn.send("done")
    c_conn.close()

    arr = Array('i',[5,2,8])
    val = Value('d',1.0)
    p_conn,c_conn = Pipe()
    p = Process(target =child, args =(arr,c_conn,val,))
    p.start()
    join
    print(P_conn.recv())
    p_conn.close()
