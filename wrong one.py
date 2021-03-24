while True:
 import random
 windows = random.randint(1, 3)
 credit=0
 def paper(play):
    import credit

    if windows==1:
        print("draw!! ou have ",credit,"credit now!")
    elif windows==2:
        credit.append(-1)
        print("you lost!!you have ",sum(credit),"credit now!")
        return credit
    elif windows==3:
        credit.append(1)
        print("you won!you have ",sum(credit),"credit now!")
        return credit
    return credit  
 def rock(play):
    if windows==1:
        credit.append(-1)
        print("you lost you have ",sum(credit),"credit now!")
        return credit
    elif windows ==2:
        credit.append(1)
        print("you won!you have ",sum(credit),"credit now!")
        return credit
    elif windows==3:
        print("draw!ou have ",sum(credit),"credit now!")
    return credit
 def scissor(play):
    if windows==1:
        credit.append(1)
        print("you won!you have ",sum(credit),"credit now!")
        return credit
    if windows ==2:
        print("draw ou have ",sum(credit),"credit now!")
    elif windows==3:
        credit.append(-1)
        print("you lost ou have ",sum(credit),"credit now!")
        return credit
    return credit

 play=int(input("what you want to play?(1.paper,2.scissor,3.rock)：：："))
 if play ==1:
        paper(play)
 elif play==2:
        scissor(play)
 elif play==3:
        rock(play)
