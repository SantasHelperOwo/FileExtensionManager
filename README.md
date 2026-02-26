# File Extension Manager

This project is a command-line tool built in Python to automate file management tasks.  
It was developed as part of coursework to demonstrate file handling, version control, and testing.

## Features
- Scan Directory: Lists all files in the current folder
- Categorize Files: Groups files by extension (e.g., Images, Documents, Executables)
- Rename Files: Renames files systematically (e.g., file_1.txt, file_2.png)
- Revert Files: Restores original filenames using saved history
- CLI Menu: Simple interface for selecting operations

## Structure
- main.py: Contains all functions and CLI logic
- README.md: Project overview and usage instructions

## Testing
Each function was tested individually.  
Screenshots and results are included in the report.

## Version Control
Git was used for version control.  
Each function was committed separately to ensure clear history and traceability.  
Repository Link: https://github.com/SantasHelperOwo/FileExtensionManager

## References
1. Python Documentation: https://docs.python.org/3/library/os.html  
2. Git Documentation: https://git-scm.com/docs  
3. GitHub Guides: https://docs.github.com/en  
4. Stack Overflow discussions on Python file handling

## Installation and Usage

To set up and run the File Extension Manager:

1. Clone the repository:
git clone https://github.com/SantasHelperOwo/FileExtensionManager.git

2. Navigate into the project folder:
cd FileExtensionManager

3. Make sure Python 3 is installed on your system.
Run the program using: python main.py


When executed, the program will display a menu with options:
1. Scan directory  
2. Categorize files  
3. Rename files  
4. Revert files  
5. Exit  

Enter the number corresponding to the action you want to perform. The program will execute the function and return to the menu until you choose Exit.
