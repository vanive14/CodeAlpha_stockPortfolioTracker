# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

# Store user's portfolio
portfolio = {}

print("===================================")
print("       STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

# Ask the user how many different stocks they want
number_of_stocks = int(input("\nHow many different stocks do you want to buy? "))

# Take stock names and quantities from the user
for i in range(number_of_stocks):

    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        portfolio[stock] = quantity
    else:
        print("Stock not available in the list.")
        print("Please choose from the available stocks.")

# Calculate total investment
total_investment = 0

print("\n===================================")
print("          PORTFOLIO DETAILS")
print("===================================")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print(stock, "x", quantity, "=", "$", investment)

print("-----------------------------------")
print("Total Investment: $", total_investment)
print("-----------------------------------")

# Save the result to a text file
save_file = input("\nDo you want to save the result? (yes/no): ").lower()

if save_file == "yes":

    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("=======================\n\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"{stock} x {quantity} = ${investment}\n"
            )

        file.write("\nTotal Investment: $" + str(total_investment))

    print("Portfolio saved successfully in portfolio.txt")

else:
    print("Portfolio was not saved.")

print("\nThank you for using Stock Portfolio Tracker!")