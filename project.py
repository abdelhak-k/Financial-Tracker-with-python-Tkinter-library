import tkinter as tk
from tkinter import messagebox,ttk
import csv
from datetime import datetime

WINDOW_WIDTH = 258
WINDOW_HEIGHT = 480
PATH="amount_of_money.csv"
LOG_PATH="transactions-log.csv"
moneyAmount = {'card': 0, 'savings': 0, 'cash': 0,'expense': 0} #expense should always be in the last column
CATEGORIES=list(moneyAmount)[0:-1] #all the keys except expense


def main():
    root = tk.Tk()
    center_window(root,WINDOW_WIDTH,WINDOW_HEIGHT)
    root.title("Financial Tracker")
    display_amountOfMoney(root)
    display_buttons(root)

    root.mainloop()    

    
def load_data(path):
    """Reads the initial data from a CSV file and returns it as a dictionary.
    
    Args:
        path (str): The path to the file to read the data from.

    Returns:
        dict: A dictionary containing the initial data, with categories as keys and amounts as values.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        ValueError: If the data format is incorrect.
        KeyError: If there is an invalid key in the CSV file.
    """
    
    #we set evry thing to 0
    for key in moneyAmount:
        moneyAmount[key]=0
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    amount = float(row['Amount'])
                    moneyAmount[row['Category'].lower()] += amount
                except ValueError:
                    messagebox.showerror("Error", f"Invalid amount in CSV file: {row['Amount']}")
                    return False
                except KeyError:
                    messagebox.showerror("Error", f"Invalid key {row['Category']}")
                    return False
    except FileNotFoundError:
        raise FileNotFoundError

    return moneyAmount


def display_buttons(root):
    """Displays the Deposit, Withdraw, and Display Log buttons in the GUI.
    
    Args:
        root (tk.Tk): The root window of the GUI.
    """
    
    deposit_button = tk.Button(root, text="Deposit", command=lambda: transaction(root, moneyAmount,"Deposit"))
    deposit_button.pack(side=tk.BOTTOM, pady=10)

    withdraw_button = tk.Button(root, text="Withdraw", command=lambda: transaction(root, moneyAmount,"Withdraw"))
    withdraw_button.pack(side=tk.BOTTOM, pady=10)

    log_button = tk.Button(root, text="Transaction Log", command=lambda: display_log(root))
    log_button.pack(side=tk.BOTTOM, pady=10)


