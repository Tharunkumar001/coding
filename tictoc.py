"""for i in range(1,10):
    print(i,end=" ")
    if(i==3 or i==6):
        print("\n")"""
list1 = [1,2,3,4,5,6,7,8,9]
def tic(list1):
    for i in range(0, 3):
        print("******************")
        for j in range(0, 1):
            if (i == 0):
                print("|  " + str(list1[0]) + "  |  " + str(list1[1]) + "  |  " + str(list1[2]) + "  |")
            elif (i == 1):
                print("|  " + str(list1[3]) + "  |  " + str(list1[4]) + "  |  " + str(list1[5]) + "  |")
            else:
                print("|  " + str(list1[6]) + "  |  " + str(list1[7]) + "  |  " + str(list1[8]) + "  |")
    print("******************")
tic(list1)

list2 = []
for k in range(0,3):
    player1 = int(input("Enter a position player1 \n"))
    s = player1 - 1

    if (player1 in list1 and player1 not in list2):
            list1.insert(s,"X")
            list1.remove(player1)
            list2.append(player1)
            tic(list1)
    else:
        player1 = int(input("Enter a valid position player1 \n"))
        if (player1 in list1 and player1 not in list2):
            list1.insert(s, "X")
            list1.remove(player1)
            list2.append(player1)
            tic(list1)


    player2 = int(input("Enter your position player2 \n"))
    ss = player2 - 1

    if (player2 in list1 and player2 not in list2):
            list1.insert(ss,"O")
            list1.remove(player2)
            list2.append(player2)
            tic(list1)
    else:
        player2 = int(input("Enter valid position player2 \n"))
        if (player2 in list2 and player1 not in list2):
            list1.insert(ss, "O")
            list1.remove(player2)
            list2.append(player2)
            tic(list1)











