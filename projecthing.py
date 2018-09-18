item_shop = {
    'Healing Potion' : 100,
    'Grappling Hook' : 250,
    'Level 1 Armor' : 50,
    'Level 2 Armor' : 200,
    'Level 3 Armor' : 350,
    }

while True:
    print("ITEM SHOP")
    answer = input("Do you want to see the shop? Yes or no? ")
    if answer == "Yes":
        for key, value in item_shop.items():
            print("%s:%s" %(key, value))
    else:
        break
        
    
