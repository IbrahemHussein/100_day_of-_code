from art import logo


# Calculator

#add
def add(n1,n2):
    return n1 + n2

#subtrack
def subtrack(n1,n2):
    return n1 - n2

#multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
 
def divde(n1,n2):
    return n1 /n2  
operation={'+':add,
           '-':subtrack,
           '*':multiply,
           '/':divde}
def calculator():
    print(logo)
    num1=float(input('Enter the first number? : '))

    for key in operation:
        print(key)
    should_continue=True
    while should_continue:
        operation_symbol=input('pick an operation :  ')
        if operation_symbol not in operation.keys():
            print('you enter valid symbol')
            operation_symbol=input('pick an operation :  ')
        num2=float(input('Enter the next  number? : '))
        calculation_function=operation[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        chack=input(f"Type 'y' to coninue calculating with {answer} , or type 'n' to exit : ,or type 's' to start new calcultor : ")
        if chack=='y':
            num1=answer
        elif chack =='n':
            should_continue=False
        elif chack== 's':
            should_continue=False
            calculator()
        else:
            print('you enter valid char ')
            chack=input(f"Type 'y' to coninue calculating with {answer} , or type 'n' to exit : ,or type 's' to start new calcultor : ")
            

calculator()