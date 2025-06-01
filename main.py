import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
from gemini import generate_response
import os

def play_response():
    # reading prompt from entry
    try:
        prompt = entry.get()
    except Exception as e:
        print(f"Could not get the prompt from Entry: {e}")
        exit()

    # generating response Gemini LLM via api call
    try:
        if not entry.get():
            messagebox.showinfo("Entry Empty", "Entry cannot be empty")
            return
        print("Generating response from Gemini")
        print(f"Prompt: {prompt}")
        text = generate_response(prompt)
        print(text)
        print("---------------------------------------")
    except Exception as e:
        print(f"Error generating response from Gemini: {e}")
        exit()
    else:
        print("Response generated successfully")

    # saving the response as speech
    language = 'en'
    try:
        output = gTTS(text=text, lang=language, slow=False)
        output.save("output.mp3")
    except Exception as e:
        print(f"gTTS related error occurred: {e}")
        exit()

    # playing speech
    try:
        os.system('afplay output.mp3')
    except Exception as e:
        print(f"Unable to play output.mp3: {e}")


window = tk.Tk()
window.title("Ask Gemini")
entry = tk.Entry(window)
entry.grid(row=0, columnspan=10)

button = tk.Button(window,text="Get Response", command=play_response)
button.grid(row=1, column=1)
window.mainloop()
