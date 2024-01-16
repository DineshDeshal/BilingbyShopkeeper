while True:
    customer_name = input("Customer name:--")
    total = 0

    while True:
        print("Please enter your amount and quantity")

        amount = int(input("Product:--"))
        quantity = int(input("Product_Quantity:--"))
        total += amount * quantity
        print("Sir, Your bill:---", total)

        another_product = input("If you want to buy any other product:-- YES/NO ")
        if another_product.lower() == "no":
            break

    print("_" * 50)
    print("Customer name:", customer_name)
    print("Bill:", total)
    print("_" * 50)

    repeat1 = input("Do you want to go to the next customer:-- (yes/no)")
    if repeat1.lower() == "no":
        break




