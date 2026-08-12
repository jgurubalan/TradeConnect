from kite_session import kite
from kiteconnect.exceptions import KiteException, OrderException

print("===== KITE LIVE ORDER =====")

try:
    # Buy or Sell
    action = input("Buy or Sell? (B/S): ").strip().upper()

    if action == "B":
        transaction_type = kite.TRANSACTION_TYPE_BUY
        action_name = "BUY"
    elif action == "S":
        transaction_type = kite.TRANSACTION_TYPE_SELL
        action_name = "SELL"
    else:
        raise ValueError("Please enter B for Buy or S for Sell")

    # CNC or MIS
    product_choice = input(
        "Trade Type - CNC (Delivery) or MIS (Intraday)? [CNC/MIS]: "
    ).strip().upper()

    if product_choice == "MIS":
        product = kite.PRODUCT_MIS
    elif product_choice == "CNC":
        product = kite.PRODUCT_CNC
    else:
        raise ValueError("Please enter CNC or MIS")

    # Order details
    tradingsymbol = input(
        "Enter stock symbol (e.g. INFY, RELIANCE, SUZLON): "
    ).strip().upper()

    quantity = int(input("Enter quantity: "))
    limit_price = float(input("Enter limit price: ₹"))

    required_amount = quantity * limit_price

    print("\n===== ORDER SUMMARY =====")
    print(f"Action         : {action_name}")
    print(f"Trade Type     : {product_choice}")
    print(f"Symbol         : {tradingsymbol}")
    print(f"Quantity       : {quantity}")
    print(f"Limit Price    : ₹{limit_price:.2f}")

    # BUY FUND CHECK
    if action == "B":
        margins = kite.margins()
        available = margins["equity"]["available"]

        available_funds = available.get("live_balance", 0)

        print(f"Required Amount: ₹{required_amount:.2f}")
        print(f"Available Funds: ₹{available_funds:.2f}")

        if available_funds < required_amount:
            raise ValueError(
                f"Insufficient funds. Need ₹{required_amount:.2f}, "
                f"Available ₹{available_funds:.2f}"
            )

    # CNC SELL HOLDINGS CHECK
    elif action == "S" and product_choice == "CNC":
        holdings = kite.holdings()

        holding_qty = 0

        for holding in holdings:
            if holding["tradingsymbol"] == tradingsymbol:
                holding_qty = holding["quantity"]
                break

        print(f"Holding Qty    : {holding_qty}")

        if holding_qty < quantity:
            raise ValueError(
                f"Insufficient holdings. You own {holding_qty} shares."
            )

    # MIS SELL (short selling)
    elif action == "S" and product_choice == "MIS":
        print("Intraday short-selling (MIS) selected.")

    # Confirmation
    confirm = input(
        "\nType YES to place the LIVE order: "
    ).strip().upper()

    if confirm != "YES":
        print("Order cancelled.")
        raise SystemExit

    # Place order
    order_id = kite.place_order(
        variety=kite.VARIETY_REGULAR,
        exchange=kite.EXCHANGE_NSE,
        tradingsymbol=tradingsymbol,
        transaction_type=transaction_type,
        quantity=quantity,
        product=product,
        order_type=kite.ORDER_TYPE_LIMIT,
        price=limit_price
    )

    print("\n✅ LIVE ORDER PLACED")
    print("Order ID:", order_id)

except OrderException as e:
    print("\n❌ Order rejected by broker/exchange")
    print(e)

except KiteException as e:
    print("\n❌ Kite API error")
    print(e)

except Exception as e:
    print("\n❌ Error")
    print(e)