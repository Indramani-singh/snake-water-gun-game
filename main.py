'''
-1 for water
0 for gun
1 for snake

'''
import random

computer= random.choice([-1,0,1]) 
youstr= input("Enter your choice: ")
dict= {
    "snake":1,
    "water":-1,
    "gun":0
    }
reverseDict= {
    1:"snake",
    -1:"water",
    0:"gun"
}

you= dict[youstr]

print(f"Your choice is: {youstr}\nComputer choice is: {reverseDict[computer]}")

if(computer==you):
    print("Game Draw!")
elif(computer==1 and you==-1):
    print("Computer wins!")    
elif(computer==1 and you==0):
    print("you win!")
elif(computer==-1 and you==0):
    print("computer win!")
elif(computer==-1 and you==1):
    print("you win!")
elif(computer==0 and you==1):
    print("computer win!")
elif(computer==0 and you==-1):
    print("you win!")
else:
    print("Something went wrong!")