# stone paper scissor project 

import random

"""
stone = 1
paper = 2
scissor = 3

"""



print("welcome to ROCK, PAPER, SCISSOR Game")
print("""Rock = 1 \n
paper = 2\n
scissor = 3""")

user_op = int(input("Enter your choice : "))

def RPSI_game():
            game_dict = {

                1 :"Rock " ,
                2 : "paper" ,
                3 : "scissor"
            }
            comp = random.choice([1,2,3])

            usrstr = game_dict[user_op]
            compstr = game_dict[comp]

            print("your choice is :", usrstr,"\n" ,"computer choice is :",compstr)

            if(user_op == comp) :
                print("it is a draw! Thank you for playing.")

            else :

                if(user_op == 1 and comp == 2) :
                    print("computer wins! Thank you for playing.")

                elif(user_op == 1 and comp == 3) :
                    print("You win! Thank you for playing.")

                elif(user_op == 2 and comp == 1) :
                    print("You win! Thank you for playing.")

                elif(user_op == 2 and comp == 3) :
                    print("Computer win! Thank you for playing.")

                elif(user_op == 3 and comp == 1) :
                    print("Computer win! Thank you for playing.")

                elif(user_op == 3 and comp == 2) :
                    print("You win! Thank you for playing.")

                else :
                    print("something went wrong! Try Again Later.")


RPSI_game()






















