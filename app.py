import tkinter as tk
from scrape import scrape_link


def center_window(root, width=800, height=600):

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f"{width}x{height}+{x}+{y}")


def on_button_click():

    input_text = entry.get()

    result = scrape_link(input_text)

    label.config(text=result)


root = tk.Tk()
root.title("Web Scrapping")


center_window(root)


prompt_label = tk.Label(root, text="Enter a URL:", font=("Arial", 12))
prompt_label.pack(pady=10)


entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=10)


button = tk.Button(root, text="Submit", font=("Arial", 12), command=on_button_click)
button.pack(pady=10)


label = tk.Label(root, text="", font=("Arial", 12))
label.pack(pady=10)


root.mainloop()
