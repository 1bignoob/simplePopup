import tkinter as tk
import webbrowser

# Function to start moving the window
def start_move(event):
    global x_offset, y_offset
    x_offset = event.x
    y_offset = event.y

# Function to move the window
def move_window(event):
    x = event.x_root - x_offset
    y = event.y_root - y_offset
    root.geometry(f"+{x}+{y}")

# Function to quit the application
def quit_application():
    root.destroy()

# Function to open Amazon.com
def open_amazon():
    webbrowser.open("https://www.amazon.com")

# Function to self-destruct the application
def self_destruct(count=3):
    if count == 3:
        self_destruct_button.config(state=tk.DISABLED)  # Disable the button at the start of the countdown
        open_button.config(state=tk.DISABLED)  # Disable the 'Open Amazon' button
    if count > 0:
        self_destruct_button.config(text=f"Self-destructing in ({count})")
        root.after(1000, self_destruct, count-1)
    else:
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Example")
root.geometry("250x125")
root.configure(bg="lightblue")
root.attributes("-topmost", True)  # Bring window to the front
root.overrideredirect(True)  # Remove window border

# Center the window horizontally and set vertical position to 100
window_width = 250
window_height = 125
screen_width = root.winfo_screenwidth()
x_coordinate = int((screen_width / 2) - (window_width / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+100")

# Add a frame to allow moving the window
title_bar = tk.Frame(root, bg="#9B9B9B", relief="raised", bd=2)
title_bar.pack(fill=tk.X)

# Add a label to the title bar for better visibility
title_label = tk.Label(title_bar, text="Example", bg="#9B9B9B", fg="white")
title_label.pack(side=tk.LEFT, padx=10)

# Bind the start_move and move_window functions to the title bar
title_bar.bind("<Button-1>", start_move)
title_bar.bind("<B1-Motion>", move_window)

# Add a Self-Destruct button
self_destruct_button = tk.Button(root, text="Self-Destruct", command=lambda: self_destruct(3), width=20, height=2)
self_destruct_button.pack(side=tk.BOTTOM, pady=5)

# Add 'Open Amazon.com' button
open_button = tk.Button(root, text="Open Amazon", command=open_amazon, width=20, height=2)
open_button.pack(side=tk.BOTTOM, pady=5)

# Start the Tkinter event loop
root.mainloop()