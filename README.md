# 🤖 JARVIS AI Assistant

A Python-based AI Assistant inspired by Tony Stark's JARVIS from Marvel's Iron Man.

## 📌 Project Overview

JARVIS is a voice-controlled personal assistant that can listen to user commands, respond using speech, execute system tasks, and maintain logs of user interactions.

This project is being developed in phases, gradually evolving from a simple voice assistant into an intelligent AI-powered personal assistant.

---

## 🚀 Current Version

### JARVIS v0.2

### Features Implemented

#### Phase 1 - Voice Assistant Foundation

* Voice Recognition using SpeechRecognition
* Text To Speech using pyttsx3
* Greeting System
* Basic Command Processing
* Open Chrome
* Open Notepad
* Modular Project Structure

#### Phase 2 - Wake Word & Utilities

* Wake Word Detection ("Jarvis")
* Open Google
* Open YouTube
* Open VS Code
* Tell Current Time
* Tell Current Date
* Command Logging
* Exit Command

---

## 🛠 Technologies Used

* Python 3.12
* SpeechRecognition
* PyAudio
* pyttsx3
* datetime
* webbrowser
* os

---

## 📂 Project Structure

JARVIS/

├── main.py

├── requirements.txt

├── README.md

├── modules/

│   ├── speak.py

│   ├── listen.py

│   ├── greet.py

│   ├── commands.py

│   └── logger.py

├── logs/

│   └── commands.log

├── data/

└── assets/

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/montylr2722l/JARVIS.git
cd JARVIS
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run JARVIS:

```bash
python main.py
```

---

## 🎤 Example Commands

```text
Jarvis
Open Chrome

Jarvis
Open Google

Jarvis
Open YouTube

Jarvis
Tell Time

Jarvis
Tell Date

Jarvis
Exit
```

---

## 🗺 Roadmap

### Completed

* [x] Voice Recognition
* [x] Text To Speech
* [x] Wake Word Detection
* [x] Open Applications
* [x] Open Websites
* [x] Date & Time Commands
* [x] Command Logging

### Upcoming

* [ ] Memory System
* [ ] System Monitoring
* [ ] AI Chat Integration
* [ ] Face Recognition
* [ ] GUI Dashboard
* [ ] Home Automation
* [ ] Local AI Models
* [ ] Multi-Agent System

---

## 👨‍💻 Author

Vishnu

Engineering Student

Building a real-world AI Assistant inspired by Tony Stark's JARVIS.
