# PlayMate
A simple voice-enabled chatbot powered by Google Gemini AI and integrated with YouTube search and playback. It allows users to interact with the chatbot using voice commands or text input, making it a seamless and interactive experience.

## 📂 Project Structure
📂 PlayMate  
 ┣ 📂 utils  
 ┃ ┣ 📜 ai_utils.py  
 ┃ ┣ 📜 speech_utils.py  
 ┃ ┣ 📜 youtube_utils.py  
 ┣ 📜 .env  
 ┣ 📜 app.py  
 ┣ 📜 requirements.txt  
 ┣ 📜 setup.py  
 ┣ 📜 README.md  
 ┣ 📜 .gitignore  

## ✨ Features
✅ Voice input using microphone.  
✅ AI-powered responses using Google Gemini.  
✅ Search and play YouTube videos directly.  

### 📌 **Working**
1. **`app.py`**: The main entry point for the application. Handles the Chainlit UI and processes user input.
2. **`speech_utils.py`**: Handles speech recognition using the `speechrecognition` library.
3. **`ai_utils.py`**: Generates AI responses using the Google Gemini API.
4. **`youtube_utils.py`**: Searches and plays YouTube videos using `pytube`.