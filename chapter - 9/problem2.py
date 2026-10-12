# The game() function in the program lets a user play a games and returns the score as an integer. You need to read  a file 'Hi.score.txt' which is either blank or contains the previous Hi score. You need to write a program ton update the Hi score whenever the game() function breaks the Hi score.

import random 

def game():
    print("You are playing the game..")
    return random .randint(1 , 62)
# fetch the hiscore.
with open("hiscore.txt") as f:
    hiscore = f.read
    if(hiscore!= ""):
        hiscore = int (hiscore)
    else: 
        hiscore = 0
    print(f"Your score: {score}")
    if(score>hiscore): 
# write this hiscore of the file.
     with open("hiscore.txt" , "w") as f:
      f.write(str(hiscore))
return score 

game()



# eski file hiscore hai [hiscore.txt]
