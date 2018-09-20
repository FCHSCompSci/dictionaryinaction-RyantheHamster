item_shop = {
    'Medkit' : 100,
    'Grappling Hook' : 250,
    'Level 1 Armor' : 50,
    'Level 2 Armor' : 200,
    'Level 3 Armor' : 350,
    }
money = 500
inventory = {
    }
while True:
    answer = input("Do you want to see the (s)hop, check (c)urrency, or check (i)nventory? ")
    if answer == "s":
        print("ITEM SHOP \n")
        for key, value in item_shop.items():
            print("%s:%s " %(key, value))

        choice = input("What do you want to buy, your (c)urrency, or see (i)nventory? ")
        if choice in item_shop:
            money = money - item_shop.get(choice)
            if money < 0:
                    print("You can't afford that! ")
                    money = money + item_shop.get(choice)
            else:
                if choice in inventory:
                    inventory[choice] += 1
                else:
                    inventory[choice] = 1
                print("You bought %s and your balance is %s" %(choice, money))
        elif choice == "c":
            print("YOUR MONEY IS %s" %(money))
        elif choice == "i":
            if inventory == {}:
                print("Your inventory is empty! ")
            else:
                print(inventory)
        else:
            print("no")
        
            
    if answer == "c":
        print("YOUR MONEY IS %s" %(money))
    if answer == "i":
        if inventory == {}:
            print("Your inventory is empty! ")
        else:
            for key, value in inventory.items():
                print("%s:%s" %(key, value))

