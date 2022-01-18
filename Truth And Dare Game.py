#Truth And Dare Game
import random
player = []
a = int(input("Number Of Player: "))
for i in range(0,a):
    x = input("Player = ").upper()
    player.append(x)
while True:
    print("To Add Player's type 143")
    print("To Remove Player's type 153")
    aa = len(player)
    question = player[random.randint(0,aa-1)]
    answer = player[random.randint(0,aa-1)]

    if question != answer:
        print("Question = ",question.capitalize())
        print("Answer = ",answer.capitalize())
        print("To Spin Press Enter Else 1")
        Spin = input()
        if Spin == "1":
            break
        if Spin == "143":
            a_1 = int(input("Number Of Player You Want To Add: "))
            for i in range(0,a_1):
                x_1 = input("Player = ").upper()
                player.append(x_1)
            print("Sucessfully Added Player")
        if Spin == "153":
            a_2 = int(input("Number Of Player You Want To Remove: "))
            for i in range(0,a_2):
                x_2 = input("Player = ").upper()
                player.remove(x_2)
            print("Sucessfully Removed Player")
            
                
        
