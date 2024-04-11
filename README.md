# Financial Tracker
#### **Quick note:**
<font color="#FF0000">this project was my final project for CS50P course.</font>

#### Description:
The Financial Tracker App is a user-friendly application designed to assist individuals in managing their finances effectively. It offers a simple yet comprehensive platform for tracking income, expenses, and overall financial status. With intuitive features and a clean interface, users can gain better control over their finances and make informed decisions regarding their money management.

## Features:
- **Income and Expense Tracking:** Users can effortlessly input their income and expenses, categorizing them based on predefined categories such as card, savings, and cash. This feature enables users to keep a detailed record of their financial transactions.
- **Visual Representation of Financial Data:** The app provides visual representations of the user's financial data, including total balance, individual category balances, and total expenses. These visualizations offer insights into spending patterns and help users identify areas where they can optimize their finances.
- **Transaction Logging:** Every transaction made by the user is logged with a timestamp, providing a comprehensive history of all financial activities. This feature allows users to track their financial journey over time and review past transactions as needed.
- **Deposit and Withdrawal Functionality:** Users can deposit funds into their chosen category or withdraw funds from it, with each transaction reflected in real-time. This flexibility allows users to manage their cash flow effectively and make adjustments to their budget as required.

## File Descriptions:
- **main.py:** Contains the main code for the Financial Tracker App, including GUI setup, data loading, and transaction processing functions.
- **transactions-log.csv:** Stores the log of all transactions made by the user, including the date, time, and nature of each transaction.
- **amount_of_money.csv:** Stores the initial and updated financial data, including the balance for each category and the total expense.

## Design Choices:
- **GUI Interface:** The app utilizes Tkinter for its graphical user interface, offering a simple and intuitive layout for users to interact with. The clean design enhances user experience and ensures easy navigation throughout the application.
- **CSV Data Storage:** Financial data is stored in CSV files for easy access and manipulation, allowing users to view and edit their data outside of the app if needed. This choice of storage format ensures data integrity and simplifies data management for both users and developers.
- **Real-Time Updates:** The app updates the display and saves data in real-time after each transaction, ensuring that users always have the most up-to-date information at their fingertips. This real-time functionality enhances the user experience and provides immediate feedback on financial transactions.

### Important Note:
- **File Naming Convention:**
    - Avoid creating files with the same names as the default data files used by the Financial Tracker App ("amount_of_money.csv" and "transactions-log.csv").
    - Creating files with identical names may cause conflicts and lead to unexpected behavior within the application.

### Using the App:
1. **Inputting Transactions:**
    - Click on the "Deposit" or "Withdraw" buttons to input transactions.
    - Select the category of the transaction (e.g., card, savings, cash).
    - Enter the amount of money to deposit or withdraw.

2. **Viewing Financial Data:**
    - The app displays the current amounts of money in each category (card, savings, cash) and the total balance.
    - Visual representations of financial data provide insights into spending patterns and overall financial status.

3. **Transaction Logging:**
    - Click on the "Display Log" button to view a log of all transactions made, including the date, time, and nature of each transaction.

4. **Real-Time Updates:**
    - All transactions are logged in real-time, ensuring that users have immediate access to up-to-date financial information.

### Troubleshooting:
- If you encounter any issues while using the app, please refer to the error messages displayed on the screen for guidance.
- Ensure that you have entered valid amounts for deposits and withdrawals.
- If the app crashes or behaves unexpectedly, try restarting it or reinstalling it.

## Conclusion:
The Financial Tracker App provides a convenient solution for individuals seeking to manage their finances effectively. With its user-friendly interface, intuitive features, and real-time updates, the app empowers users to take control of their money and make informed financial decisions. Whether tracking daily expenses, monitoring income, or planning for the future, this app offers the tools and insights needed to achieve financial goals. Download the Financial Tracker App today and start your journey towards financial success!


