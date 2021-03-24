while True:
 import random
 player=["rock","paper","scissor"]
 winlist=[["rock","scissor"],["paper","rock"],["scissor","paper"]]
 while True:
    random=random.choice(player)
    play=input("rock?paper?or scissor?").strip()
    if play not in player:
        play=input("your inout was not understandable! re-type!").strip()
        continue
    if play==random:
        print("draw!")
    elif [random,play] in winlist:
        print("you won!!")
    else:
        print("you lost!")
