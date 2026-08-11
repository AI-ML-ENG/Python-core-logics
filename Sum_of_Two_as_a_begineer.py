lists=[2,7,11,15]
target=9
num=len(lists)
final=[]
for i in lists:
    num=i
    for j in lists:
        num1=j
        add=num+num1
        if add==target:
            sum=j=i
            final.append(sum)
print(final)


