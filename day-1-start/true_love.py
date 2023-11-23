# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
full_name = name1 + name2

true = 0
love = 0
for letter in full_name:
    match letter:
        case "t" | "r" | "u" | "e":
            true += 1

    match letter:
        case "l" | "o" | "v" | "e":
            love += 1

print(str(true)+str(love))
