# ls=[]
# n=int(input("enter your list numer"))
# for j in range(0,n):
#     ele=int(input())
#     ls.append(ele)
# print(ls)
# ls.sort()
# lar=ls.pop()
# if(sum(ls)<lar):
#     print("yes")
# else:
#  print("no")
#
# ls=[100,200,400,600]
# # x=0
# for i in range(len(ls)):
#     print(ls[i])
# #     if ls[i]<=100:
# #         x += 1
# #         continue
sampleArray=[5,4,10,90,70,46,50,3,88,100]
def findBiggestNumberr(sampleArray):
    biggestNumber=sampleArray[0]
    for i in range(1,len(sampleArray)):
        if(sampleArray[i]>biggestNumber):
            biggestNumber=sampleArray[i]
    print(biggestNumber)        



