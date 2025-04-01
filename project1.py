food = 0
water = 0
clothes = 0
radiation_suit = 0



print("You have a brand-new and happy family, but unfortunately, the Third World War has broken out. In desperation, all countries have resorted to nuclear weapons. One of them exploded 30 kilometers away from your home.")
print("Now you have to lead your famliy to survive")
print("Do you want to start the game?")
user = input("yes or no")
if user == "yes":
    print("You can carry a total of ten items. Here is the list of items")
    print("1.food\n2.water\n3.clothes\n4.radiation suit")
    choice = input("Which items would you like to choose?")
    if choice == "1":
        food = food + 1
    elif choice == "2":
        water = water + 1
    elif choice == "3":
        clothes == clothes + 1
    elif choice == "4":
        radiation_suit == radiation_suit + 1


    