#project 34:stack and Queue
print("STACK Question (LIFO)")
#MoMo Pushes
print("MoMo Pushes")
stack=["Enter PIN","Select Service","Confirm"]
stack.pop()
print("Remaining stack:",stack)
#UR Pushes
print("UR Pushes") 
stack=["Rev1","Rev2","Rev3"]
stack.pop()
stack.pop()
print("Remaining stack:",stack)
#Challenge
print("Challenge")
stack=["1","2","3","4"]
stack.pop()
stack.pop()
stack.append("5")
print("stack top:",stack[-1])
print("QUEUE Question(FIFO)")
#RRA 5 clients queue
print("RRA 5 Clients queue")
queue=[]
queue.append("C1")
queue.append("C2")
queue.append("C3")
queue.append("C4")
queue.append("C5")
print("Original queue:",queue)
queue.pop(0)
queue.pop(0)
queue.pop(0)
print("Now in front",queue)
print("RRA 5 Clients queue")
queue=[]
queue.append("Bus 1")
queue.append("Bus 2")
queue.append("Bus 3")
queue.append("Bus 4")
queue.append("Bus 5")
queue.append("Bus 6")  
queue.append("Bus 7")
circular=queue;
print("Original queue:",queue)
queue.pop(0)
queue.pop(0)
print("Now the next is",queue[0])
for i in circular:
    print(i)
    
 
