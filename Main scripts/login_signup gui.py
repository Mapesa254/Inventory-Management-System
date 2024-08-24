import tkinter as tk
from tkinter import messagebox
import sqlite3

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")
        
        # Username and Password labels and entries
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Login and Signup buttons
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

        self.signup_button = tk.Button(root, text="Signup", command=self.signup)
        self.signup_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Connect to the SQLite database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Verify if user exists
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login", "Login Successful!")
        else:
            messagebox.showerror("Login", "Invalid Credentials")
        
        conn.close()

    def signup(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Signup")
        signup_window.geometry("300x200")

        # Signup window labels and entries
        signup_username_label = tk.Label(signup_window, text="New Username:")
        signup_username_label.pack()
        signup_username_entry = tk.Entry(signup_window)
        signup_username_entry.pack()

        signup_password_label = tk.Label(signup_window, text="New Password:")
        signup_password_label.pack()
        signup_password_entry = tk.Entry(signup_window, show="*")
        signup_password_entry.pack()

        def register():
            new_username = signup_username_entry.get()
            new_password = signup_password_entry.get()
            
            # Connect to the SQLite database
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()

            # Insert new user into the database
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
            conn.commit()
            conn.close()

            messagebox.showinfo("Signup", "Registration Successful!")
            signup_window.destroy()

        signup_button = tk.Button(signup_window, text="Register", command=register)
        signup_button.pack()

def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Create users table if it doesn't exist
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)''')
    conn.close()
    
    main()
