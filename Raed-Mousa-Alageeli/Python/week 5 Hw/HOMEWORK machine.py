due = 50

while due > 0:
    coin = input("Insert Coin: ")

    if not coin.isdigit():
        print("Please insert a valid integer coin")
        continue

    coin = int(coin)

    if coin not in [5, 10, 25]:
        print(f"Coin not accepted. Returning {coin} cents")
        print(f"Amount Due: {due}")
        continue

    due -= coin

    if due > 0:
        print(f"Amount Due: {due}")

print(f"Change Owed: {abs(due)}")
