from kite_session import kite

try:
    margins = kite.margins()

    cash = margins["equity"]["available"]["cash"]
    live_balance = margins["equity"]["available"]["live_balance"]

    print("\n===== AVAILABLE FUNDS =====")
    print(f"Cash         : ₹{cash:,.2f}")
    print(f"Live Balance : ₹{live_balance:,.2f}")

except Exception as e:
    print(f"Error: {e}")