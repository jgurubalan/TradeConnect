from kite_session import kite

try:
    holdings = kite.holdings()

    print("\n===== HOLDINGS =====")

    if not holdings:
        print("No holdings found.")
    else:
        for stock in holdings:
            qty = stock["quantity"]
            avg_price = stock["average_price"]
            last_price = stock["last_price"]
            pnl = stock["pnl"]

            print("\n------------------------")
            print(f"Symbol      : {stock['tradingsymbol']}")
            print(f"Exchange    : {stock['exchange']}")
            print(f"Quantity    : {qty}")
            print(f"Avg Price   : ₹{avg_price:.2f}")
            print(f"Last Price  : ₹{last_price:.2f}")
            print(f"P&L         : ₹{pnl:.2f}")
            print(f"Value       : ₹{qty * last_price:.2f}")

except Exception as e:
    print(f"Error: {e}")