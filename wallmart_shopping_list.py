#import ast
cart=[]
item1=input("enter item")#items=ast.literal_eval(item1)
cart.append(item1)
item2=input("enter item")
cart.append(item2)
item3=input("enter item")
cart.append(item3)
if 'milk' in cart:
    print("Don't forget to keep it cold")
else:
    print("milk is not in the cart")
new_item=input("enter new item")
cart[1]=new_item
print(new_item)
for item in cart:
    print("you are buying",item)
