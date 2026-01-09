#calculator program
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
con="y"
while con=="y":
    choose=int(input("choose any number to perform respective operation:\n 1.+ add 2.- sub 3.* mul 4./ div \n"))
    if choose>4 or choose<1 :
        print("invalid choose")
    elif(choose==1):
        print("sum of two number",num1+num2)
    elif(choose==2):
        print("subtraction of two number",num1-num2)
    elif(choose==3):
        print("multiplication of two number",num1*num2)
    else:
        if num2!=0:
            print("division of two number",num1/num2)
        else:
            print("invalid denominator")
    con=input("continue?:(y/n)\n").lower()