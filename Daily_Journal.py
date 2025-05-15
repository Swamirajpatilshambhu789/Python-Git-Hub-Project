import datetime

Daily_journal = {
    "coding": [],
    "crypto trading": [],
    "studying": [],
    "other": []
}

def add_entry(category, entry):
    Daily_journal[category].append(entry)
    file = open("Daily_Journal.txt", "w")
    file.write(f"{datetime.datetime.now()}: {category.capitalize()}: {entry}\n")

def view_journal():
    for category, entries in Daily_journal.items():
        print(f"{category.capitalize()}:")
        for idx, entry in enumerate(entries, 1):
            print(f"{idx}. {entry}")
        print()

def view_categories():
    print("Available categories:")
    for idx, category in enumerate(Daily_journal.keys(), 1):
        print(f"{idx}. {category}")

def main():
    while True:
        print("Daily Journal")
        print("1. Add Entry")
        print("2. View Journal")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_categories()
            category = input("Enter the category: ")
            entry = input("Enter your entry: ")
            add_entry(category, entry)
        elif choice == "2":
            view_journal()
        elif choice == "3":
            print("Exiting the journal.")
            break
        else:
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":
    main()  
