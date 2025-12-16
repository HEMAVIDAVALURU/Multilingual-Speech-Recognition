# **🎤 Multilingual Speech Recognition & Translation App**

A Python-based desktop application that performs real-time speech recognition and language translation using a simple and interactive Tkinter GUI. The application listens to user speech, converts it into text, and translates it into a selected target language.

The app supports English, Hindi, Telugu, and Tamil, making it useful for multilingual communication and learning.
## **🚀 Features**

Real-time speech-to-text conversion

Instant language translation

User-friendly Tkinter GUI

Supports multiple Indian languages

Error handling for unclear speech

One-click Speak & Translate functionality

## **🛠️ Technologies Used**

Python

Tkinter

SpeechRecognition

Google Speech API

Deep Translator

## **📦 Installation Steps**
### **1️⃣ Prerequisites**

Python 3.8 or above

Working microphone

Internet connection (for Google Speech & Translation APIs)
### **2️⃣ Clone the Repository**
https://github.com/HEMAVIDAVALURU/Multilingual-Speech-Recognition
### **3️⃣ Create a Virtual Environment (Optional but Recommended)**
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

### **4️⃣ Install Required Libraries**
pip install SpeechRecognition deep-translator pyaudio


⚠️ Note for PyAudio Installation (Windows):
If PyAudio fails to install:

Download the compatible .whl file from Unofficial Python Wheels

Install using:

pip install PyAudio-0.2.xx-cp3x-cp3x-win_amd64.whl

### **5️⃣ Run the Application**
python app.py

## **▶️ How to Use**

Select the input language

Select the translation language

Click 🎤 Speak & Translate

Speak into the microphone

View the recognized and translated text

## **📌 Supported Languages**

English

Hindi

Telugu

Tamil

## **📄 Project Structure**
```text
multilingual-speech-translation/
│
├── app.py
├── README.md
└── requirements.txt
```

## **💡 Future Enhancements**

Add more languages

Offline speech recognition support

Text-to-speech output

Mobile application version

## **📜 License**

This project is open-source and available for educational purposes.
