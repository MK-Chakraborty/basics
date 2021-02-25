def fizz_buzz(input):
    # input = input("enter a number: ")
    if int(input) % 3 == 0 and int(input) % 5 == 0:
        message = "fizz_buzz"
    elif int(input) % 5 == 0:
        # print("buzz")
        message = "buzz"
    elif int(input) % 3 == 0:
        # print("fizz")
        message = "fizz"
    else:
        # print(input)
        message = input
    return message


print(fizz_buzz(50))
