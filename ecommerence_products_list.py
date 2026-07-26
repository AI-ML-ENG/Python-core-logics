from codecs import namereplace_errors
def products():
    list= ['laptop','mouse','keyboard','monitor']
    return list
products=products()
print(products)
while True:
    try:
        user_order=input("enter your order or press enter to exit")
        converting=str(user_order)
        products.remove(converting)
        print(products)
        if user_order == 'exit':
            break
    except:
        namereplace_errors
        print(namereplace_errors)
        break

