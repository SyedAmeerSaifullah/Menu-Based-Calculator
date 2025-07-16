def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        print("Operatin can not take place denominator is 0.")
def calulator():
    
    print("1. Add two numbers")       
    print("2. Subtract two numbers")
    print("3. Muliply two numbers")
    print("4. Divide two number")
    print("5. Exit the program")
    choice=int(input("Enter your choice: "))
    if choice>=1 and choice<=4:
          
        a=int(input("Enter 1 st number:"))
        b=int(input("Enter 2 nd number:"))
    while choice<1 or choice>5:
        print("Invalid value enterd please enter the value according to the menu above:")
        print("1. Add two numbers")       
        print("2. Subtract two numbers")
        print("3. Muliply two numbers")
        print("4. Divide two number")
        print("5. Exit the program")
        choice=int(input()) 
        return True;    
    if choice==1:
            print("Sum is ",add(a,b))
    elif choice==2:
            print("Difference is ",subtract(a,b))
    elif choice==3:
            print("Product is ",multiply(a,b))
    elif choice==4:    
            print("After dividing answer",divide(a,b))
    elif choice==5:
            print("Program Exiting....")
            return False        
    if (choice>=1 and choice<=4):
            return True
print("Welcome to the calculator!")
while True:#Runs calculator infinite times
    if not calulator():
        break



