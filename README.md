# 🚀 ULTRON v0.4.0 – Local AI Assistant

ULTRON has evolved from a basic voice assistant into an offline AI-powered desktop assistant capable of handling commands, remembering user information, monitoring the system, and answering general questions using a locally running Large Language Model (LLM).

---

## ✨ Features

### 🎤 Voice Interaction
- Voice command support
- Text command support
- Wake word: "Ultorn"
- Conversation Mode
- Auto timeout (30 seconds)

### 🧠 AI Brain
- Offline AI using Ollama
- Llama 3.2 (3B)
- AI fallback for unknown commands
- No internet required for AI responses

### 💾 Smart Memory
- Remember user information
- Recall saved information
- Show all memories
- JSON-based persistent storage

### 💻 System Features
- Open Chrome
- Open VS Code
- Open Notepad
- Open Google
- Open YouTube
- Tell current time
- Tell current date
- Monitor CPU, RAM and Disk usage

### 📋 Logging
- Command history
- Timestamp logging

---

## 🛠️ Technologies Used

- Python 3.12
- SpeechRecognition
- PyAudio
- pyttsx3
- psutil
- Ollama
- Llama 3.2 (3B)
- JSON
- Windows 11

---

## 📂 Project Structure

```
ULTRON/
│
├── data/
├── logs/
├── modules/
│   ├── ai_brain.py
│   ├── commands.py
│   ├── greet.py
│   ├── listen.py
│   ├── logger.py
│   ├── memory.py
│   ├── speak.py
│   └── system_monitor.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🧪 Verified Features

- AI Brain
- Offline AI
- Voice Commands
- Text Commands
- Smart Memory
- System Monitor
- Command Logger
- Conversation Mode

---

## 📌 Current Version

**v0.4.0**

Status:
✅ Stable

---

## 🚀 Upcoming Version (v0.5.0)

- Professional project architecture
- Modular command handlers
- AI + Memory context
- Better AI responses
- More automation capabilities