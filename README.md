# File Extension Manager

This project is a simple command-line tool written in Python to automate basic file management tasks.  
It was developed as part of coursework to practice file handling, version control, and testing.

## Features
- **Scan Directory:** Lists all files in a chosen folder
- **Categorize Files:** Groups files by extension (Images, Documents, Executables, Others)
- **Rename Files:** Renames files systematically (e.g., file_1.txt, file_2.png)
- **Revert Files:** Restores original filenames using saved history
- **CLI Menu:** Easy interface for selecting operations

## Structure
- `main.py` – contains all functions and CLI logic
- `README.md` – project overview and usage instructions
- Test folders:
  - `normalfolder` – mixed files for normal case
  - `emptyfolder` – no files for empty case
  - `unsupportedfolder` – files with uncommon extensions
  - `renamefolder` – files used for rename/revert testing

## Testing
The program was tested with different scenarios:
1. Normal case – folder with mixed files
2. Empty folder – handled gracefully with no crash
3. Invalid path – showed “Directory not found”
4. Unsupported file type – categorized under “Others”
5. Rename & Revert – renamed files and restored them correctly

Screenshots of each case are included in the report.

## Version Control
Git was used for version control.  
Each function and test case was committed separately to keep history clear.  
Repository Link: [https://github.com/SantasHelperOwo/FileExtensionManager](https://github.com/SantasHelperOwo/FileExtensionManager)

## References
1. Python Documentation – https://docs.python.org/3/library/os.html  
2. Git Documentation – https://git-scm.com/docs  
3. GitHub Guides – https://docs.github.com/en  
4. Stack Overflow discussions on Python file handling

## Installation and Usage

Steps to run the File Extension Manager:

1. Clone the repository:
   ```bash
   git clone https://github.com/SantasHelperOwo/FileExtensionManager.git
2. Navigate into the project folder:
   ```bash
   cd FileExtensionManager
3. Make sure Python 3 is installed on your system.
Run the program using: py main.py "path_to_folder"
#When executed, the program shows a menu:

1.Scan directory
2.Categorize files
3.Rename files
3.Revert files
4.Exit
-Enter the number for the action you want. The program runs the function and returns to the menu until you choose Exit.

##Future Improvements

Some possible improvements:

Add a simple GUI for easier use
More advanced categorization (by size, date, metadata)
Batch operations across multiple folders
Logging or reports of actions performed
Packaging as an executable for Windows/macOS/Linux

These would make the tool more practical and closer to real-world applications.
