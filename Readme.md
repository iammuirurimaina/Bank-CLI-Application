**Banking CLI Application**


The Banking CLI Application is a command-line interface (CLI) program written in Python that simulates basic banking operations. Users can create accounts, log in, view account details, deposit funds, withdraw cash, and transfer money to other users. This application is designed to demonstrate the use of SQLAlchemy, Click, and Alembic for database management, CLI interface, and database migrations, respectively.

**Table of Contents**
Getting Started
Prerequisites
Installation
Usage
Creating a User
Logging In
Viewing All Users
Making Deposits
Withdrawing Cash
Transferring Funds
Database Management
Migrations with Alembic
Debugging
Contributing
License
Getting Started

**Prerequisites**
Before running the Banking CLI Application, make sure you have the following installed:

Python 3.x
Click (CLI library for Python)
SQLAlchemy (SQL toolkit and Object-Relational Mapping (ORM) library)
Alembic (Database migrations tool for SQLAlchemy)


**Installation**
Clone the repository to your local machine:
Navigate to the project directory:
Install the required Python packages using pip:
run python banking_app.py

**Usage**
Creating a User
To create a new user account, run the application and select "Option 1: Add user" from the main menu. You will be prompted to enter the user's name, email, address, and PIN (Personal Identification Number).

Logging In
To log in as an existing user, select "Option 2: Log in to a specific user" from the main menu. Enter the user's email and PIN when prompted. If the credentials are correct, you will be logged in and can access your account.

Viewing All Users
To view a list of all users (without their PINs), select "Option 3: View all users" from the main menu. This option provides a summary of all registered users.

Making Deposits
Once logged in, you can make a deposit into your account by selecting "Option 1: Deposit" from the user menu. Enter the deposit amount when prompted.

Withdrawing Cash
You can withdraw cash from your account by selecting "Option 2: Withdraw" from the user menu. Enter the withdrawal amount when prompted. Ensure you have sufficient balance before making a withdrawal.

Transferring Funds
To transfer money to another user, select "Option 3: Transfer" from the user menu. Enter the recipient's account ID and the transfer amount when prompted. Verify that you have enough funds for the transfer.

Database Management
The Banking CLI Application uses SQLAlchemy to interact with a SQLite database. The database schema is defined in the models.py file, and you can modify the models to suit your needs.

Creating the Database
Ensure you have set up your database as required by modifying your SQLAlchemy models and specifying the database URL (e.g., SQLite) in your code. You can create the database schema by running the following command in your terminal:
bash: python create_database.py
This command will initialize the database with the necessary tables.

Migrations with Alembic
The application includes Alembic for managing database migrations. If you make changes to your SQLAlchemy models, you can generate and apply migrations to update the database schema. Follow these steps:

Initialize Alembic:
alembic init alembic
Configure Alembic:

Edit the alembic.ini file to specify the database URL.

Generate Migrations:

Create a new migration to capture your model changes:

bash: alembic revision --autogenerate -m "Description of changes"
Apply Migrations:

Apply the generated migration to update the database schema:

bash: alembic upgrade head

**Debugging**
For debugging purposes, you can use the built-in Python debugger (pdb) by adding pdb.set_trace() at the beginning of any function you want to debug. Run the application, and it will pause at the breakpoints, allowing you to step through the code and inspect variables.

**Contributing**
Contributions to this project are welcome! Feel free to open issues or pull requests on the GitHub repository.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**ScreenShots**
image
image
image
image
