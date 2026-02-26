import os

def scan_directory(path="."):
    try:
        files = os.listdir(path)
        print("\nFiles in directory:")
        for f in files:
            print(f)
    except FileNotFoundError:
        print("Directory not found.")

def categorize_files(path="."):
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".txt", ".pdf", ".docx"],
        "Executables": [".exe", ".bat", ".sh"],
        "Others": []
    }

    categorized = {"Images": [], "Documents": [], "Executables": [], "Others": []}

    try:
        files = os.listdir(path)
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            found = False
            for category, extensions in categories.items():
                if ext in extensions:
                    categorized[category].append(f)
                    found = True
                    break
            if not found:
                categorized["Others"].append(f)

        print("\nCategorized files:")
        for category, items in categorized.items():
            print(f"{category}:")
            for item in items:
                print(f"  {item}")

    except FileNotFoundError:
        print("Directory not found.")

def main():
    while True:
        print("\nFile Extension Manager")
        print("1. Scan directory")
        print("2. Categorize files by extension")
        print("3. Rename files by extension")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            scan_directory()
        elif choice == "2":
            categorize_files()
        elif choice == "3":
            print("Renaming files... (function coming soon)")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
