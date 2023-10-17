print("~~~~~~~ Simple Calculator ~~~~~~~~")
print('''
Instruction:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

first_value=int(input("enter your first value: "))
second_value=int(input("enter your second value: "))

opr=input("enter your opr:")

if opr=="+":
       print(first_value + second_value)
elif opr=="-":
       print(first_value - second_value)
elif opr=="*":
       print(first_value * second_value) 
elif opr=="/":
       print(first_value / second_value)
       
else:
    print("invalid input")