def split(s):
    return list (s)

s = str(input())

integer = int(input())

save = split(s)

list1 = []

list2 = []
save1 = int(integer/len(s))
save2 = int(integer % len(s))
save3 = s.count('a')
save4 = save1 * save3

if(len(s) > integer):
    for loop2 in range(0,integer):
        list2.append(save[loop2])
    print(list2.count('a'))

elif(save1 != 0 ):
    for loop1 in range(0,save2):
        list1.append(save[loop1])
    save5 = list1.count('a')
    print(int(save4+save5))
else:
    print(int(save4))




