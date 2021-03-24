import random
true=random.randint(0,99)
count=0
left=0
print ("Number(0,100) guess game")
print ("You will have 10 times to guess")
print ("Guess out of range will game over immediately!")
guess = int(input("guess a number:"))
count=count+1
left=10-count
while 0<=guess<=99:
    if count==10:
        if guess>true:
          print("too high, game over!, the true number is :",true)
        elif guess<true:
          print("too low, game over!, the true number is :",true)
        else:
          print("you finally got it, the true number is:",true)
        break
    else:
     left=10-count
     if guess>true:
            print("too high, guess again!")
            print("you have ",left,"tries")
 
     elif guess<true:
         
            print("too low, guess again!")
            print("you have ",left,"tries")
     else:
          print("you win!")
          print("you take ",count,"try to got it!")
          break
     guess = int(input("guess a number:"))
     count=count+1
     
else:
    print("you number is not correct!game over!!!")
