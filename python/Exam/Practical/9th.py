#Create a simple GUI application using tkinter
import tkinter as tk

def display_text():
    """Function to update the label with the text from the entry field."""
    user_input = entry.get()  # Get the text from the entry field
    label.config(text=f"You entered: {user_input}")  # Update the label

# Create the main window
root = tk.Tk()
root.title("Simple GUI Application")  # Set the window title
root.geometry("300x200")  # Set the window size

# Create a label
label = tk.Label(root, text="Enter something:", font=("Arial", 14))
label.pack(pady=10)  # Add some vertical padding

# Create an entry field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)  # Add some vertical padding

# Create a button
button = tk.Button(root, text="Submit", command=display_text, font=("Arial", 14))
button.pack(pady=10)  # Add some vertical padding

# Start the GUI event loop
root.mainloop()