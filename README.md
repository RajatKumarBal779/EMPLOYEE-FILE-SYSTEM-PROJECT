# Employee Information System (Python – File Handling Project)
A simple file-system–based Employee Management System built using Python. This project demonstrates how to store, retrieve, update, and manage employee records using binary files with the pickle module. The program provides a clean menu-driven interface to perform all CRUD operations.
***
## 📌 About the Project
The system uses Python file handling, custom exception handling, and modular programming. All data is securely stored in a binary file named empdetails.data.
- This project is designed as a console-based application to manage employee records such as:
  - Employee Number (Unique ID)
  - Employee Name
  - Salary
  - Company Name
***
## 🔧 Features
- Add New Employee
  - Stores employee details as a list.
  - Uses custom name validation and exception handling.
  - Prevents duplicate Employee Numbers.
- Delete Employee
  - Searches for an employee and removes the record from the file.
- Update Employee
  - Allows updating salary and company name for a specific employee.
- View Employee Details
  - Displays detailed information for a single employee.
- View All Employees
  - Displays all employee records in a tabular format.
- Search Employee
  - Searches employees by Employee Number and validates if they exist.
- Exit
  - Gracefully ends the program.
***
## 🗂️ Project Structure
1. Employeeadd.py
- Add new employee
2. Employeedelete.py
- Delete employee record
3. Employeeupdate.py
- Update salary and company name
4. Employeeview.py
- View one or all employees
5. Employeesearch.py
- Search employee by ID
6. Empmenu.py
- Displays the main menu
7. Employeemainproject.py
- Main driver program
8. empdetails.data
- Binary file storing employee records
***
## 🧠 Concepts Used
### 📁 File Handling
- Reading and writing binary data using pickle
- Loading and dumping objects using pickle.load() and pickle.dump()
### 🧩 Modular Programming
- Each operation is handled in a separate Python file for cleaner design
### ⚠️ Exception Handling
- Handling EOFError, ValueError, and custom exceptions
- Custom exceptions like:
- ZeroNameLengthError
- SpaceError
- InvalidNameError
### 🧮 Validation
- Name and company name validations using external validation functions
### 🔄 CRUD Operations
- Full Create / Read / Update / Delete functionality on employee data
### 🎛️ Menu-Driven Interface
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
## 📬 Contact
For questions, suggestions, or collaboration, feel free to reach out:
- [LinkedIn – Rajat Kumar Bal](https://www.linkedin.com/in/rajat-kumar-bal)
***
Happy Coding! 🚀
