a=[[1,2],[2,7],[5,9,20]]
b=[5,9,4,2,6,10,6]
messages = ["hello world", "this is amazing", "dont click that link", "hello human"]
block_list = ["link", "human"]
heh=[]
for msg in messages:
    print(msg.split(),end=' ')
correction=[f'{j}'for i in messages for j in i.split() if j not in block_list]


print(correction)