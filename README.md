# 🎙️ Speech-to-Text Transcription System

A web-based Speech-to-Text Transcription System built using **Python and Django**, integrated with the **AssemblyAI API** to convert audio input into readable text.

## 📌 Overview

The Speech-to-Text Transcription System allows users to convert spoken audio into text through an easy-to-use web interface. It uses AssemblyAI's speech recognition capabilities to process audio and generate accurate transcriptions.

The application combines Django for backend development with Python audio-processing libraries to handle audio input and transcription workflows.

## ✨ Features

- **🎧 Audio-to-Text Conversion:** Convert audio recordings into readable text.
- **🌐 AssemblyAI Integration:** Uses the AssemblyAI API for speech recognition and transcription.
- **🎙️ Audio Input:** Supports audio input through the application's interface.
- **🔊 Audio Processing:** Handles audio data using Python audio-processing libraries.
- **📊 Audio Visualization:** Uses Matplotlib for audio signal visualization.
- **📝 Transcription Output:** Displays generated text through the web interface.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| Speech Recognition | AssemblyAI API |
| Audio Processing | PyAudio, Wave, NumPy |
| Data Visualization | Matplotlib |
| Frontend | HTML, CSS, JavaScript |

## 📂 Project Structure

```text
Speech-To-Text-Transcription-System/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
├── static/
├── your_app/
│
└── project/
```

*Note: Replace `your_app` and `project` with your actual Django folder names if they differ.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Speech-To-Text-Transcription-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Speech-To-Text-Transcription-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Configure your AssemblyAI API key and other required settings using environment variables.

Do not upload API keys or private credentials to GitHub.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Start the Development Server

```bash
python manage.py runserver
```

### 9. Open the Application

Visit:

```text
http://127.0.0.1:8000/
```

## 🔄 How It Works

1. **Audio Input:** The user provides audio through the application.
2. **Audio Processing:** Audio data is handled using Python audio-processing libraries.
3. **Speech Recognition:** Audio is processed through the AssemblyAI API.
4. **Transcription:** The API returns the recognized speech as text.
5. **Output:** The generated transcription is displayed through the Django web interface.

## 🔐 Security

- Store API keys in environment variables.
- Never commit `.env` files or private credentials.
- Keep sensitive Django configuration out of public repositories.

## 👨‍💻 Developer

**Sameer Kumar Choudhury**

Computer Science Engineering | Python | Django | AI/ML

## 📄 License

This project is available for educational and learning purposes.