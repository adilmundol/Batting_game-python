import random

def battinggame():
    #odd or even
    while True:
        print("odd or even")
        uchoice=input()
        if uchoice!='odd' and uchoice!='even':
            print("invalid input")
            continue
        pcchoice='odd'
        if uchoice=='even':
            pcchoice='odd'
        else:
            pcchoice='even'
        print("computer choice:",pcchoice)
        unumber=int(input("enter a number btw 1-6:"))
        if  unumber<1 or unumber>6:
            print("invalid input")
            continue
        pcnumber=random.randint(1,6)
        print("computer choice:",pcnumber)

        if(unumber+pcnumber)%2==0 and  uchoice=='even':
            print("you won the odd or even  game , you get choose ") 
            battingchoice=input("enter 'bat' or 'bowl':")
            if battingchoice=='bat':
                batting='user'
            else:
                batting='pc'
            break
        elif(unumber+pcnumber)%2!=0 and  uchoice=='odd':
            print("you won the odd or even  game , you get choose ") 
            battingchoice=input("enter 'bat' or 'bowl':")
            if battingchoice=='bat':
                batting='user'
            else:
                batting='pc'
            break
        else:
            print("pc wins  the odd or even game , pc gets choose")
            if random.choice(['bat','bowl'])=='bat':
                batting='pc'
                print("pc chose to bat")
            else:
                batting='user'
                print("pc chose to bowl")
            break
    print("........................batting game starts.....................................")
    #batting game
    uscore=0
    pcscore=0
    while True:
        if batting=='user':
            uroll=int(input("enter your roll (1-6):"))
            if uroll<1 or uroll>6:
                print("invalid input")
                continue
            pcroll=random.randint(1,6)
            print("user roll:",uroll)
            print("pc roll:",pcroll)
            if uroll==pcroll:
                print("you're out!!!!")
                batting='pc'
                break
            else:
                uscore+=uroll
        else:
            pcroll=random.randint(1,6)
            uroll=int(input("enter your roll (1-6):"))
            if uroll<1 or uroll>6:
                print("invalid input")
                continue
            print("user roll:",uroll)
            print("pc roll:",pcroll)
            if uroll==pcroll:
                print("pc out!!")
                batting='user'
                break
            else:
                pcscore+=pcroll
    #batting switch
    print("..........................switch batting................................")
    while True:
        if batting=='user':
            uroll=int(input("enter your roll (1-6):"))
            if uroll<1 or uroll>6:
                print("invalid input")
                continue
            pcroll=random.randint(1,6)
            print("user roll:",uroll)
            print("pc roll:",pcroll)
            if uroll==pcroll:
                print("you're out!!!")
                break
            else:
                uscore+=uroll
        else:
            pcroll=random.randint(1,6)
            uroll=int(input("enter your roll (1-6):"))
            if uroll<1 or uroll>6:
                print("invalid input")
                continue
            print("user roll:",uroll)
            print("pc roll:",pcroll)
            if uroll==pcroll:
                print("pc out!!")
                break
            else:
                pcscore+=pcroll
    #comparing scores
    print("........................................final score.............................................")
    print("user final score:",uscore)
    print("pc final score:",pcscore)
    if uscore>pcscore:
        print("you win!!!!!!")
    elif uscore<pcscore:
        print("pc wins!!!!!!!")
    else:
        print("it's a tie!!!!!!")
battinggame()