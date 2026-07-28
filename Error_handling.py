while True :
    action=input("enter 'run' if you want to run and 'exit' to stop")
    if action=='run':
        a=int(input("enter your number"))
        try :
            result=10/a
            print(result)
        except ZeroDivisionError:
            print("error")
        except ValueError:
            print("error")
    elif action=='exit':
        break


