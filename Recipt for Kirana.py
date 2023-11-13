print("Welcome to Recipt Maker")
def writer(items, tax_rate=0.07):
    total = 0
    receipt = "\n===== Receipt =====\n"
    for item, price in items.items():
        receipt += f"{item}: ${price:.2f}\n"
        total += float(price)

    tax = total * tax_rate
    total_with_tax = total + tax
    
    receipt += f"\nSubtotal: ${total:.2f}"
    receipt += f"\nTax ({tax_rate * 100}%): ${tax:.2f}"
    receipt += f"\nTotal: ${total_with_tax:.2f}\n"

    file = open('recipt.txt', 'w')
    file.write(receipt)

items = {}
while True:
    item = input("Enter the name of the item(enter done to finish): ")
    if item=='done':
        break

    price = input("Enter the price of the item: ")
    items[item] = float(price)

receipt = writer(items)
