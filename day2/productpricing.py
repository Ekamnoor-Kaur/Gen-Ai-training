products=[]
productprice=0.0
while True:
    print("1. add product")
    print("2. view all products with price")
    print("3. gst calculate")
    print("4. discount>=3000 10%, <=2000 6%")
    print("5. final bill")

    ch=int(input("enter choice"))
    if ch==1:
        productname=input("enter product name")
        productquantity=int(input("enter product quantity"))
        price=int(input("enter price"))
        productprice+=price*productquantity
        print(productprice)
        products.append([productname,productquantity,price])
        print("product added")
    elif ch==2:
        if len(products)==0:
            print("no product found")
        for product in products:
            print("Product :",product[0]," Product price : ",product[2], "Product Quantity : ", product[1])
    elif ch==3:
        productprice=productprice+0.18*productprice
        print("total price without discount : ",productprice)
    elif ch==4:
        if productprice>=3000:
            productprice-=(0.10*productprice)
        elif productprice<=2000:
            productprice-=(0.06*productprice)
        print(productprice)
    elif ch==5:
        print("final bill",productprice)
        break
    else:
        print("enter a valied choice")