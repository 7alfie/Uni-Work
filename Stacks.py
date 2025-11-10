MAX = 5
stack = [None] * MAX
pointer = -1

def push(item):
    global pointer
    if pointer == MAX - 1:
        print("Stack overflow")
    else:
        pointer += 1
        stack[pointer] = item
        print("Item has been added to stack")


item = input("Enter the item to be pushed ")
push(item)
print(stack)






# Removing something from the stack

def pop():
    global pointer
    if pointer == -1:
        print("Stack underflow")
    else:
        item = stack[pointer]
        stack[pointer] = None
        pointer -= 1
        print(f"Item has been removed from the stack")
pop()
print(stack)

def peek():
    if is_empty():
        print("Stack is empty")
    else:
        print(f"{stack[pointer]} is at the top of the stack")
peek()
print(stack)