def calculate_total_price(items, discount):
    total = 0

    for i in range(len(items)):
        total = total + items[i]["price"] * items[i]["qty"]

    if discount > 0:
        total = total - (total * discount / 100)

    return total


items = [
    {"price": 100, "qty": 2},
    {"price": 50, "qty": 3},
    {"price": 20, "qty": 1},
]

print(calculate_total_price(items, 10))
