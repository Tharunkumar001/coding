test = int(input())

hike = list(str(input()))

arr = []
sums = 0
#print(hike)

for valley in hike:
    if(valley == 'U'):
        sums = sums+1
        arr.append(sums)
    elif(valley == 'D'):
        sums = sums - 1
        arr.append(sums)

#print(arr)

arr1 = []

for result in range(1,len(arr)):

   if(arr[result] == 0):
       if (arr[result - 1] == -1):
           
           arr1.append(0)
       else:
           continue
#print(arr1)

save = arr1.count(0)
print(save)











