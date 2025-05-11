from LibraryManager import LibraryManager

manager = LibraryManager()
manager.load_data()

while True:
    user_choice = input("Enter option\n1.Add book\n2.Show library report\n3.Borrow book\n"
                        "4.Return book\n5.Show borrow book\n6..Exit\n")

    if user_choice == "1":
        book_name = input("Enter book name: ")
        stock = int(input("Enter book stock: "))
        msg = manager.add_book(book_name, stock)
        print(msg)

    elif user_choice == "2":
        library_report = manager.show_library_report()
        print("Library stock:")
        for book, stock in library_report.items():
            print(f"- {book}: {stock}")

    elif user_choice == "3":
        book_name = input("Enter book name: ")
        amount = int(input("Enter book amount: "))
        msg = manager.borrow_book(book_name, amount)
        print(msg)

    elif user_choice == "4":
        book_name = input("Enter book name: ")
        amount = int(input("Enter book amount: "))
        msg = manager.return_book(book_name, amount)
        print(msg)

    elif user_choice == "5":
        borrow_report = manager.show_borrow_report()
        print("Borrowed books:")
        for book, amount in borrow_report.items():
            print(f"- {book}: {amount}")

    elif user_choice == "6":
        manager.save_data()
        print("Record report to json complete.")
        break