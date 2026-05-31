import tkinter as tk
from tkinter import messagebox, ttk

from calculations import OPERATIONS, calculate_result, format_number


class ValueCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Value Calculator")
        self.geometry("520x560")
        self.minsize(460, 500)

        self.value_entries = []
        self.operation = tk.StringVar(value="Sum")
        self.result_text = tk.StringVar(value="Enter values, choose a calculation, then press Calculate.")

        self._build_ui()

    def _build_ui(self):
        container = ttk.Frame(self, padding=16)
        container.pack(fill="both", expand=True)

        title = ttk.Label(container, text="Value Calculator", font=("Arial", 18, "bold"))
        title.pack(anchor="w")

        input_frame = ttk.LabelFrame(container, text="Values", padding=12)
        input_frame.pack(fill="x", pady=(14, 12))

        for index in range(10):
            row = index // 2
            column = (index % 2) * 2

            label = ttk.Label(input_frame, text=f"Value {index + 1}")
            label.grid(row=row, column=column, sticky="w", padx=(0, 8), pady=5)

            entry = ttk.Entry(input_frame, width=16)
            entry.grid(row=row, column=column + 1, sticky="ew", padx=(0, 16), pady=5)
            self.value_entries.append(entry)

        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(3, weight=1)

        options_frame = ttk.Frame(container)
        options_frame.pack(fill="x", pady=(0, 12))

        ttk.Label(options_frame, text="Calculation").pack(anchor="w")
        operation_menu = ttk.Combobox(
            options_frame,
            textvariable=self.operation,
            values=OPERATIONS,
            state="readonly",
        )
        operation_menu.pack(fill="x", pady=(4, 0))

        button_frame = ttk.Frame(container)
        button_frame.pack(fill="x", pady=(0, 12))

        calculate_button = ttk.Button(button_frame, text="Calculate", command=self.calculate)
        calculate_button.pack(side="left")

        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear)
        clear_button.pack(side="left", padx=(8, 0))

        output_frame = ttk.LabelFrame(container, text="Output", padding=12)
        output_frame.pack(fill="both", expand=True)

        result_label = ttk.Label(
            output_frame,
            textvariable=self.result_text,
            justify="left",
            wraplength=440,
        )
        result_label.pack(anchor="nw", fill="both", expand=True)

    def calculate(self):
        values = self._get_values()
        if values is None:
            return

        if not values:
            messagebox.showwarning("No values", "Please enter at least one number.")
            return

        calculation = self.operation.get()
        result = calculate_result(calculation, values)

        self.result_text.set(
            f"{calculation}: {format_number(result)}\n\n"
            f"Values used: {len(values)}\n"
            f"Total: {format_number(sum(values))}\n"
            f"Average: {format_number(sum(values) / len(values))}\n"
            f"Minimum: {format_number(min(values))}\n"
            f"Maximum: {format_number(max(values))}"
        )

    def clear(self):
        for entry in self.value_entries:
            entry.delete(0, tk.END)

        self.result_text.set("Enter values, choose a calculation, then press Calculate.")
        self.value_entries[0].focus_set()

    def _get_values(self):
        values = []

        for index, entry in enumerate(self.value_entries, start=1):
            raw_value = entry.get().strip()
            if not raw_value:
                continue

            try:
                values.append(float(raw_value))
            except ValueError:
                messagebox.showerror("Invalid value", f"Value {index} must be a number.")
                entry.focus_set()
                return None

        return values
