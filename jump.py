testcase = int(input())

jump = list(map(int,input().split()))

list1 = []

list2 = []

sums = 0

if(1 not in jump):
    ss = jump.count(0)
    print(int(ss/2))
else:

    for loop1 in range(0, len(jump)):
        if (jump[loop1] == 1):
            sums = sums + 1
            list2.append(loop1)
            save = list1.count(0)
            if (save >= 2):
                save1 = int(save / 2)
                sums = sums + save1
                list1.clear()
            else:
                list1.clear()
                continue
        else:
            index = loop1
            list1.append(jump[loop1])

    save3 = list1.count(0)

    if (save3 > 1):
        save4 = int(save3 / 2)
        sums = sums + save4
        print(int(sums))
    else:
        print(int(sums))







