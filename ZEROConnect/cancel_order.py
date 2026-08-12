from kite_session import kite
from kiteconnect.exceptions import KiteException, OrderException

print("===== OPEN ORDERS =====")

try:
    orders = kite.orders()

    open_orders = [
        o for o in orders
        if o["status"] in ["OPEN", "TRIGGER PENDING"]
    ]

    if not open_orders:
        print("No open orders found.")
        raise SystemExit

    for i, order in enumerate(open_orders, start=1):
        print(
            f"{i}. "
            f"{order['tradingsymbol']} | "
            f"{order['transaction_type']} | "
            f"Qty:{order['quantity']} | "
            f"Price:{order['price']} | "
            f"Status:{order['status']} | "
            f"ID:{order['order_id']}"
        )

    choice = int(input("\nSelect order number to cancel: "))

    order = open_orders[choice - 1]

    confirm = input(
        f"Type YES to cancel {order['tradingsymbol']} "
        f"({order['order_id']}): "
    ).strip().upper()

    if confirm != "YES":
        print("Cancellation aborted.")
        raise SystemExit

    kite.cancel_order(
        variety=kite.VARIETY_REGULAR,
        order_id=order["order_id"]
    )

    print("\n✅ Order cancelled successfully")

except OrderException as e:
    print("\n❌ Order cancellation rejected")
    print(e)

except KiteException as e:
    print("\n❌ Kite API error")
    print(e)

except Exception as e:
    print("\n❌ Error")
    print(e)