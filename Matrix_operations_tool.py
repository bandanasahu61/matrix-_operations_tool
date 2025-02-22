import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Operations Tool")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Style configuration
        style = ttk.Style()
        style.configure("TButton", padding=5, font=('Arial', 10))
        style.configure("TLabel", padding=5, font=('Arial', 10))

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Matrix size selection
        size_frame = ttk.LabelFrame(main_frame, text="Matrix Size", padding="5")
        size_frame.grid(row=0, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        ttk.Label(size_frame, text="Rows:").grid(row=0, column=0, padx=5)
        self.rows_var = tk.StringVar(value="2")
        self.rows_entry = ttk.Entry(size_frame, textvariable=self.rows_var, width=5)
        self.rows_entry.grid(row=0, column=1, padx=5)

        ttk.Label(size_frame, text="Columns:").grid(row=0, column=2, padx=5)
        self.cols_var = tk.StringVar(value="2")
        self.cols_entry = ttk.Entry(size_frame, textvariable=self.cols_var, width=5)
        self.cols_entry.grid(row=0, column=3, padx=5)

        ttk.Button(size_frame, text="Create Matrices", command=self.create_matrix_inputs).grid(row=0, column=4, padx=10)

        # Matrix input frames
        self.matrix_frame = ttk.LabelFrame(main_frame, text="Matrix Input", padding="10")
        self.matrix_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        # Operations frame
        operations_frame = ttk.LabelFrame(main_frame, text="Operations", padding="5")
        operations_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        operations = [
            ("Add", self.add_matrices),
            ("Subtract", self.subtract_matrices),
            ("Multiply", self.multiply_matrices),
            ("Transpose", self.transpose_matrix),
            ("Determinant", self.calculate_determinant)
        ]

        for i, (text, command) in enumerate(operations):
            ttk.Button(operations_frame, text=text, command=command).grid(row=0, column=i, padx=5, pady=5)

        # Result frame
        self.result_frame = ttk.LabelFrame(main_frame, text="Result", padding="10")
        self.result_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def create_matrix_inputs(self):
        try:
            rows = int(self.rows_var.get())
            cols = int(self.cols_var.get())
            
            if rows <= 0 or cols <= 0:
                raise ValueError("Dimensions must be positive")

            # Clear previous matrix inputs
            for widget in self.matrix_frame.winfo_children():
                widget.destroy()

            # Create Matrix A inputs
            matrix_a_frame = ttk.LabelFrame(self.matrix_frame, text="Matrix A", padding="5")
            matrix_a_frame.grid(row=0, column=0, padx=10, pady=5)
            
            self.matrix_a_entries = []
            for i in range(rows):
                row_entries = []
                for j in range(cols):
                    entry = ttk.Entry(matrix_a_frame, width=5)
                    entry.insert(0, "0")
                    entry.grid(row=i, column=j, padx=2, pady=2)
                    row_entries.append(entry)
                self.matrix_a_entries.append(row_entries)

            # Create Matrix B inputs
            matrix_b_frame = ttk.LabelFrame(self.matrix_frame, text="Matrix B", padding="5")
            matrix_b_frame.grid(row=0, column=1, padx=10, pady=5)
            
            self.matrix_b_entries = []
            for i in range(rows):
                row_entries = []
                for j in range(cols):
                    entry = ttk.Entry(matrix_b_frame, width=5)
                    entry.insert(0, "0")
                    entry.grid(row=i, column=j, padx=2, pady=2)
                    row_entries.append(entry)
                self.matrix_b_entries.append(row_entries)

        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid matrix dimensions")

    def get_matrix_values(self, entries):
        return np.array([[float(entry.get()) for entry in row] for row in entries])

    def display_result(self, result):
        # Clear previous results
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        if isinstance(result, np.ndarray):
            for i in range(result.shape[0]):
                for j in range(result.shape[1]):
                    ttk.Label(self.result_frame, text=f"{result[i,j]:.2f}").grid(row=i, column=j, padx=2, pady=2)
        else:
            ttk.Label(self.result_frame, text=f"Result: {result:.2f}").grid(row=0, column=0)

    def add_matrices(self):
        try:
            matrix_a = self.get_matrix_values(self.matrix_a_entries)
            matrix_b = self.get_matrix_values(self.matrix_b_entries)
            result = matrix_a + matrix_b
            self.display_result(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def subtract_matrices(self):
        try:
            matrix_a = self.get_matrix_values(self.matrix_a_entries)
            matrix_b = self.get_matrix_values(self.matrix_b_entries)
            result = matrix_a - matrix_b
            self.display_result(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def multiply_matrices(self):
        try:
            matrix_a = self.get_matrix_values(self.matrix_a_entries)
            matrix_b = self.get_matrix_values(self.matrix_b_entries)
            result = np.dot(matrix_a, matrix_b)
            self.display_result(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def transpose_matrix(self):
        try:
            matrix_a = self.get_matrix_values(self.matrix_a_entries)
            result = np.transpose(matrix_a)
            self.display_result(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calculate_determinant(self):
        try:
            matrix_a = self.get_matrix_values(self.matrix_a_entries)
            if matrix_a.shape[0] != matrix_a.shape[1]:
                raise ValueError("Matrix must be square to calculate determinant")
            result = np.linalg.det(matrix_a)
            self.display_result(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculator(root)
    root.mainloop()
