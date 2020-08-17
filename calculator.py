import os; os.system("cls")
num1 = int(float(input(" ENTER FIRST NUMBER : ")))
num2 = int(float(input(" ENTER SECOND NUMBER : ")))
ans_inp = input(" ENTER YOUR OPERATION : \n"
                        " A - ADDITION\n"
                        " S - SUBTRACTION\n"
                        " M - MULTIPLICATION\n"
                        " D - DIVISION\n : ")
if (ans_inp == 'a'):
    print(" YOUR ANSWER IS : " ,num1+num2)
elif (ans_inp == 's'):
    print(" YOUR ANSWER IS : " ,num1-num2)
elif (ans_inp == 'm'):
    print(" YOUR ANSWER IS : " ,num1*num2)
elif (ans_inp == 'd'):
    print(" YOUR ANSWER IS : " ,num1/num2)
elif (ans_inp != 'a' or ans_inp != 's' or ans_inp != 'm' or ans_inp != 'd'):
    print("pls choose from a s m d")






