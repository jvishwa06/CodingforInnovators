from groq import Groq
from tkinter import *
from tkinter import ttk
import dotenv
import os
dotenv.load_dotenv()
api_keye = os.getenv('GROQ_API_KEY')

root = Tk()
root.geometry('1020x720')
root.title('GROQ Chatbot')

root.config(padx=20, pady=20)

def func():
    "Function to process user input and display result"
    prompt = name1.get()  
    
    if not prompt.strip():
        result.config(text="Please enter a query.")
        return

    client = Groq(
        api_key=api_keye,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    temp = chat_completion.choices[0].message.content
    result.config(text=temp)


heading = Label(root, text='GROQ Chatbot', font=("Helvetica", 24, "bold"))
heading.pack(pady=10)

slot1 = Label(root, text="Enter Query:", font=("Helvetica", 14))
slot1.pack(pady=5)

input_frame = Frame(root)
input_frame.pack(pady=10)

name1 = Entry(input_frame, font=("Helvetica", 14), width=50, borderwidth=2, relief="solid")
name1.pack(side="left", padx=5, pady=10)

bt = Button(input_frame, text="Send", height=1, width=5, font=("Helvetica", 14, "bold"), bg='grey', fg="white", relief="raised", command=func)
bt.pack(side="left", padx=5, pady=5)

result_frame = Frame(root, relief="solid", borderwidth=2, width=600, height=150)
result_frame.pack(pady=10)

canvas = Canvas(result_frame)
scrollbar = Scrollbar(result_frame, orient="vertical", command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)

result_display = Frame(canvas)

canvas.create_window((0, 0), window=result_display, anchor="nw")

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

result_display.bind("<Configure>", on_frame_configure)

result = Label(result_display, text='Your result will appear here...', font=("Helvetica", 12), wraplength=580, justify="left", padx=10, pady=10)
result.pack()

root.mainloop()
