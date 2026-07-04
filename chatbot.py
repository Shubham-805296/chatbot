import tkinter as tk
from tkinter import scrolledtext
import time
import threading

# -------------------------------
# Chatbot Logic
# -------------------------------
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

# -------------------------------
# Message Handling
# -------------------------------
def send_message(event=None):
    user_input = entry.get()
    if user_input.strip() != "":
        insert_message("You", user_input, "user")
        entry.delete(0, tk.END)
        show_typing_indicator()
        threading.Thread(target=bot_reply, args=(user_input,)).start()

def bot_reply(user_input):
    time.sleep(1.2)  # simulate typing delay
    response = get_response(user_input)
    hide_typing_indicator()
    insert_message("Bot", response, "bot")

def insert_message(sender, message, tag):
    timestamp = time.strftime("%H:%M")
    chat_window.insert(tk.END, f"{sender}: {message}\n", tag)
    chat_window.insert(tk.END, f"   {timestamp}\n", "time")
    chat_window.see(tk.END)

def show_typing_indicator():
    typing_label.config(text="Bot is typing...")

def hide_typing_indicator():
    typing_label.config(text="")

# -------------------------------
# UI Setup
# -------------------------------
root = tk.Tk()
root.title("Attractive Chatbot")
root.geometry("900x700")
root.config(bg="#FFFFFF")  # Clean white background

# Header
header_frame = tk.Frame(root, bg="#4A90E2")
header_frame.place(relx=0, rely=0, relwidth=1, height=60)

header_label = tk.Label(header_frame, text="🤖 Chatbot", bg="#4A90E2", fg="white",
                        font=("Arial", 18, "bold"))
header_label.pack(side=tk.LEFT, padx=20, pady=10)

# Chat Window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD,
                                        font=("Arial", 13), bg="#FFFFFF", fg="black", bd=0)
chat_window.tag_config("user", foreground="white", background="#4A90E2",
                       spacing3=12, lmargin1=10, rmargin=150)
chat_window.tag_config("bot", foreground="black", background="#E0E0E0",
                       spacing3=12, lmargin1=150, rmargin=10)
chat_window.tag_config("time", foreground="#999999", font=("Arial", 9, "italic"))
chat_window.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.7)

# Typing Indicator
typing_label = tk.Label(root, text="", bg="#FFFFFF", fg="#666666", font=("Arial", 11, "italic"))
typing_label.place(relx=0.02, rely=0.83)

# Entry Frame (smaller height)
entry_frame = tk.Frame(root, bg="#FFFFFF")
entry_frame.place(relx=0.02, rely=0.87, relwidth=0.96, relheight=0.06)

entry = tk.Entry(entry_frame, font=("Arial", 13),
                 bg="#F7F7F7", fg="black", bd=1, relief="solid")
entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=3)

send_button = tk.Button(entry_frame, text="Send", command=send_message,
                        font=("Arial", 11, "bold"), bg="#4A90E2", fg="white")
send_button.pack(side=tk.RIGHT, padx=5, pady=3)

# Bind Enter Key
root.bind("<Return>", send_message)

# -------------------------------
# Run Application
# -------------------------------
root.mainloop()
