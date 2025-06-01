from gtts import gTTS
from gemini import generate_response
import os

#reading prompt from text.txt file
try:
    prompt = open("text.txt", mode="r", encoding='UTF-8').read()
except FileNotFoundError as e:
    print("Error: text.txt not found")
    exit()

#generating response Gemini LLM via api call
try:
    print("Generating response from Gemini")
    text = generate_response(prompt)
except Exception as e:
    print(f"Error generating response from Gemini: {e}")
    exit()
else:
    print("Response generated successfully")

#saving the response as speech
language = 'en'
try:
    output = gTTS(text=text, lang=language, slow=False)
    output.save("output.mp3")
except Exception as e:
    print(f"gTTS related error occurred: {e}")
    exit()

#playing speech
try:
    os.system('afplay output.mp3')
except Exception as e:
    print(f"Unable to play output.mp3: {e}")

