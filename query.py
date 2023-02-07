
import data
items = data.items

def main():
    name = input("Please provide your name: ")
    print("Hello, " + name + "!", "What would you like to do" + "?")
    print("Menu:")
    print("1. List items by warehouse")
    print("2. Search an item and place an order")
    print("3. Quit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Warehouse 1 items:")
        for item in items:
            if item["warehouse"] == "Warehouse 1":
                print(item["name"], item["amount"])
        print("Warehouse 2 items:")
        for item in items:
            if item["warehouse"] == "Warehouse 2":
                print(item["name"], item["amount"])
    elif choice == 2:
        item_name = input("Enter item name: ")
        search_item(item_name)
    elif choice not in ['1', '2', '3']:
        print("Error: Invalid operation.")
    else:
        print("thank you for your visit, " + name + "!")


if __name__ == '__main__':
    main()