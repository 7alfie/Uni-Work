MAX = 5
queue = [None] * MAX
front = -1
back = -1
data = str(input("Enter your data"))

def enqueue(data):
    global back
    if back == MAX -1:
        print("Queue overflow")
    else:
        queue[back] = data
enqueue(data)
print(queue)