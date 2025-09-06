

# 🖐️🎤 Gesture and Voice Control System

## 📌 Overview

This project integrates **gesture recognition** (using MediaPipe & OpenCV) and **voice recognition** (using Azure Cognitive Services) to enable **hands-free machine control**. A **Tkinter-based GUI** allows intuitive management of services, while **PyAutoGUI** executes cursor movements and clicks.

The system enhances **Human-Machine Interaction (HMI)** by enabling natural controls through gestures and voice commands.

---

## 🚀 Features

* **Gesture Recognition (MediaPipe + OpenCV)**

  * Detects hand gestures to control cursor and clicks.
* **Voice Recognition (Azure Speech Services)**

  * Recognizes spoken commands and executes them.
* **Tkinter GUI**

  * Easy-to-use interface for starting/stopping services.
* **PyAutoGUI Control**

  * Maps gestures/voice commands to system actions like click, move, etc.
* **Multi-threaded Execution**

  * Gesture and voice recognition run in parallel.

---

## 📂 Project Structure

```
GestureVoiceControl/
│
├── main.py                # Entry point integrating all modules
├── gesture_recognition.py  # MediaPipe + OpenCV for gesture detection
├── voice_recognition.py    # Azure Cognitive Services for speech commands
├── gui.py                  # Tkinter GUI
├── control.py              # PyAutoGUI-based system actions
└── config.py               # Configurations (API keys, thresholds)
```

---

## ⚙️ Requirements

* **Python 3.8+**
* Libraries:

  ```bash
  pip install opencv-python mediapipe pyautogui azure-cognitiveservices-speech tkinter
  ```
* **Azure Speech API Key & Region**
* Webcam & microphone

---

## 🛠️ Setup & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/maheshtamdi/GestureVoiceControl.git
   cd GestureVoiceControl
   ```
2. Add your Azure credentials in `config.py`:

   ```python
   AZURE_KEY = "YOUR_KEY"
   AZURE_REGION = "YOUR_REGION"
   ```
3. Run the system:

   ```bash
   python main.py
   ```
4. Use the GUI to start gesture/voice control.

---

## 📊 Example Actions

* **Gestures:**

  * Index finger up → Cursor click
  * Hand swipe left/right → Cursor move
* **Voice Commands:**

  * "Up" → Cursor moves up
  * "Down" → Cursor moves down
  * "Click" → Mouse click

---

## 📧 Contact

For queries or collaboration, reach out at: **[maheshmeenaa7976@gmail.com](mailto:maheshmeenaa7976@gmail.com)**
