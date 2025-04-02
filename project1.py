import random
def reduce_randomly(a,b):
    a -= random.choice([1,2])
    b -= random.choice([1,2])
    return a, b
def probaility_randomly(c):
    c -= random.choice([0,5])
    return c
food = 0
water = 0
clothes = 0
radiation_suit = 0
total_items = 0
game1 = True
game2 = True
print("You have a brand-new and happy family, but unfortunately, the Third World War has broken out. In desperation, all countries have resorted to nuclear weapons. One of them exploded 30 kilometers away from your home.")
print("Now you have to lead your famliy to survive")
print("Do you want to start the game? yes or no ")   
user = input("")
if user == "yes":
    while game1:
        print("You can carry a total of ten items. Here is the list of items")
        print("1.food\n2.water\n3.clothes\n4.radiation suit")
        choice = input("Which items would you like to choose?") 
        if choice == "1":
            print("How much do you want to take")
            number = int(input())
            food += number
        elif choice == "2":
            print("How much do you want to take")
            number = int(input())
            water += number
        elif choice == "3":
            print("How much do you want to take")
            number = int(input())
            clothes += number
        elif choice == "4":
            print("How much do you want to take")
            number = int(input())
            radiation_suit += number
        else:
            print("Please choose right number")
        if water + food + clothes + radiation_suit > 10:
            print("It is too much, you only can bring ten items")
            food = 0
            water = 0
            clothes = 0
            radiation_suit = 0
        elif water + food + clothes + radiation_suit == 10:
            print("That's enough. YOu' re going to the basement to escape this disaster")
            game1 = False
elif user == "no":
    game1 = False
else:
    print("Please input Yes or NO")
'''print("You will carry these items to await military rescue")
print("Day ONe")
print("You eat some food and water for you lunch")
water, food = reduce_randomly(water, food)
print(f"You still have {water} bottles of water")
print(f"You still have {food} bottles of water")
print("After you finish your lunch you have two choices\n1.Put on a radiation suit and go outside to find food\n2.Stay in the basement")
while game2:
    choice = input()
    if choice == "1":
        if radiation_suit >= 1:
            print("You have a radiation suit. Please select the destination you want to go\n1.restaurant\n2.shop\n3.hospital")
            if choice == "1":
                print("You choose to go to a restaurant")
                if random.random() < 0.5:
                    print("The restaurant is open")
                    open = reduce_randomly(open)
                    if probaility_randomly() == 0:
                        print("You don't find the food")
                    elif probaility_randomly() >3 <5:
                        print(f"You got {c} food ")
                else:
                    print("The restaurant is close")
    elif choice == "2":
        print("OK")'''