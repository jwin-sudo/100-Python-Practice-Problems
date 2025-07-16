'''
Exercise 98: Solution

Exercise for reference: 

Create a program that asks the user to submit a string or number through a graphical user interface (GUI), and that string or number is stored as a new line in an existing text file. Please have three buttons: Add Line , Save Changes , and Save and Close .
'''

import tkinter as tk
from tkinter import messagebox
import os
class TextFileEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text File Editor")
        
        self.text_area = tk.Text(master, height=10, width=50)
        self.text_area.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Line", command=self.add_line)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(master, text="Save Changes", command=self.save_changes)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.close_button = tk.Button(master, text="Save and Close", command=self.close_editor)
        self.close_button.pack(side=tk.LEFT, padx=5)

    def add_line(self):
        line = self.text_area.get("1.0", tk.END).strip()
        if line:
            with open('textfile.txt', 'a') as file:
                file.write(line + '\n')
            self.text_area.delete("1.0", tk.END)
            messagebox.showinfo("Success", "Line added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter a line to add.")

    def save_changes(self):
        with open('textfile.txt', 'w') as file:
            content = self.text_area.get("1.0", tk.END).strip()
            file.write(content + '\n')
        messagebox.showinfo("Success", "Changes saved successfully!")

    def close_editor(self):
        self.save_changes()
        self.master.destroy()   
if __name__ == "__main__":
    if not os.path.exists('textfile.txt'):
        with open('textfile.txt', 'w') as file:
            pass  # Create the file if it doesn't exist
    root = tk.Tk()
    editor = TextFileEditor(root)
    root.mainloop()
'''This code creates a simple GUI application using Tkinter that allows users to add lines to a text file, save changes, and close the editor. The text file is created if it does not already exist.
'''