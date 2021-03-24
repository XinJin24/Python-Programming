import random
true=random.randint(0,99)
count=0
left=0
print("you have ten chances to get the right number!")
guess=int(input("guess a number!!"))
left=10-count
while 0<=guess<=99:
   if count==10:
       if guess>true:
        print("your number is so high!,game over!")
        print("true number is ",true,".")
       elif guess<true:
        print("your number is so low!,game ovrer!")
        print("true number is ",true,".")
       else:
        print("you finally got it!!",)
        print("true number is ",true,".")
       break
   else:
    left=10-count
    if guess>true:
          print("your number is so high!")
          print("you have ",left,"try!")
    elif guess<true:
          print("you number is so low !")
          print("you have ",left,"try!")
    else:
          print("you got it, you used ",count,"chances to got it!")
          break
    guess = int(input("guess a number:"))

    count=count+1

else:
     print("type right number!game over!")
    
    
