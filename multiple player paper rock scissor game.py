namearray=[]
creditarray=[]
x=0
y=0
z=0
amount=int(input("how many player?"))
while amount>x:
            name=input("please give me names one by one ")
            namearray.append(name)
            x=x+1
while amount>y:
               print(namearray[y],"play")
               x=0
               credit=0
               while x<5:
                  import random
                  guess_list = ["rock","scissor","paper"]
                  guize = [["paper","rock"],["rock","scissor"],["scissor","paper"]]
                  computer = random.choice(guess_list)
                  print("you have", 5-x,"chances left")
                  people =  input("type:rock, scissor,or paper:").strip()
                  if people not in  guess_list:
                        people =input("retype:rock, scissor,or paper").strip()
                        x=x+1
                        continue
                  elif computer ==people:
                        print("draw！play again!")
                        print("you credit is ",credit)
                        x=x+1
                  elif [computer,people] in guize:
                        print("you lost!！")
                        print("you credit is ",credit)
                        x=x+1
                  else:
                        credit=credit+1
                        print("you won！")
                        print("you credit is ",credit)
                        x=x+1
               else:
                print("no more chance!")
                creditarray.append(credit)
                y=y+1
while amount>z:
             print(namearray[z],creditarray[z])
             z=z+1
             
        
         



        
        
