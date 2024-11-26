import tkinter as tk
from tkinter import messagebox
import sys
from database import DBhelper  # Ensure you have DBhelper implemented

class FlipkartGUI:
    
    def __init__(self):
        # Initialize database helper
        self.db = DBhelper()
        self.root = tk.Tk()
        self.root.title("ICTOB")
        self.root.geometry("400x400")
        self.main_menu()
        self.root.mainloop()
        
    def main_menu(self):
        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="ICTOB Reg By Zawad", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Register", font=("Arial", 12), command=self.register).pack(pady=10)
        tk.Button(self.root, text="Login", font=("Arial", 12), command=self.login).pack(pady=10)
        tk.Button(self.root, text="Exit", font=("Arial", 12), command=sys.exit).pack(pady=10)
        
    def register(self):
        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Register", font=("Arial", 16)).pack(pady=10)
        
        # Input fields
        fields = ["Name", "Email", "Phone Number", "Date of Birth", "Division", "District", "Thana", "Village"]
        self.entry_vars = {field: tk.StringVar() for field in fields}
        
        for field in fields:
            tk.Label(self.root, text=f"Enter {field}:", font=("Arial", 12)).pack(pady=5)
            tk.Entry(self.root, textvariable=self.entry_vars[field]).pack(pady=5)
        
        tk.Button(self.root, text="Submit", font=("Arial", 12), command=self.register_user).pack(pady=10)
        tk.Button(self.root, text="Back to Menu", font=("Arial", 12), command=self.main_menu).pack(pady=10)
    
    def register_user(self):
        # Collect inputs
        data = {field: var.get() for field, var in self.entry_vars.items()}
        response = self.db.register(
            data["Name"], data["Email"], data["Phone Number"], data["Date of Birth"],
            data["Division"], data["District"], data["Thana"], data["Village"]
        )
        if response:
            messagebox.showinfo("Success", "Registration Successful!")
        else:
            messagebox.showerror("Error", "Registration Failed.")
        self.main_menu()
    
    def login(self):
        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        
        # Input fields
        tk.Label(self.root, text="Enter Email:", font=("Arial", 12)).pack(pady=5)
        self.login_email = tk.StringVar()
        tk.Entry(self.root, textvariable=self.login_email).pack(pady=5)
        
        tk.Label(self.root, text="Enter Phone Number:", font=("Arial", 12)).pack(pady=5)
        self.login_phone = tk.StringVar()
        tk.Entry(self.root, textvariable=self.login_phone).pack(pady=5)
        
        tk.Button(self.root, text="Login", font=("Arial", 12), command=self.login_user).pack(pady=10)
        tk.Button(self.root, text="Back to Menu", font=("Arial", 12), command=self.main_menu).pack(pady=10)
    
    def login_user(self):
        email = self.login_email.get()
        phone = self.login_phone.get()
        
        # Replace with actual login logic
        response = self.db.login(email, phone)  # Assume this returns True/False
        if response:
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid credentials.")
        self.main_menu()

# Run the application
if __name__ == "__main__":
    FlipkartGUI()
