import random

confirmation = input("Do you want to roll the dice?")

start = 1
end = 6
roll = "y"

while roll == "y":
    value = random.randint(start, end)

    if value == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if value == 2:
        print("-----")
        print("     ")
        print(" 0 0 ")
        print("     ")
        print("-----")
    if value == 3:
        print("-----")
        print("0    ")
        print("  0  ")
        print("    0")
        print("-----")
    if value == 4:
        print("-----")
        print(" 0 0 ")
        print("     ")
        print(" 0 0 ")
        print("-----")
    if value == 5:
        print("-----")
        print("0   0")
        print("  0  ")
        print("0   0")
        print("-----")
    if value == 6:
        print("-----")
        print(" 0 0 ")
        print(" 0 0 ")
        print(" 0 0 ")
        print("-----")
        
    



















