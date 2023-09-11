from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Account, Transaction

DATABASE_URL = 'sqlite:///lib/bank.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
   
    users_data = [
        {"name": "Scar Mkadinali", "email": "mkadinali@example.com", "address": "123 Umoroto", "pin": "1234"},
        {"name": "Sewersydaa", "email": "sewersydaa@example.com", "address": "Ploti 247", "pin": "5678"},
     
    ]

    for user_info in users_data:
        user = User(**user_info)
        session.add(user)
        session.commit()
        print(f"User '{user.name}' created with user_id {user.user_id}")

    
    for user in session.query(User).all():
        account = Account(user_id=user.user_id, balance=1000.00)  # Adjust the initial balance as needed
        session.add(account)
        session.commit()
        print(f"Account created for '{user.name}' with account_id {account.account_id}")

if __name__ == '__main__':
    seed_data()
