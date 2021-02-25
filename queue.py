from collections import deque
Queue = deque([])
trigger = "a"


def push(items):
    for i in range(5):
        Queue.append(input("Take position in line: "))
    return Queue


def pop():
    if not Queue:
        print("WoHo!! For now  line is empty")
    else:
        Queue.popleft()
    return Queue


while trigger.lower() != "stop":
    print("Want to deposit/withdraw your money:")
    desission = input("Stand in line --> 1 \nLeave the line --> 2\n -----> ")
    if int(desission) == 1:
        print(push(1))
    elif int(desission) == 2:
        print(pop())
    else:
        print("You fucking donkey wrong input.")
    trigger = input("Have any other staff?\nYes --> Y\nNo --> stop --> ")
