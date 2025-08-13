# 🧠 LitBuddy

**LitBuddy** is a multi-modal literacy and math learning companion designed for children with dyslexia, dysgraphia, and speech-related challenges. Built by a cybersecurity professional for a homeschool educator, LitBuddy integrates text-to-speech, speech-to-text, phonics games, and math challenges into one accessible, offline-friendly platform.

This tool is aligned with accessibility principles recommended by the **International Dyslexia Association (IDA)** and supports a wide range of learning needs through auditory, visual, and interactive reinforcement.

---

## 🎯 Core Modules

LitBuddy is divided into three main learning zones:

### 🔊 Listen
For reading support and auditory reinforcement:
- ✏️ Large-font text input with dyslexia-friendly styling
- 🎧 “Read Aloud” button using offline TTS (pyttsx3)
- 🎚 Adjustable voice and speed settings

### 📝 Write
For handwriting and speech difficulty support:
- 🎤 Speech-to-text input using microphone
- 👀 Visual typing with enlarged letters and high contrast
- 🧠 “Sound It Out” tool to speak typed letters/words

### 🎲 Play
Interactive games to reinforce phonics, spelling, and math skills:

#### 📚 Language Lab
- 🔡 **Select the Word** – Choose correct spelling from options
- 👂 **Audio Challenge** – Hear a word, select matching spelling
- 🧩 **Syllable Snap** – Rearrange syllables to form words
- ⌨️ **Type the Word** – Listen and type the correct word

#### ➕ Math Lab
- ➕ **Add It Up** – Solve addition problems under time pressure
- ➖ **Subtraction Sprint** – Fast-paced subtraction practice
- ✖️ **Multiply Mania** – Reinforce multiplication facts
- 🔢 **Sudoku Challenge** – Visual logic and number sequencing

---

## 🛠️ Accessibility Features

| Challenge             | Supported Features                                                                 |
|----------------------|-------------------------------------------------------------------------------------|
| **Dyslexia**          | ✅ TTS, ✅ Large fonts, ✅ Spaced text, ✅ Colored overlays                          |
| **Dysgraphia**        | ✅ STT, ✅ On-screen keyboard, ✅ Word prediction                                    |
| **Speech Difficulty** | ✅ Visual cueing, ✅ Audio-based phonics games                                      |

- Dyslexia-friendly fonts: Users can toggle dyslexia-friendly fonts within the app. If OpenDyslexic is installed on their system, it will be used automatically; otherwise, Comic Sans MS provides a widely supported fallback.

- High-contrast themes: Designed to reduce visual stress and improve readability.

- Spaced text and clean layout: Supports learners with dyslexia, dysgraphia, and other reading challenges.

---

## 🖥️ Installation (Windows)

LitBuddy is designed to be easy to install and run on any Windows device — no technical experience required.

✅ Quick Setup

1.Install Python 
- Download and install the latest version of Python from python.org. 
- ✅ During installation, make sure to check the box that says “Add Python to PATH.”

2. Install Git for Windows Download and install Git from git-scm.com. ✅ Use the default options during setup.

3. Download LitBuddy
- Right-click on your desktop and choose Git Bash Here
- Run this command to download LitBuddy:
  - git clone https://github.com/ttehsec/LitBuddy.git
- Open the LitBuddy folder that was created

4. Launch LitBuddy
- Right-click on Launch_LitBuddy_Windows.bat
- Choose Run as administrator ✅ This will automatically set up everything and launch the app

---

## 🐧 Installation (Linux / Kali)

If you're using Kali or another Linux distro:

```bash
git clone https://github.com/ttehsec/LitBuddy.git
cd LitBuddy
pip install -r requirements.txt
python3 LitBuddy.py
