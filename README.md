# Bank App Project

## Overview
A Python-based bank application simulating real-world banking operations. The app supports user account creation, deposits, withdrawals, and balance inquiries, with error handling, inheritance, and memory storage implemented.

## Features
- **Object-Oriented Programming (OOP):**
  - Base class `BankAccount`.
  - Inheritance used for `SavingsAccount` and `InterestRewardAccount`.
- **Error Handling:**
  - Custom exceptions: `BalanceException` and `InvalidInput`.
- **Control Flow:**
  - User interaction through input-based prompts.
- **Data Storage:**
  - In-memory storage using Python dictionaries for accounts.
- **Detailed User Flow:**
  - Seamless experience for both new and returning users.

## Technology Stack
- **Programming Language:** Python
- **Modules Used:**
  - Built-in: `os`, `sys`
  - Custom classes: `BankAccount`, `SavingsAccount`, `InterestRewardAccount`, `Bank`
- **Development Tools:**
  - Python 3.x
  - Git/GitHub for version control

## How to Run
1. Clone the repository:
   ```bash
   git clone git@github.com:legendyen/bank_app.git
   cd bank_app

2. Run the app:
   ```bash
   python main.py

## Usage
1. New User Flow
- Ask for client information
- Provide selection to open a savings or interest reward account.
- Perform initial deposits.

![image](https://github.com/user-attachments/assets/a5b9cfbf-dc85-4b92-98f6-55572503b6cf)

2. Trasaction Validation (Include Error Handling)
- Check if input value is positive.
- Check if witdrawal is less than balance amount.
- Perform deposits and withdrawals.

![image](https://github.com/user-attachments/assets/9a2b0880-2fd1-41d3-bca7-b9fd7d15e3a8)

3. Returning User Flow:
- Send user back to main menu.
- Retrieve account details or continue banking.

![image](https://github.com/user-attachments/assets/3f1d80d2-450c-4247-9b3d-e3da1c359aa4)

## GUI Interface
- Welcom page
![image](https://github.com/user-attachments/assets/e3853868-77e6-410b-83d0-f6422d22a0af)
- Create an account
![image](https://github.com/user-attachments/assets/0a67b326-1aa7-463c-b865-72571e45f54e)
- Deposit/Withdraw
![image](https://github.com/user-attachments/assets/304e3c2e-d56c-4c03-bf40-1fba3e776d00)
- Overdrawn hadling
![image](https://github.com/user-attachments/assets/daf90333-3025-4ca2-9f31-931c673d6f45)
- Invalid inpuy
![image](https://github.com/user-attachments/assets/2953bca0-d5a7-40b3-9702-6fd2c851b09a)
![image](https://github.com/user-attachments/assets/b511d7ff-734a-42ef-a235-18df68873991)
- Log in to check amount.
![image](https://github.com/user-attachments/assets/7272e211-5daa-4d50-b2e2-729778cfb21d)

## Future Enahancement
1. Add a database for persistent storage. (Currenlty using in-memory Python storage)
2. Add a search algorithm (e.g., binary search) could be used to quickly find an account by name.


   
