import random
conf='y'

class inp(Exception):
    pass

while conf=='y':
    num=random.randint(1,20)
    flag, correct=1, 0
    while (flag<=5) and (correct==0):   
        check, flag1=0, 1
        while True and flag1<=5:    
            guess=input("Guess number between 1 and 20: ")
            try:
                flag1+=1
                float(guess)
                if(float(guess)>0 and float(guess)<1):
                    raise inp
                check=0
                break
            except ValueError:
                check=1
                print("Invalid input")  
            except inp:
                check=1
                print("Invalid Input")  
        if check==1:
            break
        guess=float(guess)
        guess=int(guess)
        if guess>=21 or guess<=0:
            print("Out of range input. Enter again")
            flag+=1        
        elif guess>num:   
            print("Guess is too high. This is your "+str(flag)+" attempt")
            flag+=1
        elif guess<num:
            print("Guess is too low. This is your "+str(flag)+" attempt")
            flag+=1
        elif guess==num:
            print("Congratulations! You found it at attempt ",flag)
            correct=1
    if check==1:
        break
    if correct==0:
        print("Number is ",int(num))
        conf=input("Do you want to try again?(y): ")
    elif correct==1:
        conf=input("Wanna play the game again?(y): ")