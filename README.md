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

LitBuddy uses the **OpenDyslexic font**, high-contrast themes, and spaced text to reduce visual stress and improve readability.

---

## 🖥️ Installation (Windows)

LitBuddy is distributed as a split ZIP archive due to GitHub’s file size limits.

### ✅ Quick Setup

1. Go to the [LitBuddy for Windows 1–3 Release](https://github.com/ttehsec/LitBuddy/releases/tag/4Windows)
2. Download all `.zip` parts and the `restore.bat` file
3. Place them in the same folder
4. Double-click `restore.bat` to rebuild `LitBuddy.zip`
5. Extract the ZIP and run `LitBuddy.exe`

---

## 🐧 Installation (Linux / Kali)

If you're using Kali or another Linux distro:

```bash
git clone https://github.com/ttehsec/LitBuddy.git
cd LitBuddy
python3 LitBuddy.py
