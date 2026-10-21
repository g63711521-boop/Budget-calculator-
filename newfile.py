import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        income = float(entry_income.get() or 0)
        bills = float(entry_bills.get() or 0)
        savings = float(entry_savings.get() or 0)
        food = float(entry_food.get() or 0)
        fun = float(entry_fun.get() or 0)
        
        total_expenses = bills + savings + food + fun
        balance = income - total_expenses
        
        lbl_income_res.config(text=f"${income:.2f}")
        lbl_expenses_res.config(text=f"${total_expenses:.2f}")
        lbl_balance_res.config(text=f"${balance:.2f}")
        
        if balance > 0:
            lbl_msg.config(text=f"🎉 Surplus of ${balance:.2f} available to save!", fg="#065f46")
        elif balance == 0:
            lbl_msg.config(text="⚖️ You broke even!", fg="#3730a3")
        else:
            lbl_msg.config(text=f"⚠️ Over budget by ${abs(balance):.2f}", fg="#991b1b")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers only.")

# Create the main app window
app = tk.Tk()
app.title("Personal Budget App")
app.geometry("400x480")
app.config(bg="#f4f7f6")

# Title
title = tk.Label(app, text="Budget Calculator App", font=("Arial", 16, "bold"), fg="#4f46e5", bg="#f4f7f6")
title.pack(pady=15)

# Frame for inputs
frame_inputs = tk.Frame(app, bg="#f4f7f6")
frame_inputs.pack(pady=5)

def add_input(frame, label_text, row):
    lbl = tk.Label(frame, text=label_text, font=("Arial", 10), bg="#f4f7f6")
    lbl.grid(row=row, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(frame, font=("Arial", 10), width=12, justify="right")
    entry.insert(0, "0")
    entry.grid(row=row, column=1, padx=10, pady=5)
    return entry

entry_income = add_input(frame_inputs, "Total Income ($):", 0)
entry_bills = add_input(frame_inputs, "Bills & Subscriptions ($):", 1)
entry_savings = add_input(frame_inputs, "Savings ($):", 2)
entry_food = add_input(frame_inputs, "Food & Snacks ($):", 3)
entry_fun = add_input(frame_inputs, "Entertainment ($):", 4)

# Calculate Button
btn = tk.Button(app, text="Calculate Budget", font=("Arial", 11, "bold"), bg="#4f46e5", fg="white", command=calculate, width=18, relief="flat")
btn.pack(pady=10)

# Summary Frame
frame_summary = tk.Frame(app, bg="#eef2ff", bd=1, relief="solid")
frame_summary.pack(pady=5, padx=20, fill="x")

tk.Label(frame_summary, text="Total Income:", font=("Arial", 10), bg="#eef2ff").grid(row=0, column=0, sticky="w", padx=10, pady=3)
lbl_income_res = tk.Label(frame_summary, text="$0.00", font=("Arial", 10, "bold"), bg="#eef2ff")
lbl_income_res.grid(row=0, column=1, sticky="e", padx=10, pady=3)

tk.Label(frame_summary, text="Total Expenses:", font=("Arial", 10), bg="#eef2ff").grid(row=1, column=0, sticky="w", padx=10, pady=3)
lbl_expenses_res = tk.Label(frame_summary, text="$0.00", font=("Arial", 10, "bold"), bg="#eef2ff")
lbl_expenses_res.grid(row=1, column=1, sticky="e", padx=10, pady=3)

tk.Label(frame_summary, text="Net Balance:", font=("Arial", 10, "bold"), bg="#eef2ff").grid(row=2, column=0, sticky="w", padx=10, pady=5)
lbl_balance_res = tk.Label(frame_summary, text="$0.00", font=("Arial", 10, "bold"), bg="#eef2ff")
lbl_balance_res.grid(row=2, column=1, sticky="e", padx=10, pady=5)

lbl_msg = tk.Label(app, text="Fill in numbers and click Calculate!", font=("Arial", 9, "bold"), bg="#f4f7f6", fg="#555")
lbl_msg.pack(pady=10)

app.mainloop()
