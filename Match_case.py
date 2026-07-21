a=int(input("enter the lucky number between 1 to 10:"))
if a >10:
    print("invalid no.")
match a:
    case 1:
        print("You won a charger ")
    case 3:
        print("You won a book  ")
    case 6:
        print("You won a phone")
    case _:#    case _ if (a<10):

        print ("better luck next time")
