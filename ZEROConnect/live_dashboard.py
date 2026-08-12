from kite_session import kite
import os
import time

REFRESH_SECONDS = 5

while True:
    try:
        os.system("clear")  # Mac/Linux

        print("=" * 90)
        print("               ZERODHA LIVE TRADING DASHBOARD")
        print("=" * 90)

        # Funds
        margins = kite.margins()
        available = margins["equity"]["available"]

        print("\nFUNDS")
        print("-" * 90)
        print(f"Live Balance : ₹{available.get('live_balance', 0):,.2f}")
        print(f"Cash         : ₹{available.get('cash', 0):,.2f}")

        # Holdings
        holdings = kite.holdings()

        print("\nHOLDINGS")
        print("-" * 90)

        if holdings:
            print(
                f"{'Symbol':<15}"
                f"{'Qty':<10}"
                f"{'Avg Price':<15}"
                f"{'LTP':<15}"
                f"{'PnL':<15}"
            )

            for h in holdings:
                print(
                    f"{h['tradingsymbol']:<15}"
                    f"{h['quantity']:<10}"
                    f"{h['average_price']:<15.2f}"
                    f"{h['last_price']:<15.2f}"
                    f"{h['pnl']:<15.2f}"
                )
        else:
            print("No holdings.")

        # Orders
        orders = kite.orders()

        print("\nRECENT ORDERS")
        print("-" * 90)

        if orders:
            print(
                f"{'Symbol':<15}"
                f"{'Side':<8}"
                f"{'Qty':<8}"
                f"{'Filled':<8}"
                f"{'Status':<15}"
                f"{'Price':<12}"
            )

            for order in reversed(orders[-10:]):
                print(
                    f"{order['tradingsymbol']:<15}"
                    f"{order['transaction_type']:<8}"
                    f"{order['quantity']:<8}"
                    f"{order['filled_quantity']:<8}"
                    f"{order['status']:<15}"
                    f"{order['price']:<12}"
                )
        else:
            print("No orders.")

        print("\nRefreshing every 5 seconds... (Ctrl+C to quit)")
        time.sleep(REFRESH_SECONDS)

    except KeyboardInterrupt:
        print("\nDashboard stopped.")
        break

    except Exception as e:
        print(f"\nError: {e}")
        time.sleep(5)