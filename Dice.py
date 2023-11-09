import random

while True:

    boolinput=input("Do you want to trow a dice? Y/N: ")

    if boolinput == "Y":
        num = random.randint(1,6)

        if num == 1:
            print("○○○")
            print("○●○")
            print("○○○")
        elif num == 2:
            print("●○○")
            print("○○○")
            print("○○●")
        elif num == 3:
            print("●○○")
            print("○●○")
            print("○○●")
        elif num == 4:
            print("●○●")
            print("○○○")
            print("●○●")
        elif num == 5:
            print("●○●")
            print("○●○")
            print("●○●")
        elif num == 6:
            print("●●●")
            print("●●●")
            print("○○○")
        
    else:
        break