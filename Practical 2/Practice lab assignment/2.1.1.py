menu = ["Add", "Remove", "Display", "Quit"]
lst = []

while True:
    for i, item in enumerate(menu, 1):
        print(f"{i}. {item}")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input")
        continue

    if choice == 1:
        try:
            a = int(input("Integer: "))
            lst.append(a)
            print("List after adding:", lst)
        except ValueError:
            print("Invalid input")
    elif choice == 2:
        if not lst:
            print("List is empty")
            continue
        a = int(input("Integer: "))
        if a in lst:
            lst.remove(a)
            print("List after removing:", lst)
        else:
            print("Element not found")
    elif choice == 3:
        print("List is empty" if not lst else lst)
    elif choice == 4:
        break
    else:
        print("Invalid choice")