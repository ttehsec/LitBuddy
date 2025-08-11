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

LitBuddy is distributed as split ZIP files due to GitHub’s file size limits.

### ✅ Step-by-Step

1. **Download all the following files** from the repository:
   - `LitBuddy.zip.part_aa`
   - `LitBuddy.zip.part_ab`
   - `LitBuddy.zip.part_ac` (and so on)
   - `rebuild_zip.bat`

2. **Place all files in the same folder** on your Windows machine.

3. **Double-click** `rebuild_zip.bat`  
   This will combine the parts into `LitBuddy.zip`.

4. **Right-click** `LitBuddy.zip` → **Extract All**

5. **Open** the extracted folder and **double-click** `LitBuddy.exe` to launch the app.

---

## 🐧 Installation (Linux / Kali)

If you're using Kali or another Linux distro:

1. **Clone the repository**
   ```bash
   git clone https://github.com/ttehsec/LitBuddy.git
   cd LitBuddy/dist
