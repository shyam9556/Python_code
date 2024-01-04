#it is evalute the equation
# a=eval(input("enter equation"))
# print(a)
# for j in range(4):
#     print("")
#     for i in range(4):
#         print("# ",end="")

num=int(input("Enter the number"))
for i in range(2,num):
    if num%i == 0:
        print("not prime")
        break
else:
    print("prime")