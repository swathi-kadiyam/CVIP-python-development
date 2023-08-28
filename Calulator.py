import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.history = []  # List to store calculation history
        self.create_ui()

    def create_ui(self):
        # Entry widget to display the input and output
        self.entry = tk.Entry(self.root, width=25, font=("Helvetica", 20), bg="blue", fg="white")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Common styles for buttons
        btn_style = {"width": 4, "height": 1, "font": ("Helvetica", 16), "bd": 4, "relief": tk.GROOVE, "bg": "pink"}

        # Calculator buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0),  # Clear button
            ('AC', 5, 1), # All Clear button
            ('%', 5, 2),  # Percentage button
            ('History', 5, 3),  # History button
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, **btn_style, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky='nsew')

        # Make rows and columns expand with window resizing
        for i in range(6):  # 6 rows
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4 columns
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.entry.get())
                full_expression = self.entry.get() + " = " + str(result)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.add_to_history(full_expression)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == 'C':
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text[:-1])  # Remove the last character
        elif value == 'AC':
            self.entry.delete(0, tk.END)  # Clear the entire content
        elif value == '%':
            try:
                result = eval(self.entry.get()) / 100
                full_expression = self.entry.get() + " = " + str(result)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.add_to_history(full_expression)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == 'History':
            self.show_history_page()
        else:
            self.entry.insert(tk.END, value)

    def add_to_history(self, expression):
        # Add the calculation history to the list
        self.history.append(expression)

    def show_history_page(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")

        history_listbox = tk.Listbox(history_window, width=50, height=10, font=("Helvetica", 14))
        history_listbox.pack(padx=20, pady=20)

        # Populate the history listbox with the actual calculation history
        for item in self.history:
            history_listbox.insert(tk.END, item)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()