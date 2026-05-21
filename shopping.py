snacks = ["chips","chocolate","juice","biscuits","sandwich"]
prices=[20,50,30,10,70]
cart=[]
bill=[]
while True:
    print("\n=====SNACK MENU====")
    for i in range(len(snacks)):
        print(i+1,",",snacks[i],"- Rs.",prices[i])
        choice=int(input("choose your snack number:"))
        if choice >= 1 and choice <=len(snacks):
            cart.append(snacks[hoice-1])
            bill.append(prices[choice-1])
            print(snacks[choice-1],"added to cart successfully!")
        else:
            print("invalid choice!")
            continue
        more=input("do you want to add more snacks?(yes\no)")
        if more.lower()!="yes":
            break
        print("---------------------------------")
        print("total snacks bought:",len(cart))
        print("total amount    :Rs.",sum(bill))
        print("--------------------------------")
        confirm=input("confirm order?(yes?no):")
        if confirm.lower()=="yes":
            print("order placed successfully!")
            print("enjoy your snacks")
        else:
            print("order cancelled")
