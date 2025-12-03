## Employee Information System (Python – File Handling Project)
A simple file-system–based Employee Management System built using Python. This project demonstrates how to store, retrieve, update, and manage employee records using binary files with the pickle module. The program provides a clean menu-driven interface to perform all CRUD operations.
***
## 📌 About the Project
This project is designed as a console-based application to manage employee records such as:
Employee Number (Unique ID)
Employee Name
Salary
Company Name
The system uses Python file handling, custom exception handling, and modular programming. All data is securely stored in a binary file named empdetails.data.
***
## 🔧 Features
✅ 1. Add New Employee
Stores employee details as a list.
Uses custom name validation and exception handling.
Prevents duplicate Employee Numbers.
✅ 2. Delete Employee
Searches for an employee and removes the record from the file.
✅ 3. Update Employee
Allows updating salary and company name for a specific employee.
✅ 4. View Employee Details
Displays detailed information for a single employee.
✅ 5. View All Employees
Displays all employee records in a tabular format.
✅ 6. Search Employee
Searches employees by Employee Number and validates if they exist.
✅ 7. Exit
Gracefully ends the program.
***
## 🗂️ Project Structure
Employeeadd.py         # Add new employee
Employeedelete.py      # Delete employee record
Employeeupdate.py      # Update salary and company name
Employeeview.py        # View one or all employees
Employeesearch.py      # Search employee by ID
Empmenu.py             # Displays the main menu
Employeemainproject.py # Main driver program
empdetails.data        # Binary file storing employee records
***
## 🧠 Concepts Used
## 📁 File Handling
- Reading and writing binary data using pickle
- Loading and dumping objects using pickle.load() and pickle.dump()
## 🧩 Modular Programming
- Each operation is handled in a separate Python file for cleaner design
## ⚠️ Exception Handling
- Handling EOFError, ValueError, and custom exceptions
- Custom exceptions like:
- ZeroNameLengthError
- SpaceError
- InvalidNameError
## 🧮 Validation
- Name and company name validations using external validation functions
## 🔄 CRUD Operations
- Full Create / Read / Update / Delete functionality on employee data
## 🎛️ Menu-Driven Interface
- Organized user interaction using pattern matching (match-case)
***
## 📘 Learning Outcomes
- How to use binary files for data persistence
- Implementing CRUD operations without a database
- Structuring Python programs using modules
- Creating menu-driven applications
- Using the pickle module to store complex data
- Writing cleaner, maintainable code using separation of concerns
- Handling data validation and user input safely
- Working with custom exception classes
***
## ▶️ How to Run the Project
1. Ensure all .py files and empdetails.data are in the same directory.
2. Run the main program:
3. python Employeemainproject.py
4. Follow the menu options displayed in the terminal.
***
## 🛠 Requirements
- Python 3.10 or above (recommended for match-case)
- No external libraries required (only built-in modules)
***
## 🤝 Contributing
Feel free to fork this project and submit pull requests.
Suggestions and improvements are always welcome!
***
## 📄 License
This project is open-source and free to use.
***
Happy Coding! 🚀
