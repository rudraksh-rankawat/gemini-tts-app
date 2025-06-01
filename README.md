## Gemini Text to Speech Project ##

Built this project to try calling gemini API and getting the response from the prompt. The response recieved than is converted to speech using gTTS (Google Text to Speech). The generated audio file is then played using OS system call (MacOS is my case).

<img width="256" alt="Screenshot 2025-06-01 at 10 59 32 PM" src="https://github.com/user-attachments/assets/57e70776-732b-4bb5-b575-0b3880212638" />

This is powered by simple GUI made with Tkinter.

After Clicking Get Response, you will get the response on the console as well as via speech through your audio output device.

I loved building this project, you can say it as my first GenAI project made by myself (lot more to build ahead).



### Installation

1. **Clone the repo:**

   ```bash
    git clone https://github.com/rudraksh-rankawat/gemini-tts-app.git
    cd gemini-tts-app
   
   ```


2. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
    
3. **Install dependencies:**
    Ensure you have all the necessary Python packages installed.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your Gemini API Key:**
    * Obtain a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
    * Create a file named `.env` in the root directory of your project (same level as `main.py`).
    * Add your API key to the `.env` file in the following format:
        ```
        GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```
        (Replace `YOUR_API_KEY_HERE` with your actual key).

5. **Now run the main.py file (note that if you are on windows or any other OS, "os.system('afplay output.mp3')", replace the right command acc to ur os, I tried install common lib to solve it, but due to some reason it did not work)**
   

