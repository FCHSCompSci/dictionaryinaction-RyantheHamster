item_shop = {
    'Healing Potion' : 100,
    'Grappling Hook' : 250,
    'Level 1 Armor' : 50,
    'Level 2 Armor' : 200,
    'Level 3 Armor' : 350,
    }
money = 500
while True:
    answer = input("Do you want to see the (s)hop or do you wanna check (c)urrency? ")
    if answer == "s":
        print("ITEM SHOP")
        for key, value in item_shop.items():
            print("%s:%s" %(key, value))

        choice = input("What do you want to buy? Or do you want to see your (c)urrency? ")
        if choice in item_shop.items():
            print("no")
        elif choice == "c":
            print("YOUR MONEY IS %s" %(money))
        else:
            money = money - item_shop.get(choice)
            print("You bought %s and your balance is %s" %(choice, money))
    if answer == "c":
        print("YOUR MONEY IS %s" %(money))
   
   