def display_log(root):
    """Displays the transaction log in a new window.
    
    Args:
        root (tk.Tk): The root window of the GUI.
    """
    
    log_window = tk.Toplevel(root)
    log_window.title("log") #setting the name to log
    center_window(log_window,WINDOW_WIDTH*2,WINDOW_HEIGHT) 
    #configure the log as a table
    tree = ttk.Treeview(log_window, columns=("Datetime", "Transaction"), show="headings")
    tree.heading("Datetime", text="Date and time")
    tree.heading("Transaction", text="Transaction")
    tree.pack(fill="both", expand=True)
    
    try:
        log=load_log(LOG_PATH)
    except FileNotFoundError:
        with open(LOG_PATH, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Datetime', 'Transaction'])
            writer.writeheader()
    except KeyError | ValueError as e:
        messagebox.showerror("Error", f"Invalid key/value: {e}")
        log_window.destroy()
        return
    

    for entry in log:
        tree.insert("", "end", values=(entry['Datetime'], entry['Transaction']))

    log_window.grab_set()

    
def load_log(path):
    """Reads the transaction log from a CSV file and returns it as a list of dictionaries.
    
    Args:
        path (str): The path to the file to read the log from.

    Returns:
        list: A list of dictionaries containing log entries.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        ValueError: If the data format is incorrect.
        KeyError: If there is an invalid key in the CSV file.
    """
    
    log_entries = []
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                log_entries.append(row)
    except Exception as e:
        raise e
    
    return log_entries
    
    
def display_amountOfMoney(root):
    """Displays the current amounts of money in the GUI.
    
    Args:
        root (tk.Tk): The root window of the GUI.
    """
    data={'card': 0, 'savings': 0, 'cash': 0,'expense': 0}
    try:
        data = load_data(PATH)
    except FileNotFoundError: #if this happens we should create one
        with open(PATH, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Category', 'Amount'])
            writer.writeheader()
    
    #configure
    canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT/2)
    canvas.pack(padx=50, pady=10, anchor=tk.N)

    total = data['card'] + data['savings'] + data['cash']
    
    #check if we should display the total in red or green
    fill="green"
    if (total<0):
        fill="red"
    canvas.create_text(20, 20, anchor="nw", text=f"Total: {total}", font=("Arial", 12), fill=fill)
    
    #check if we should display the amounts of the CAREGORIES in red or green
    y_pos=50 
    for catogerie in CATEGORIES:
        if (data[catogerie]<0):
            fill="red"
        else:
            fill="green"
        canvas.create_text(20, y_pos, anchor="nw", text=f"{catogerie.title()}: {data[catogerie]}", font=("Arial", 12), fill=fill)
        y_pos+=30 #to change the y position of the text
     
    #expense should always be in red
    canvas.create_text(20, y_pos, anchor="nw", text=f"Expense: {data['expense']}", font=("Arial", 12), fill="red")


def transaction(root, data, transaction_type):
    """Creates a new transaction window for deposit or withdrawal.
    
    Args:
        root (tk.Tk): The root window of the GUI.
        data (dict): A dictionary containing the current amounts of money.
        transaction_type (str): The type of transaction ('Deposit' or 'Withdraw').
    """
    
    transaction_window = tk.Toplevel(root)
    transaction_window.title(transaction_type) #setting the name to either deposit or withdraw
    center_window(transaction_window,158,128)
    #menu of (card,cash,savings) using grid
    tk.Label(transaction_window, text="Category:").grid(row=0, column=0)
    category_var = tk.StringVar(transaction_window)
    category_var.set('card') #the default category
    category_menu = tk.OptionMenu(transaction_window, category_var, *CATEGORIES)
    category_menu.grid(row=0, column=1)
    tk.Label(transaction_window, text="Amount:").grid(row=1, column=0)
    amount_entry = tk.Entry(transaction_window) #the value entered by the user
    amount_entry.grid(row=1, column=1)
    #we choose if the user clicked on Deposit button or Withdraw button
    
    if transaction_type.lower() == 'deposit':
        transaction_button = tk.Button(transaction_window, text="Deposit", command=lambda: process_deposit(root,transaction_window, data, category_var.get(), amount_entry.get()))
    elif transaction_type.lower() == 'withdraw':
        transaction_button = tk.Button(transaction_window, text="Withdraw", command=lambda: process_withdraw(root,transaction_window, data, category_var.get(), amount_entry.get()))
    
    transaction_button.grid(row=2, columnspan=2, pady=10)
    transaction_window.grab_set()


def process_deposit(root,window, data, category, amount):
    """Processes a deposit transaction and updates the GUI.
    
    Args:
        root (tk.Tk): The root window of the GUI.
        window (tk.Toplevel): The transaction window.
        data (dict): A dictionary containing the current amounts of money.
        category (str): The category of the transaction.
        amount (str): The amount of money to deposit.
    """
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
        return

    data[category.lower()] += amount
    messagebox.showinfo("Success", f"Successfully deposited {amount} to {category} 💰")
    #we add the transaction to the log
    DictLine= {"Datetime":datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"Transaction":f"deposited {amount} to {category}"}
    window.destroy()
    #save updated data
    write_data(data,PATH)
    append_data(DictLine,LOG_PATH)
    #update display
    clear_and_reload(root)


def process_withdraw(root,window, data, category, amount):
    """Processes a withdrawal transaction and updates the GUI.
    
    Args:
        root (tk.Tk): The root window of the GUI.
        window (tk.Toplevel): The transaction window.
        data (dict): A dictionary containing the current amounts of money.
        category (str): The category of the transaction.
        amount (str): The amount of money to withdraw.
    """
    try:
        amount = float(amount) #user can enter a string rather than an integer
    except ValueError:
        messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
        return

    data[category.lower()] -= amount
    data['expense'] += amount
    
    messagebox.showinfo("Success", f"Successfully withdrew {amount} from {category} 💰")
    
    window.destroy()
    #save updated data
    write_data(data,PATH)
    #we add the transaction to the log
    DictLine= {"Datetime":datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"Transaction":f"withdrew {amount} from {category}"}
    append_data(DictLine,LOG_PATH)
    #update display
    clear_and_reload(root)


def clear_and_reload(root):
    """Clears the current widgets in the GUI and reloads them with updated data.
    
    Args:
        root (tk.Tk): The root window of the GUI.
    """
    #destroy all the current widgets in the window
    for widget in root.winfo_children():
        widget.destroy()

    #reload the widgets with new data
    display_amountOfMoney(root)
    display_buttons(root)
    

def append_data(DictLine, path):
    """Appends a log entry to the transaction log file.
    
    Args:
        DictLine (dict): A dictionary representing a log entry.
        path (str): The path to the transaction log file.
    """
    
    try:
        with open(path, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Datetime', 'Transaction'])
            if file.tell()==0:
                writer.writeheader()
            writer.writerow(DictLine)
    except FileNotFoundError:
        messagebox.showerror("Error", f"Could not open {path} for saving the log transaction.")


def write_data(data,path):
    """Writes the current amounts of money to a CSV file.
    
    Args:
        data (dict): A dictionary containing the current amounts of money.
        path (str): The path to the file to write the data to.
    """
    try:
        with open(path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Category', 'Amount'])
            writer.writeheader()
            for category, amount in data.items():
                writer.writerow({'Category': category.capitalize(), 'Amount': amount})      

    except FileNotFoundError:
        messagebox.showerror("Error",f"error while oppening {path} for writing data.")



def center_window(window, width, height):
    """Centers a window on the screen.
    
    Args:
        window: The window to center.
        width: The width of the window.
        height: The height of the window.
    """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int((screen_width - width) / 2)
    y_coordinate = int((screen_height - height) / 2)

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
    


if __name__ == "__main__":
    main()
