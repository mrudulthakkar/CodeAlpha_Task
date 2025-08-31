import random

fruits = ["apple", "banana", "mango", "litchi", "grapes"]
vegetables = ["potato", "tomato", "onion", "brinjal", "cabbage"]
milk_products = ["cheese", "paneer", "curd", "ghee", "butter"]

user_choice = int(input("enter the category\n1.Fruits\n2.Vegetables\n3.Milk Items: "))

if user_choice == 1:
    word = random.choice(fruits)
elif user_choice == 2:
    word = random.choice(vegetables)
elif user_choice == 3:
    word = random.choice(milk_products)
else:
    print("Invalid choice!")
    exit()

trials = 0    
temp_ls = ["_"] * len(word)
ls = ["_"] * len(word)

while trials < 6:
    print("".join(ls))
    letter = input("enter the char: ")
    
    for i in range(len(word)): 
        if letter == word[i]:
            ls[i] = letter

    if temp_ls == ls:
        trials += 1
        print("❌ Incorrect guess. Trials left:", 6 - trials)
    else:
        print("✅ Good guess!")
    
    temp_ls = ls.copy()

    if "_" not in ls:
        print("".join(ls), " ✅ You guessed the word!")
        break

if trials == 6:
    print("YOU ARE OUT OF TRIALS ❌")
    print("The word was:", word)
