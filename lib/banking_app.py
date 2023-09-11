import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Account, Transaction, Base

DATABASE_URL = 'sqlite:///bank.db'
engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Banking CLI Application"""

@cli.command()
def main_menu():
    """Main menu options"""
    
    while True:
        click.clear()
        click.echo("Main Menu:")
        click.echo("Option 1: Add user")
        click.echo("Option 2: Log in to a specific user")
        click.echo("Option 3: View all users")
        click.echo("Option 0: Exit")
        choice = click.prompt("Enter your choice (0-3)", type=int)

        if choice == 1:
            add_user()
        elif choice == 2:
            logged_in_user = login()
            if logged_in_user:
                user_menu(logged_in_user)
        elif choice == 3:
            view_all_users()
        elif choice == 0:
            click.echo("Exiting the application. Goodbye!")
            break
        else:
            click.echo("Invalid choice. Please select a valid option.")

def add_user():
    """Create a new user with name, email, address, and pin"""
    
    session = Session()
    name = click.prompt("Enter your name")
    email = click.prompt("Enter your email")
    address = click.prompt("Enter your address")
    pin = click.prompt("Enter your PIN", hide_input=True)
    
    new_user = User(name=name, email=email, address=address, pin=pin)
    
    session.add(new_user)
    session.commit()
    click.echo(f"User {new_user.name} added with user_id {new_user.user_id}")
    session.close()

def login():
    """Log in to a specific user account"""
    
    session = Session()
    email = click.prompt("Enter your email")
    pin = click.prompt("Enter your PIN", hide_input=True)
    
    user = session.query(User).filter_by(email=email, pin=pin).first()
    
    if user:
        click.echo(f"Logged in as {user.name}")
        return user
    else:
        click.echo("Invalid credentials. Please try again.")
        return None

def view_all_users():
    """Show a list of all users (without their pins)"""
    
    session = Session()
    users = session.query(User).all()
    
    click.echo("All Users:")
    for user in users:
        click.echo(f"User ID: {user.user_id}, Name: {user.name}, Email: {user.email}, Address: {user.address}")
    session.close()

def user_menu(logged_in_user):
    """User menu options after login"""
    
    while True:
        click.clear()
        click.echo(f"Logged in as {logged_in_user.name}")
        click.echo("User Menu:")
        click.echo("Option 1: Deposit")
        click.echo("Option 2: Withdraw")
        click.echo("Option 3: Transfer")
        click.echo("Option 4: Log out")
        choice = click.prompt("Enter your choice (1-4)", type=int)

        if choice == 1:
            deposit(logged_in_user)
        elif choice == 2:
            withdraw(logged_in_user)
        elif choice == 3:
            transfer(logged_in_user)
        elif choice == 4:
            click.echo("Logging out.")
            break
        else:
            click.echo("Invalid choice. Please select a valid option.")

def deposit(logged_in_user):
    """Make a deposit into the logged-in user's account"""
    
    session = Session()
    amount = click.prompt("Enter the deposit amount", type=float)

    if logged_in_user.accounts:
        account = logged_in_user.accounts[0]  # Assuming the user has only one account
        deposit_transaction = Transaction(account_id=account.account_id, transaction_type="deposit", amount=amount)

        account.balance += amount

        session.add(deposit_transaction)
        session.commit()

        click.echo(f"Deposited ${amount} into your account.")
    else:
        click.echo("No accounts found for the logged-in user.")
    session.close()

def withdraw(logged_in_user):
    """Withdraw cash from the logged-in user's account"""
    
    session = Session()
    amount = click.prompt("Enter the withdrawal amount", type=float)

    if logged_in_user.accounts:
        account = logged_in_user.accounts[0]  
        if account.balance >= amount:
            withdrawal_transaction = Transaction(account_id=account.account_id, transaction_type="withdrawal", amount=amount)

            account.balance -= amount

            session.add(withdrawal_transaction)
            session.commit()

            click.echo(f"Withdrew ${amount} from your account.")
        else:
            click.echo("Insufficient balance. Withdrawal failed.")
    else:
        click.echo("No accounts found for the logged-in user.")
    session.close()

def transfer(logged_in_user):
    """Transfer funds to another user"""
    
    session = Session()
    recipient_account_id = click.prompt("Enter the recipient's account ID", type=int)
    amount = click.prompt("Enter the transfer amount", type=float)

    recipient_account = session.query(Account).filter_by(account_id=recipient_account_id).first()

    if recipient_account:
        if logged_in_user.accounts:
            source_account = logged_in_user.accounts[0]  # Assuming the user has only one account
            if source_account.balance >= amount:
                transfer_out_transaction = Transaction(account_id=source_account.account_id, transaction_type="transfer_out", amount=amount)
                transfer_in_transaction = Transaction(account_id=recipient_account.account_id, transaction_type="transfer_in", amount=amount)

                source_account.balance -= amount
                recipient_account.balance += amount

                session.add_all([transfer_out_transaction, transfer_in_transaction])
                session.commit()

                click.echo(f"Transferred ${amount} to account {recipient_account_id}.")
            else:
                click.echo("Insufficient balance. Transfer failed.")
        else:
            click.echo("No accounts found for the logged-in user.")
    else:
        click.echo(f"Recipient account with ID {recipient_account_id} not found. Transfer failed.")
    session.close()

if __name__ == '__main__':
    cli()
