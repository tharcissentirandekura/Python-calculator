def helpMenu():
    print("Choose operation: \n\na/A.Addition \nm/M.Multiplication \ns/s.Substraction \nd/D.Division \ne/D.Exit program\n")
    
def getUserInput(kind):
    if kind == "l":
        flag = True
        operation = ["a","A","m","M","s","S","d","D","e","E"]
        while flag == True:
            operation_selection = input("Enter the operation number:")
            if operation_selection in operation:
                flag = False
                return operation_selection
            else:
                print("Invalid Input.try again")
    
    elif kind == "n":
        x = True
        while x == True:
            try:
                number = float(input("Enter the number:"))
                x = False
                return number
            except:
                print("Invalid Input. Try again!")
                
                
print("Welcome to my calculator and feel free to use it well")

while True:
    helpMenu()
    operation_type = getUserInput("l")
    print("The operation chosen is:",operation_type)

    if operation_type == "a" or operation_type == "A":
        num1 = getUserInput("n")
        num2 = getUserInput("n")
        answer = num1 + num2
        symb = "+"
        
    elif operation_type == "m" or operation_type == "K":
        num1 = getUserInput("n")
        num2 = getUserInput("n")
        answer = num1 * num2
        symb = "x"
        
    
    elif operation_type == "s" or operation_type == "S":
        num1 = getUserInput("n")
        num2 = getUserInput("n")
        answer = num1 - num2
        symb = "-"

    
    elif operation_type == "d" or operation_type == "D":
        symb = "/"
        num1 = getUserInput("n")
        x = True
        while x == True:
            num2 = getUserInput("n")
            if num2 == 0:
                print("Invalid input.Try again because you can not devide by zero")
            else:
                x = False
        answer = num1 / num2
        
    elif operation_type == "e" or operation_type =="E":
        print("Program exit...")
        print("Program finished running!")
        exit()
print(f"The answer of: {num1} {symb} {num2} is : {answer}\n")
    
