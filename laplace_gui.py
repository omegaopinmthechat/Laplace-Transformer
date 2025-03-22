import tkinter as tk
from tkinter import ttk, messagebox
from sympy import symbols, laplace_transform, inverse_laplace_transform, Heaviside
from sympy.parsing.sympy_parser import parse_expr

# Define symbols
t, s = symbols('t s', real=True)

def compute_transform():
    try:
        expr_str = input_box.get()
        expr = parse_expr(expr_str.replace("^", "**"), {"t": t, "s": s})

        if transform_choice.get() == "Laplace":
            result, _, _ = laplace_transform(expr, t, s)
        else:
            result = inverse_laplace_transform(expr, s, t).simplify()
            result = result.replace(Heaviside(t), 1)  # Remove Heaviside

        output_box.config(state="normal")  # Enable editing
        output_box.delete(0, tk.END)  # Clear previous result
        output_box.insert(0, str(result))  # Display new result
        output_box.config(state="readonly")  # Disable editing

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Laplace Transform Calculator")
root.geometry("400x200")

# Dropdown for selecting transform type
transform_choice = ttk.Combobox(root, values=["Laplace", "Inverse Laplace"])
transform_choice.set("Laplace")  # Default selection
transform_choice.pack(pady=5)

# Input field
input_label = tk.Label(root, text="Enter function:")
input_label.pack()
input_box = tk.Entry(root, width=50)
input_box.pack(pady=5)

# Compute button
compute_button = tk.Button(root, text="Compute", command=compute_transform)
compute_button.pack(pady=10)

# Output field
output_label = tk.Label(root, text="Result:")
output_label.pack()
output_box = tk.Entry(root, width=50, state="readonly")
output_box.pack(pady=5)

# Run the application
root.mainloop()
