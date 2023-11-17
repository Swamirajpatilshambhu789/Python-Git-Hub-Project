# Intro
print("Welcome to Recipt Maker")

# Making Receipt and converting it into txt file
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

# Making a dict to store the item name and its price
items = {}

# Continueing till all items are entered
while True:
    try:
        # Asking for name of item
        item = input("Enter the name of the item(enter done to finish): ")

        # If all items are entered
        if item=='done':
            break
        
        # Asking for Price of item
        price = input("Enter the price of the item: ")

        # Storing name and price into dict
        items[item] = float(price)

        # Calling Function
        receipt = writer(items)

    # Handling Error
    except:
        print("Enter valid input")
        continue