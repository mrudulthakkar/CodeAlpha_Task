stock_dict = {
    "reliance": 1380,
    "asian paints": 2570,
    "wipro": 259,
    "infosys": 1500,
    "ola": 45,
    "tcs": 3015
}

user_portfolio = dict()
is_investor = int(input("Enter 1 if you are an investor else enter 0: "))
total_investment = 0

if is_investor:
    user_ch = 1
    while user_ch:
        user_stock = input("Enter the name of the stock: ").lower()

        if user_stock not in stock_dict:
            print("We do not have this stock listed.")
        else:
            user_quantity = int(input(f"How many stocks of {user_stock} do you have? "))
            user_portfolio[user_stock] = user_quantity
            total_investment += stock_dict[user_stock] * user_quantity

        user_ch = int(input("Enter 1 if you have more investment in other stocks else enter 0: "))


with open("stocks_info.txt", "w", encoding="utf-8") as file_obj:
    file_obj.write("The stock details are:\n")
    for stock, price in stock_dict.items():
        file_obj.write(f"{stock} : {price}\n")

    file_obj.write("-------------------\n")
    file_obj.write("User Stock Details:\n")
    for user_stock, user_quantity in user_portfolio.items():
        file_obj.write(f"{user_stock} : {user_quantity}\n")

    file_obj.write(f"Your total investment = ₹{total_investment}\n")
    file_obj.write("THANK YOU")

print("✅ Portfolio details have been saved to stocks_info.txt")
