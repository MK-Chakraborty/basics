stack = []
trigger = ""


def push(up_limit):
    for i in range(up_limit):
        stack.append(input("URL OF BROWSER: "))
    return stack


def pop():
    if not stack:
        print("U Have No History")
    else:
        stack.pop(0)
    return stack


while trigger.lower() != "stop":
    print("Which operation you want to operate: ")
    operation = input(" 1 --> Push \n 2 --> Pop \n --->")
    if int(operation) == 1:
        print(push(5))
    elif int(operation) == 2:
        print(pop())
    else:
        print("worng input")

    trigger = input(
        "Enter stop to get out of app \nor enter 'a' to run again --> ")
