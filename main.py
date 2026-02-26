def main():
    while True:
        print("\nFile Extension Manager")
        print("1. Scan directory")
        print("2. Categorize files by extension")
        print("3. Rename files by extension")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Scanning directory... (function coming soon)")
        elif choice == "2":
            print("Categorizing files... (function coming soon)")
        elif choice == "3":
            print("Renaming files... (function coming soon)")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
