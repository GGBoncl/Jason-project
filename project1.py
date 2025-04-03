import random

def reduce_randomly(a, b):
    a -= random.choice([1, 2])
    b -= random.choice([1, 2])
    return max(a, 0), max(b, 0)  

def probability_randomly():
    return random.choice([0, 5])  

food = 0
water = 0
clothes = 0
radiation_suit = 0
total_items = 0
day = 0
health = 10
game1 = True
game2 = True

print("You have a brand-new and happy family, but unfortunately, the Third World War has broken out. In desperation, all countries have resorted to nuclear weapons. One of them exploded 30 kilometers away from your home.")
print("Now you have to lead your family to survive.")
print("Do you want to start the game? yes or no ")   
user = input().lower()

if user == "yes":
    while game1:
        print("You can carry a total of ten items. Here is the list of items")
        print("1. Food\n2. Water\n3. Clothes\n4. Radiation suit")
        choice = input("Which items would you like to choose? (Enter number) ") 

        if choice in ["1", "2", "3", "4"]:
            number = int(input("How much do you want to take? "))
            if choice == "1":
                food += number
            elif choice == "2":
                water += number
            elif choice == "3":
                clothes += number
            elif choice == "4":
                radiation_suit += number
        else:
            print("Please choose a valid number.")

        if water + food + clothes + radiation_suit > 10:
            print("It is too much, you can only bring ten items.")
            food, water, clothes, radiation_suit = 0, 0, 0, 0  
        elif water + food + clothes + radiation_suit == 10:
            print("That's enough. You're going to the basement to escape this disaster.")
            game1 = False
print("\nYou will carry these items to await military rescue.")
print("Day One")
day += 1
print("You eat some food and water for lunch.")
if water and food > 0:
    water, food = reduce_randomly(water, food)
    print(f"You still have {water} bottles of water.")
    print(f"You still have {food} units of food.")
elif water and food == 0:
    print("You don't have food")
    health -= 1

print("After you finish your lunch, you have two choices:\n1. Put on a radiation suit and go outside to find food\n2. Stay in the basement")

while game2:
    choice = input()
    if choice == "1":
        if radiation_suit >= 1:
            print("You have a radiation suit. Please select the destination you want to go:\n1. Restaurant\n2. Shop\n3. Hospital")
            location_choice = input()

            if location_choice == "1":
                print("You choose to go to a restaurant.")
                if random.random() < 0.5:
                    print("The restaurant is open.")
                    food_found = probability_randomly()
                    water_found = probability_randomly()
                    if food_found == 0:
                        print("You don't find any food.")
                    else:
                        print(f"You got {food_found} units of food.")
                        food += food_found
                    if water_found == 0:
                        print("You don't find any water.")
                    else:
                        print(f"You find {water_found} bottle of water")
                        water += water_found
                    if food_found and water_found == 0:
                        print("You feel tired, and back to the basement")
                else:
                    print("The restaurant is closed.\nYou choose back to the basement")
            if location_choice == "2":
                print("You choose to go to a shop")
                if random.random() < 0.5:
                    print("The restaurant is open.")
                    food_found = probability_randomly()
                    water_found = probability_randomly()
                    if food_found == 0:
                        print("You don't find any food.")
                    else:
                        print(f"You got {food_found} units of food.")
                        food += food_found
                    if water_found == 0:
                        print("You don't find any water.")
                    else:
                        print(f"You find {water_found} bottle of water")
                        water += water_found
                    
                else:
                    print("The shop is closed.\nDo you want to go to othehr way?yes or no")
                    
    elif choice == "2":
        print("You chose to stay in the basement and rest.")
        game2 = False 
    else:
        print("Please enter a valid choice (1 or 2).")