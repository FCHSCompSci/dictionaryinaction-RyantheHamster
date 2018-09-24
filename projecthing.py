# Ryan Gumm
#Item_Shop_Dictionary
# 9/24/2018

item_shop = {
    'Medkit' : 100,
    'Grappling Hook' : 250,
    'Sensor Dart' : 200,
    'Barricade' : 300,
    'Frag Grenade' : 100,
    '9-Bang' : 150,
    'Concussion Grenade' : 100,
    'Combat Axe' : 200,
    'Cluster Grenade' : 200,
    'Mesh Mine' : 250,
    'Molotov' : 150,
    'Monkey Bomb' : 100,
    'Level 1 Armor' : 50,
    'Level 2 Armor' : 200,
    'Level 3 Armor' : 350,
    }
money = 2000
inventory = {
    }
while True:
    answer = input("Do you want to see the (s)hop, check (b)alance, or check (i)nventory? ")
    if answer.strip() == "s":
        print("ITEM SHOP \n")
        for key, value in sorted(item_shop.items()):
            print("%s:%s " %(key, value))

        choice = input("What do you want to buy, or your (b)alance, or see (i)nventory? ")
        if choice in item_shop:
            if money - item_shop.get(choice) < 0:
                    print("You can't afford that! ")
            else:
                money = money - item_shop.get(choice)
                if choice in inventory:
                    inventory[choice] += 1
                else:
                    inventory[choice] = 1
                print("You bought %s and your balance is %s" %(choice, money))
        elif choice.strip() == "b":
            print("Your balance is %s" %(money))
        elif choice.strip() == "i":
            if inventory: 
                print("%s:%s" %(key, value))
            else:
                print("Your inventory is empty! ")
        else:
            print("That is not in the shop!")
        
            
    if answer.strip() == "b":
        print("Your balance is %s" %(money))
    if answer.strip() == "i":
        if inventory:
            for key, value in inventory.items():
                print("%s:%s" %(key, value))
        else:
            print("Your inventory is empty! ")

