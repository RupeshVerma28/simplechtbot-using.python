import tkinter as tk

# Step 2: Chatbot Logic
def get_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a simple chatbot created to help you with basic tasks.",
        "bye": "Goodbye! Have a great day!",
        "rupesh" : "HI DEV"
    }
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I didn't understand that.")

# Step 3: GUI Setup Using Tkinter
# Create the main application window
root = tk.Tk()
root.title("Chatbot")

# Create the text display area
chat_display = tk.Text(root, height=20, width=50, bg="light yellow")
chat_display.pack()

# Create the entry widget where the user types their input
user_input = tk.Entry(root, width=50)
user_input.pack()

# Function to handle sending a message
def send_message():
    user_message = user_input.get()  # Get user input
    chat_display.insert(tk.END, "You: " + user_message + "\n")  # Display user message
    user_input.delete(0, tk.END)  # Clear the input field

    bot_response = get_response(user_message)  # Get chatbot response
    chat_display.insert(tk.END, "Chatbot: " + bot_response + "\n")  # Display chatbot response

# Create the send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Run the main loop of the application
root.mainloop()
