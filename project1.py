import random
def reduce_randomly(a, b):
    used_a = random.choice([1, 2])
    used_b = random.choice([1, 2])
    actual_used_a = min(a, used_a)
    actual_used_b = min(b, used_b)
    a -= actual_used_a
    b -= actual_used_b
    return max(a, 0), max(b, 0), actual_used_a, actual_used_b
def probability_randomly():
    return random.choice([0, 6])
food = 0
water = 0
medicine = 0
radiation_suit = 0
day = 0
health = 10
max_health = 10
game1 = True
loop = True
print("You were living alone in a remote town. Unfortunately, World War Three broke out and countries started using nuclear weappons. One of them exploded 30 kilometers away from you.")
print("Now you have to make sure you can survive.")
print("Do you want to start the game? yes or no ")

while loop:
    user = input().lower()
    if user == "yes":
        while game1:
            print("You can carry a total of ten items. Here is the list of items:")
            print("1. Food\n2. Water\n3. Medicine\n4. Radiation suit")
            choice = input("Which items would you like to choose? (Enter number) ")
            if choice in ["1", "2", "3", "4"]:
                number = int(input("How much do you want to take? "))
                if choice == "1":
                    food += number
                elif choice == "2":
                    water += number
                elif choice == "3":
                    medicine += number
                elif choice == "4":
                    radiation_suit += number
                print(f"Food {food}, Water {water}, Medicine {medicine}, Radiation Suit {radiation_suit}")        
            else:
                print("Please choose a number.")

            if food + water + medicine + radiation_suit > 10:
                print("Too much! You can only bring 10 items total.")
                food = water = medicine = radiation_suit = 0
            elif food + water + medicine + radiation_suit == 10:
                print("You head into the basement to escape the disaster.")
                game1 = False
        while health > 0 and day < 7:
            day += 1
            print(f"\n--- Day {day} ---")
            print(f"Health: {health}")
            print(f"Food: {food} | Water: {water} | Medicine: {medicine} | Radiation suits: {radiation_suit}")
            print("\nLunch time:")
            food, water, used_food, used_water = reduce_randomly(food, water)
            print(f"Used {used_food} food and {used_water} water.")
            if used_food < 1 or used_water < 1:
                print("Not enough food or water! You lose 1 extra health.")
                health -= 1
            print("Nuclear radiation affects your body. You lose 1 health.")
            health -= 1
            print(f"Current Health: {health}")
            if health <= 0:
                print("\nYou couldn't survive the nuclear aftermath. Game Over.")
                break
            elif health > 0 and day == 7:
                print(f"\nAfter {day} difficult days, the military arrives and rescues your family. You survived. Congratulations!")
                break
            print("\nWhat do you want to do after lunch?\n1. Go outside\n2. Stay in basement\n3. Use medicine")
            action = input()
            if action == "1":
                if radiation_suit > 0:
                    print("You have a radiation suit. Where do you want to go?\n1. Restaurant\n2. Shop\n3. Hospital")
                    p = input()
                    if p in ["1", "2"]:
                        print("You go out scavenging...")
                        if random.random() > 0.5:
                            print("The place is open!")
                            food_found = probability_randomly()
                            water_found = probability_randomly()
                            if food_found > 0:
                                print(f"You found {food_found} food.")
                                food += food_found
                            else:
                                print("No food found.")
                            if water_found > 0:   
                                print(f"You found {water_found} water.")
                                water += water_found
                            else:
                                print("No water found.")
                        else:
                            print("It's closed. You return empty-handed.")
                    elif p == "3":
                        print("You head to the hospital...")
                        if random.random() < 0.5:
                            med_found = probability_randomly()
                            if med_found > 0:
                                print(f"You found {med_found} medicine.")
                                medicine += med_found
                            else:
                                print("No medicine found.")
                        else:
                            print("Hospital is closed.")
                else:
                    print("You don't have a radiation suit and can't go outside.")
            elif action == "2":
                print("You stayed in the basement and rested.")
            elif action == "3":
                if medicine > 0:
                    medicine -= 1
                    healed = min(3, max_health - health)
                    health += healed
                    print(f"You used 1 medicine and recovered {healed} health.")
                else:
                    print("You have no medicine to use.")
            else:
                print("Invalid choice. You lose your chance to act.")
                print("\nDinner time:")
            food, water, used_food, used_water = reduce_randomly(food, water)
            print(f"Used {used_food} food and {used_water} water.")
            if used_food < 1 or used_water < 1:
                print("Not enough food or water! You lose 1 extra health.")
                health -= 1
            print("More radiation exposure. You lose 1 more health.")
            health -= 1
            print(f"End of Day {day} | Health: {health}")
            print(f"Remaining - Food: {food}, Water: {water}, Medicine: {medicine}\n")

            
    elif user == "no":
        print("Ok, bye")
        break
    else:
        print("Please input yes or no")