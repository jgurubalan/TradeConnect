from kite_session import kite
from kiteconnect.exceptions import KiteException

try:
    orders = kite.orders()

    print("\n===== ORDER STATUS =====")

    if not orders:
        print("No orders found.")
    else:
        for order in reversed(orders):  # newest first
            print("-" * 60)
            print(f"Order ID      : {order['order_id']}")
            print(f"Symbol        : {order['tradingsymbol']}")
            print(f"Transaction   : {order['transaction_type']}")
            print(f"Quantity      : {order['quantity']}")
            print(f"Filled Qty    : {order['filled_quantity']}")
            print(f"Price         : {order['price']}")
            print(f"Status        : {order['status']}")
            print(f"Order Type    : {order['order_type']}")
            print(f"Product       : {order['product']}")
            print(f"Time          : {order['order_timestamp']}")

except KiteException as e:
    print("Kite API error:", e)

except Exception as e:
    print("Error:", e)