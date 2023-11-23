print("""Welcome to Treasure Island.
Your mission is to find the treasure.""")

choice1 = input("You are at a cross road, choose \"left\" of \"right\": ").lower()
if choice1 == "left":
    choice2 = input("You are now at a river, choose to \"wait\" or \"swim\": ").lower()
    if choice2 == "wait":
        choice3 = input("You door do you want to enter, \"red\", \"blue\" or \"yellow\": ").lower()
        if choice3 == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")


