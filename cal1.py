#small calculator program
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("choose any number to perform respective operation:\n 1.+ add 2.- sub 3.* mul 4./ div ")
choose=int(input())
if choose>4 or choose<1 :
    print("invalid choose")
elif(choose==1):
    print("sum of two number",num1+num2)
elif(choose==2):
    print("subtraction of two number",num1-num2)
elif(choose==3):
    print("multiplication of two number",num1*num2)
else:
    print("division of two number",num1/num2)
