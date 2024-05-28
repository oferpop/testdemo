# Test Management System

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Overview

The Test Management System is a command-line tool designed by Mr. Ofer Koren for performing basic mathematical operations and checks on numbers. It includes functionality to add, subtract, calculate the sum of digits, and check if a number is a palindrome.

---

## Features

- Addition of two numbers
- Subtraction of two numbers
- Calculation of sum of digits in a number
- Checking if a number is a palindrome

---

## Installation

### Prerequisites

- Python 3.8 or higher
- `pip` package installer

### Clone the repository

```bash
git clone : https://github.com/oferpop/testdemo.git
cd test-management-system
Create a virtual environment (optional but recommended)
bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install dependencies
bash
Copy code
pip install -r requirements.txt
Usage
bash
Copy code
python app.py
Choose an operation from the menu:

Enter 1 for addition
Enter 2 for subtraction
Enter 3 for sum of digits
Enter 4 for palindrome check
Enter 5 to exit
Follow the prompts to input numbers and view results.

Project Structure
markdown
Copy code
test-management-system/
│
├── app.py
│
├── tools/
│   ├── __init__.py
│   └── numbers/
│       ├── __init__.py
│       ├── simp.py
│       └── comp.py
│
├── requirements.txt
├── LICENSE
└── README.md
app.py: Main script implementing the command-line interface and application logic.
tools/: Directory containing modules for mathematical operations.
tools/numbers/: Subdirectory with modules for simple and complex operations.
requirements.txt: File listing all Python dependencies for the project.
LICENSE: MIT License file for open-source distribution.
README.md: Documentation file providing an overview of the project.
Dependencies
The following Python packages are used:

icecream: For debugging and logging.
enum34: Compatibility library for Python Enum.
pyfiglet: For generating ASCII art text.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/add-new-feature).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/add-new-feature).
Create a new Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, please contact Mr. Ofer Koren at oferpop@gmail.com.

# testdemo
