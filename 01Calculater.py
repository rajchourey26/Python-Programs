print("Simple calculater of two no.")

a=int(input("Choose what you want from 1/2/3/4 :\n 1.Addition\n 2. Substration\n 3.Multiplication \n 4.Division\n ->"))

if a==1:
    A=int(input("Enter First no: "))
    A1=int(input("Enter Second no: "))
    print("Result:",A+A1)

elif a==2:
    S=int(input("Enter First no: "))
    S1=int(input("Enter Second no: "))
    print("Result:",S-S1)

elif a==3:
    M=int(input("Enter First no: "))
    M1=int(input("Enter Second no: "))
    print("Result:",M*M1)

elif a==4:
    S=int(input("Enter First no: "))
    S1=int(input("Enter Second no: "))
    print("Result:",S/S1)
else:
    print("Invalid no.")    