import ast
while True:
    sibling=input('enter your sibling name and age')
    try:
        siblings=ast.literal_eval(sibling)
        if isinstance(siblings,list) or siblings== 'stop':
           print(siblings)

    except:
        print("the name and age is not in list")
        break
