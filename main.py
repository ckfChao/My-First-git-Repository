from op import op

#input
a = int(input("Enter value of a:"))
input_op = input("Enter operater:")
b = int(input("Enter value of b:"))

calc = op(a, b)

if (input_op == "+"):
    print("%d + %d = %d"%(a, b, calc.add()))
elif (input_op == "-"):
    print("%d - %d = %d"%(a, b, calc.sub()))
elif (input_op == "*"):
    print("%d * %d = %d"%(a, b, calc.mult()))