print("PLEACE DONT PLACE YOUR 3 COINS IN A LINE FIRST TIME \n")

print("LETS START A GAME")

list1 = [1,2,3,4,5,6,7,8,9]
def tic(list1):
    for i in range(0, 3):
        print("******************")
        for j in range(0, 1):
            if (i == 0):
                print("|  " + str(list1[0]) + "  |  " + str(list1[1]) + "  |  " + str(list1[2]) + "  |  ")
            elif (i == 1):
                print("|  " + str(list1[3]) + "  | " + str(list1[4]) + "   |  " + str(list1[5]) + "  |  ")
            else:
                print("|  " + str(list1[6]) + "  |  " + str(list1[7]) + "  |  " + str(list1[8]) + "  |  ")
    print("******************")
tic(list1)

def moving_posibility(n):
    if (n == 1):
        list_1 = [2, 4]
        return list_1
    elif (n == 2):
        list_2 = [1, 3, 5]
        return list_2
    elif (n == 3):
        list_3 = [2, 6]
        return list_3
    elif (n == 4):
        list_4 = [1, 5, 7]
        return list_4
    elif (n == 5):
        list_5 = [2,4,6,8]
        return list_5
    elif (n == 6):
        list_6 = [3, 5, 9]
        return list_6
    elif (n == 7):
        list_7 = [4, 8]
        return list_7
    elif (n == 8):
        list_8 = [5, 7, 9]
        return list_8
    elif(n==9):
        list_9 = [6, 8]
        return list_9
    else:
        print('please enter valid input')

def checking_position(y,o):
    list3 = []
    for loop8 in o:
        if(loop8 == "x1" or loop8 == 'X1'):
            list3.append(o.index(loop8)+1)
        elif(loop8 == "x2" or loop8 == 'X2'):
            list3.append(o.index(loop8)+1)
        elif(loop8 == 'x3' or loop8 == 'X3'):
            list3.append(o.index(loop8 )+1)
        else:
            continue

    for loop10 in o:
        if (loop10 == "o1" or loop10 == 'O1'):
            list3.append(o.index(loop10) + 1)
        elif (loop10 == "o2" or loop10 == 'O2'):
            list3.append(o.index(loop10) + 1)
        elif (loop10 == 'o3' or loop10 == 'O3'):
            list3.append(o.index(loop10) + 1)
        else:
            continue

    list4 = []

    for loop9 in y:
        if loop9 in list3:
            continue
        else:
            list4.append(loop9)
    return list4

def result(q):
    list4 = ["a","b","c","d","e","f","g","h","i"]
    list5 = [["abc"],["cba"],["acb"],["cab"],["bac"],["bca"],["def"],["dfe"],["edf"],["efd"],["fed"],["fde"],["ghi"],["gih"],["igh"],["ihg"],["hig"],["hgi"],["adg"],["agd"],["dag"],["dga"],["gad"],["gda"],["beh"],["bhe"],["hbe"],["heb"],["ehb"],["ebh"],["cfi"],["cif"],["fci"],["fic"],["ifc"],["icf"]]
    list3 = []
    index_value1 = q.index("x1")
    index_value2 = q.index("x2")
    index_value3 = q.index("x3")

    list3.append(list4[index_value1]+list4[index_value2]+list4[index_value3])
    x =10
    if list3 in list5:
        return x
    else:
        return 0

def result1(q):
    list4 = ["a","b","c","d","e","f","g","h","i"]
    list5 = [["abc"],["cba"],["acb"],["cab"],["bac"],["bca"],["def"],["dfe"],["edf"],["efd"],["fed"],["fde"],["ghi"],["gih"],["igh"],["ihg"],["hig"],["hgi"],["adg"],["agd"],["dag"],["dga"],["gad"],["gda"],["beh"],["bhe"],["hbe"],["heb"],["ehb"],["ebh"],["cfi"],["cif"],["fci"],["fic"],["ifc"],["icf"]]
    list3 = []
    index_value1 = q.index("o1")
    index_value2 = q.index("o2")
    index_value3 = q.index("o3")

    list3.append(list4[index_value1]+list4[index_value2]+list4[index_value3])
    x = 10
    if list3 in list5:
        return x
    else:
        return 0

def input_function(list1):
    list2 = []
    for k in range(0, 3):
        player1 = int(input("Player1 : Enter a position \n"))
        s = player1 - 1

        if (player1 in list1 and player1 not in list2):

            list1.insert(s, "x" + str(k + 1))
            list1.remove(player1)
            list2.append(player1)
            tic(list1)
        else:
            player1 = int(input("Player2: Enter a valid position \n"))
            if (player1 in list1 and player1 not in list2):
                list1.insert(s, "x" + str(k + 1))
                list1.remove(player1)
                list2.append(player1)
                tic(list1)

        player2 = int(input("Enter your position player2 \n"))
        ss = player2 - 1

        if (player2 in list1 and player2 not in list2):
            list1.insert(ss, "o" + str(k + 1))
            list1.remove(player2)
            list2.append(player2)
            tic(list1)
        else:
            player2 = int(input("Enter valid position player2 \n"))
            if (player2 in list2 and player1 not in list2):
                list1.insert(ss, "o" + str(k + 1))
                list1.remove(player2)
                list2.append(player2)
                tic(list1)

