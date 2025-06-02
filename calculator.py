on = True
while on:
    calculation = input("Would you like to perform a calculation? Y/N ")
    if calculation == "Y":
        first_number = int(input("Please type the first number: "))
        second_number = int(input("Please type the second number: "))
        operation = input("What kind of calculation would you like to perform? +,-,*,/ ")
        if operation == "+":
            print("The result is: ", first_number + second_number)
        elif operation == "-":
            print("The result is: ", first_number - second_number)
        elif operation == "*":
            print("The result is: ", first_number * second_number)
        else:
            print("The result is: ", first_number / second_number)     
    else:
         on = False