import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("500x600")
        self.root.resizable(False, False)  # Disable resizing window

        # Default theme
        self.is_dark_theme = False

        # Counter to number tasks
        self.task_counter = 1
        
        # Header title and background color
        self.header = tk.Label(self.root, text="Todo List", font=("Helvetica Neue", 24, "bold"), fg="#fff", bg="#4CAF50", pady=10)
        self.header.pack(fill=tk.X)
        
        # Theme toggle button
        self.theme_button = tk.Button(self.root, text="🌙", font=("Helvetica Neue", 12), command=self.toggle_theme, bg="#f4f4f9", fg="#4a4a4a", relief="flat")
        self.theme_button.place(x=440, y=10)  # Adjusted position
        
        # Frame for task input area
        frame = tk.Frame(self.root, bg="#fff", padx=10, pady=5)
        frame.pack(pady=20)
        
        # Entry widget to input new task
        self.entry = tk.Entry(frame, width=25, font=("Helvetica Neue", 12), bg="#f0f0f0", fg="#333", relief="flat", justify="left")
        self.entry.grid(row=0, column=0, padx=5, pady=5)
        
        # Add task button
        add_button = tk.Button(frame, text="➕ Add", font=("Helvetica Neue", 12), bg="#28a745", fg="white", relief="flat", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5, pady=5)
        
        # Task listbox to display tasks
        self.listbox = tk.Listbox(self.root, width=40, height=10, font=("Helvetica Neue", 12), bg="#ffffff", fg="#333", relief="flat", selectbackground="#4CAF50")
        self.listbox.pack(pady=10)
        
        # Buttons for task management (Remove, Delete All)
        button_frame = tk.Frame(self.root, bg="#f5f5f5")
        button_frame.pack(pady=10)
        
        # Remove selected task button
        remove_button = tk.Button(button_frame, text="🗑 Remove", font=("Helvetica Neue", 12), bg="#f76c6c", fg="white", relief="flat", command=self.remove_task)
        remove_button.grid(row=0, column=0, padx=10, pady=5)
        
        # Delete all tasks button
        delete_button = tk.Button(button_frame, text="❌ Delete All", font=("Helvetica Neue", 12), bg="#FF5050", fg="white", relief="flat", command=self.delete_all_tasks)
        delete_button.grid(row=0, column=1, padx=10, pady=5)
        
        # Close app button
        close_button = tk.Button(self.root, text="🛑 Close", font=("Helvetica Neue", 12), bg="#FF5050", fg="white", relief="flat", command=self.close_app)
        close_button.pack(pady=15)

        # Apply the initial theme
        self.apply_theme()  
    
    def add_task(self):
        #Add a new task with a task number
        task = self.entry.get().strip()
        if task:
            # Add task with numbering
            task_with_number = f"{self.task_counter}. {task}"
            self.listbox.insert(tk.END, task_with_number)
            # Increment the task counter
            self.task_counter += 1
            self.entry.delete(0, tk.END)  
        else:
            # Warning if no task is entered
            messagebox.showwarning("Empty Task", "Please enter a task before adding.")  
    
    def remove_task(self):
        #Remove the selected task from the listbox
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
        except IndexError:
            # Warning if no task is selected
            messagebox.showwarning("Warning", "You must select a task.")  
    
    def delete_all_tasks(self):
        #Delete all tasks after confirmation
        if messagebox.askyesno("Confirmation", "Are you sure you want to delete all tasks?"):
            self.listbox.delete(0, tk.END)
            self.task_counter = 1
    
    def toggle_theme(self):
        #Toggle between dark and light themes
        # Switch between themes 
        self.is_dark_theme = not self.is_dark_theme
        self.apply_theme()
    
    def apply_theme(self):
        #Apply the selected theme (dark or light)
        if self.is_dark_theme:
            self.root.configure(bg="#333")
            self.listbox.configure(bg="#444", fg="#fff")
            self.entry.configure(bg="#555", fg="#fff")
            self.theme_button.configure(text="🌞", bg="#666", fg="#fff")
        else:
            self.root.configure(bg="#f1f1f1")  
            self.listbox.configure(bg="#fff", fg="#333")  
            self.entry.configure(bg="#f0f0f0", fg="#333")  
            self.theme_button.configure(text="🌙", bg="#f4f4f9", fg="#4a4a4a")  
    
    def close_app(self):
        #Close the application
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)  # Create and run the app
    root.mainloop()  # Start the Tkinter event loop





    
