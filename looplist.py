#for loop
looplist=["rafi","kafi","safi","mafi"]
for i in looplist:
    print(i)

#for loop position print
looplist=["rafi","kafi","safi","mafi"]

for i in range(len(looplist)):
    print(i)

#while loop
y=0
while y<len(looplist):
    print(looplist[y])
    y=y+1

    #list comprehension

    num=[1,2,3,4,5]
    double=[i*2 for i in num]
    print(double)

    #sort list
    num=[1,2,91,13,3,4,5]
    num.sort()
    print(num)

   #reverse list
    num=[1,2,91,13,3,4,5]
    num.sort(reverse=True)
    print(num)  