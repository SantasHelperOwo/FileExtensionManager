import os
import sys

rename_history = {}

def scan_directory(path="."):
    try:
        files = os.listdir(path)
        print(f"\nFiles in directory: {path}")
        if not files:
            print("  [No files found]")
        for f in files:
            print(f"  {f}")
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

        print(f"\nCategorized files in: {path}")
        for category, items in categorized.items():
            print(f"{category}:")
            if not items:
                print("  [None]")
            for item in items:
                print(f"  {item}")

    except FileNotFoundError:
        print("Directory not found.")

def rename_files(path="."):
    global rename_history
    rename_history = {}
    try:
        files = os.listdir(path)
        counter = {}

        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext == "":
                continue

            if ext not in counter:
                counter[ext] = 1
            else:
                counter[ext] += 1

            new_name = f"file_{counter[ext]}{ext}"
            old_path = os.path.join(path, f)
            new_path = os.path.join(path, new_name)

            os.rename(old_path, new_path)
            rename_history[new_name] = f
            print(f"Renamed: {f} -> {new_name}")

    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied while renaming files.")

def revert_files(path="."):
    global rename_history
    try:
        for new_name, old_name in rename_history.items():
            new_path = os.path.join(path, new_name)
            old_path = os.path.join(path, old_name)
            os.rename(new_path, old_path)
            print(f"Reverted: {new_name} -> {old_name}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Allow user to pass a folder path when running the program
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.getcwd()

    while True:
        print("\nFile Extension Manager")
        print("1. Scan directory")
        print("2. Categorize files by extension")
        print("3. Rename files by extension")
        print("4. Revert renamed files")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            scan_directory(path)
        elif choice == "2":
            categorize_files(path)
        elif choice == "3":
            rename_files(path)
        elif choice == "4":
            revert_files(path)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