input_function(list1)


def player2_move(list1):
    moveFor_player2 = str(input("enter your(Player2) moving coin name o1 or o2 or o3 \n"))
    if (moveFor_player2 == "o1" or moveFor_player2 == 'o2' or moveFor_player2 == 'o3') or (
            moveFor_player2 == "O1" or moveFor_player2 == 'O2' or moveFor_player2 == 'O3'):
        app2 = list1.index(moveFor_player2)
        list1.remove(moveFor_player2)
        list1.insert(app2, app2+1)
        ap1 = app2 + 1
        apps2 = moving_posibility(ap1)

        # get a value to move  a coin to another place

        apps3 = checking_position(apps2, list1)

        if (apps3 == []):
            print('you(Player2) cannot move this coin choose another one')
            list1.insert(app2,moveFor_player2)
            list1.remove(app2+1)
            player2_move(list1)
        else:
            print("moving poibility", apps3)

            moveend1 = int(input("where you(player2) want to place a coin enter a position \n"))

            if moveend1 not in apps3:
                print('please enter valid moving point')
                moveend3 = int(input("where you(Player2) want to place a coin, enter a position \n"))

                if moveend3 not in apps3:
                    print('sorry u start a new game because u make more than 2  mistakes \n')
                    list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    tic(list3)
                else:
                    app2 = list1.index(moveend3)
                    list1.remove(moveend3)
                    list1.insert(app2, moveFor_player2)
                    tic(list1)
                    res1 = result1(list1)
                    if res1 == 10:
                        print('player_2 won the game coungrats!! \n')
                        again = int(input('enter 1 to again start a game \n'))
                        if again == 1:
                            list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            tic(list3)
                            input_function(list3)
                    else:
                        player_move(list1)
            else:

                app2 = list1.index(moveend1)
                list1.remove(moveend1)
                list1.insert(app2, moveFor_player2)
                tic(list1)
                res1 = result1(list1)

                if res1 == 10:
                    print('player_2 won the game coungrats \n')
                    again = int(input('enter 1 to aagain start a game \n'))
                    if again == 1:
                        list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        tic(list3)
                        input_function(list3)
                else:
                    player_move(list1)
    else:
        print("enter valid input may be u had type error")
        player2_move(list1)

def player_move(list1):
    moveFor_player1 = str(input("Which coin you(player1) want to move x1 or x2 or x3 \n"))
    if(moveFor_player1 == "x1" or moveFor_player1 == 'x2' or moveFor_player1 == 'x3') or (moveFor_player1 == "X1" or moveFor_player1 == 'X2' or moveFor_player1 == 'X3'):
        app = list1.index(moveFor_player1)
        list1.remove(moveFor_player1)
        list1.insert(app, app+1)
        ap = app+1
        apps = moving_posibility(ap)

        #get a value to move  a coin to another place

        apps1 = checking_position(apps, list1)

        if(apps1 == []):
            print('you(Player1) cannot move this coin choose another one \n')
            list1.insert(app,moveFor_player1)
            list1.remove(app+1)
            print(list1)
            player_move(list1)
        else:
            print("moving poibility", apps1)

            moveend1 = int(input("where you(Player) want to place a coin, enter a position \n"))

            if moveend1 not in apps1:
                print('please enter valid moving point')

                moveend = int(input("where you(Player1) want to place a coin, enter a position \n"))

                if moveend not in apps1:
                    print('you make more than 2 mistakes so now you start a new game \n')
                    list3 = [1,2,3,4,5,6,7,8,9]
                    tic(list3)
                else:
                    app1 = list1.index(moveend)
                    list1.remove(moveend)
                    list1.insert(app1, moveFor_player1)
                    tic(list1)
                    res = result(list1)
                    if res == 10:
                        print('player_1 won the game coungrats \n')
                        again = int(input('enter 1 to aagain start a game \n'))
                        if again == 1:
                            list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            tic(list3)
                            input_function(list3)
                    else:
                        player2_move(list1)
            else:
                app1 = list1.index(moveend1)
                list1.remove(moveend1)
                list1.insert(app1, moveFor_player1)
                tic(list1)
                res =  result(list1)
                if res == 10:
                    print('player_1 won the game coungrats \n')
                    again = int(input('enter 1 to again start a game \n'))
                    if again == 1:
                         list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                         tic(list3)
                         input_function(list3)
                else:
                    player2_move(list1)
    else:
        print("enter valid input may be u had type error")
        player_move(list1)

player_move(list1)

