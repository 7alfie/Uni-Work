MAX = 5
circularqueue = [None] * MAX
front = -1
back = -1

data = input("Enter data ")

def circularenqueue(data):
    global front, back
    if (front == 0 and back == MAX - 1) or (back + 1 == front):
        print("Queue overflow")
        return
    if front == -1:
        front = 0
        back = 0
    elif back == MAX - 1 and front != 0:
        back = 0
    else:
        back += 1
    circularqueue[back] = data

def circulardequeue():
    global front, back
    if front == -1:
        print("Queue underflow")
        return
    data = circularqueue[front]
    circularqueue[front] = None
    if front == back:
        front = -1
        back = -1
    elif front == MAX - 1:
        front = 0
    else:
        front += 1
    return data

def peek():
    if front == -1:
        print("Queue underflow")
    else:
        print(f"The first item in your queue is {circularqueue[front]}")
