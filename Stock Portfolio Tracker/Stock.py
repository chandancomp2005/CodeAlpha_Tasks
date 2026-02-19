import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 155
}

def show_available_stocks():
    print("\n📌 Available Stocks & Prices:")
    for stock, price in stock_prices.items():
        print(f"{stock} = ${price}")


def portfolio_tracker():
    portfolio = {}  # store user stocks

    print("📈 Welcome to Stock Portfolio Tracker!")
    show_available_stocks()

    while True:
        stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not found in price list. Try again!")
            continue

        try:
            qty = int(input(f"Enter quantity for {stock}: "))
            if qty <= 0:
                print("❌ Quantity must be greater than 0.")
                continue
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        # Add quantity (if stock already exists, add more)
        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"✅ Added {qty} shares of {stock}.")

    if not portfolio:
        print("\n⚠️ No stocks added. Exiting...")
        return

    # Display portfolio summary
    print("\n📊 Portfolio Summary:")
    print("-" * 45)
    print(f"{'Stock':<10}{'Qty':<10}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    total_value = 0
    portfolio_data = []

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        total_value += value

        print(f"{stock:<10}{qty:<10}{price:<10}{value:<10}")

        portfolio_data.append([stock, qty, price, value])

    print("-" * 45)
    print(f"💰 Total Investment Value: ${total_value}")

    # Optional save
    save = input("\nDo you want to save the result? (yes/no): ").lower()

    if save == "yes":
        file_type = input("Save as (txt/csv): ").lower()

        if file_type == "txt":
            with open("portfolio.txt", "w") as file:
                file.write("Portfolio Summary\n")
                file.write("-" * 45 + "\n")
                file.write(f"{'Stock':<10}{'Qty':<10}{'Price':<10}{'Value':<10}\n")
                file.write("-" * 45 + "\n")

                for row in portfolio_data:
                    file.write(f"{row[0]:<10}{row[1]:<10}{row[2]:<10}{row[3]:<10}\n")

                file.write("-" * 45 + "\n")
                file.write(f"Total Investment Value: ${total_value}\n")

            print("✅ Saved successfully as portfolio.txt")

        elif file_type == "csv":
            with open("portfolio.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Stock", "Quantity", "Price", "Value"])
                writer.writerows(portfolio_data)
                writer.writerow([])
                writer.writerow(["Total", "", "", total_value])

            print("✅ Saved successfully as portfolio.csv")

        else:
            print("❌ Invalid file type. Not saved.")

    else:
        print("👍 Okay! Not saving the file.")


# Run the program
portfolio_tracker()
