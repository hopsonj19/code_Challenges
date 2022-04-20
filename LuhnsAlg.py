def Luhn_check(string):
    string = string.replace(" ", "")
    if len(string) != 16:
        return "Invalid number of digits."
    string = string[::-1]
    checkdigit = string[0]
    string = string.replace(checkdigit, '', 1)
    sum = 0
    rank = "Even"
    for i in string:
        num = int(i)
        if rank == "Even":
            num = num * 2
            rank = "Odd"
            numString = str(num)
            if (len(numString)) > 1:
                num1 = numString[0]
                num2 = numString[1]
                num = int(num1) + int(num2)
        else:
            rank = "Even"
        sum = sum + num
    checksum = (10 - (sum % 10) % 10)
    if str(checksum) == checkdigit:
        return "Accept"
    else:
        return "Invalid Credit Card Number"

string = input("Please enter your 16 digit card number: ")
while string != "stop":
    print(Luhn_check(string))
    string = input("Enter another card number or type 'stop' if you are finished: ")
    string = string.lower()
