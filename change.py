def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print(f"\nVuelto")
    print(f"\nPesos:")
    print(int(money-expense))
    print("Centavos:")
    print(int((float(money-expense)-int(money-expense))*100))
