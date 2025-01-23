import random
plhth=20
slht=15

print("you encounter a slime that has ", slht, "hp and you have", plhth, "hp, so what do you do?")
while slht > 0:
    choice = input("Do you attack(1), heal(2) or run(3)? ")
    miss = random.randint(0, 1)
    atk = random.randint(2, 3)
    healrate = random.randint(1, 3)
    ham = plhth+healrate
    slatkdmg=random.randint(2,3)
    slmatk = random.randint(0, 1)

    if slmatk == 1:
        plhth -= slatkdmg
        print("the slime attacked you! you have ", plhth, "hp left")

    if choice == "1":
        if miss == 1:
            print("You miss! the health of the slime remains at", slht, "hp, and you have", plhth, "hp")
        else:
            slht -= atk
            print("you dealt", atk, "damage, the slime has", slht, "hp remaining")

    elif choice == "2":
        if ham > 20:
            print("your health is too high to heal")
        else:
            plhth += healrate
            print("you have healed", healrate, "health, you now have", plhth, "hp left")

    else:
        print("you ran away, seriously?!")
        exit()

    if plhth < 1:
        print("the you is die")
        break

    if slht < 1:
        print("the slime is die")
        break



