import tkinter as tk
from tkinter import ttk, messagebox
from sympy import symbols, laplace_transform, inverse_laplace_transform, Heaviside
from sympy.parsing.sympy_parser import parse_expr

t, s = symbols('t s', real=True)

def compute_transform():
    try:
        expr_str = input_box.get()
        expr = parse_expr(expr_str.replace("^", "**"), {"t": t, "s": s})

        if transform_choice.get() == "Laplace":
            result, _, _ = laplace_transform(expr, t, s)
        else:
            result = inverse_laplace_transform(expr, s, t).simplify()
            result = result.replace(Heaviside(t), 1)

        output_box.config(state="normal")
        output_box.delete(0, tk.END)
        output_box.insert(0, str(result))
        output_box.config(state="readonly")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")

root = tk.Tk()
root.title("Laplace Transform Calculator")
root.geometry("400x200")

transform_choice = ttk.Combobox(root, values=["Laplace", "Inverse Laplace"])
transform_choice.set("Laplace")
transform_choice.pack(pady=5)

input_label = tk.Label(root, text="Enter function:")
input_label.pack()
input_box = tk.Entry(root, width=50)
input_box.pack(pady=5)

compute_button = tk.Button(root, text="Compute", command=compute_transform)
compute_button.pack(pady=10)

output_label = tk.Label(root, text="Result:")
output_label.pack()
output_box = tk.Entry(root, width=50, state="readonly")
output_box.pack(pady=5)

root.mainloop()
