📋 Overview
A Python-based voice-controlled AI assistant named "JARVIS" that responds to voice commands, opens websites, and answers questions using OpenRouter's AI models.

✨ Features
🎤 Voice Recognition - Listens for wake word "Jarvis"

🗣️ Text-to-Speech - Responds verbally using pyttsx3

🌐 Website Control - Opens Google, Facebook, YouTube, GitHub, etc.

🤖 AI Integration - Answers questions via OpenRouter API (Gemini/Claude models)

⏰ Basic Functions - Tells time and date

🛠️ Prerequisites
Python 3.7+

Working microphone

Internet connection

OpenRouter API key (free tier available)

📦 Installation
1. Clone/Download the Project
bash
# Create project folder
mkdir JARVIS-Assistant
cd JARVIS-Assistant
2. Create Virtual Environment
bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux  
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies
bash
pip install speechrecognition pyttsx3 requests python-dotenv webbrowser
4. Get OpenRouter API Key
Visit OpenRouter.ai

Sign up with Google/GitHub

Go to Keys section

Click Create Key

Copy the key immediately

5. Create .env File

Add your API KEY there for security dont directly use it in the code


How to Use
Say "Jarvis" to activate

Wait for "Yes Sir! How can I help you?"

Give your command:

"Open Google" - Opens Google

"What is Python?" - AI answers

"What time is it?" - Current time

"Exit" - Closes program
