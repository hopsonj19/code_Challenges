def Luhn_check():
    string = input("Please enter your 16 digit card number: ")
    # string = string.join("")
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
        return "Invalid Credit Number"

contin = "Start"
while contin != "Stop":
    print(Luhn_check())
    contin = input("Type 'Stop' if you are finished: ")