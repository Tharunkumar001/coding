a = str(input("enter your class name"))
e = 'p'
f = 'a'
g = 'o'
list1 = []
list2 = []
list3 = []
dict1 = {64: 'mythily.R', 65: 'mythily.P', 66: 'Naveenkarthik.k R', 67: 'Neshika.S', 68: 'Nikilprasath.S',
         69: 'Nishanthini.S', 70: 'nitheshprawin.P', 71: 'Nivetha.E', 72: 'pinjala supriya', 73: 'ponvasanth.R',
         74: 'prathisha.N', 75: 'Praveen.K P', 76: 'praveenraj.N', 77: 'Prawin.N', 78: 'preethi.M A B',
         79: 'Pugalenthi.N M', 80: 'Rahul M', 81: 'Rahul Gandhi.V', 82: 'Ranitha.N M', 83: 'Ranjana.P', 84: 'Ranjith.N',
         85: 'Riya k Mathew', 86: 'Sabarinath.M', 87: 'Sangavi.A', 88: 'Sanjai.R', 89: 'Sanjai.S', 90: 'Sankaran.S M',
         91: 'Santhoshkumar.K A', 92: 'Saranya.S', 93: 'Sathyapriya.M', 94: 'Sathyarooba.V', 95: 'Sathyasri.J',
         96: 'Sethupathi.V', 97: 'Sanmugapriya.R J', 98: 'Sanmugapriya.V', 99: 'SANTHOSH.A C', 100: 'Srikala.V',
         101: 'sruthiga.S', 102: 'Sham Kishore.V', 103: 'Sivaneshwarn.R N', 104: 'SONIYA.D', 105: 'Sreeraam.K',
         106: 'Sri Abhirame.B M', 107: 'Srinithi.K', 108: 'Srivarshan.S N', 109: 'Subarna.S', 110: 'Sugumar.S',
         111: 'Sugant.B', 112: 'Surya.M', 113: 'Swathi.D', 114: 'Tamilarasan.S', 115: 'Thanvee Ahamed.M',
         116: 'Tharunkumar.G', 117: 'Thirugnanasambantham.N', 118: 'Udaya.M', 119: 'Umamaheshwari.J',
         120: 'Vaishnavi Suvetha.S', 122: 'Vedeshvar.L', 123: 'Vidhyavarshini.L', 124: 'Vignesh Kumar.M',
         125: 'Vishnu Prasath.J'}
if (a == "cse"):
    for key, val in dict1.items():
        print(key)
        b = str(input("enter p or a or o"))

        if (b == e):
            list1.append(key)
        elif (b == f):
            list2.append(key)
        elif (b == g):
            list3.append(key)
        else:
            print("enter a valid input")
        print("\n")
    print("present members")
    # print(list1,list2,list3)
    u = len(list1)
    if (u == 0):
        print("no presenties")
    else:
        for k in list1:
            print(k, "(", dict1[k], ")")
    print("no of present is", u)
    print("\n")
    print("abesent members")
    s = len(list2)
    if (s == 0):
        print("no absenties well done keep it up")
    else:
        for l in list2:
            print(l, "(", dict1[l], ")")
    print("no of absent is", s)
    print("\n")
    print("od members")
    y = len(list3)
    if (y == 0):
        print("no od members")
    else:
        for m in list3:
            print(m, "(", dict1[m], ")")
    print("no of od is", y)
    print("\n")
    print("bye see u later👋 👋 👋 ")
else:
    list4 = []
    list5 = []
    list6 = []
    print(a)
    print("\n just enter roll no full form")
    print("ur roll is 19csr116 then u enter 116")
    q = int(input("enter starting roll no of ur class"))
    w = int(input("enter a ending roll no of ur class"))
    for v in range(q, w + 1, 1):
        print(v)
        r = str(input("enter p or a or od"))
        if (r == e):
            list4.append(v)
        elif (r == f):
            list5.append(v)
        elif (r == g):
            list6.append(v)
        else:
            print("enter a valid input")
    print("\n")
    print(" present members")
    x = len(list4)
    if (x == 0):
        print("no presenties")
    else:
        for o in list4:
            print("roll no", o)
        print("no of present is", x)
    print("\n")
    xx = len(list5)
    if (xx == 0):
        print("no absenties well done keep it up")
    else:
        for z in list5:
            print("roll. no", z)
        print("no of absent is", xx)
    print("\n")
    xxx = len(list6)
    if (xxx == 0):
        prnt("no od's")
    else:
        for zz in list6:
            print("roll no", zz)
        print("no of od is", xxx)
print("bye see u soon 👋 👋 👋 ")
