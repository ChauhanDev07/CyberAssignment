# 🛡️ Key Logger

## 📘 Overview
  
It captures key input **locally** and sends **search terms or typed text snippets** to a Telegram bot (with prior consent)

> ⚠️ **Disclaimer:**  
> This program is created strictly for educational — with full consent of the user being monitored.  
> Misuse of this software for surveillance or unauthorized tracking is **illegal** and **not endorsed** by this project.

---

## ⚙️ Features

- ⌨️ Detects keyboard input in real time.  
- 🧠 Buffers text until the Enter key is pressed.  
- 📤 Sends typed phrases to a Telegram chat or group for analysis.   
- 🧹 Gracefully handles termination with **Ctrl + C**.

---

## 🧩 Technologies Used

| Technology | Purpose |
|-------------|----------|
| **Python 3.x** | Programming language |
| **keyboard** | Capturing keystrokes |
| **requests** | Telegram API communication |
| **logging**, **signal** | Safe program control |

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/parents-protector.git
cd parents-protector

```

### 2. Install dependencies
```bash
pip install keyboard requests

```

### 3. Configure Telegram Bot
1. Create a bot via **[@BotFather](https://t.me/BotFather)**.  
2. Copy your **BOT_TOKEN**.  
3. Create a **private Telegram group**, add the bot, and get the **CHAT_ID**.  
4. Replace these values in the script:
   ```python
   BOT_TOKEN = "your-bot-token-here"
   CHAT_ID = "your-chat-id-here"
   ```

### 4. Run the program
```bash
pyinstaller --onefile filename.py (To convert in .exe)
```

---

## 🧠 How It Works

1. The script listens for keypresses using the `keyboard` module.  
2. It accumulates keystrokes into a temporary buffer.  
3. When the **Enter** key is pressed, the buffer is sent to the Telegram bot as a message.  
4. All data is also saved locally in **childsafety.txt** for record-keeping.

---

## 🧰 Example Output

**Console:**
```
Starting . Press Ctrl+C to stop.
```

**Telegram Bot Message:**
```
-> how to install games safely
```

---

## 🔒 Ethical Use

✅ Use only on your **own systems** or with **explicit consent**.  
🚫 Do **not** deploy on public or third-party devices.  
🎓 Intended for **educational use only** — such as cybersecurity, parental safety research, or academic submission.

---

## 🧾 License

This project is distributed under the **MIT License** — you are free to modify and use it for **legal and ethical purposes**.

---

## 👨‍🏫 Author

**Dev Singh Chauhan**  
**Shivam Bhagour**  
*Computer Science *
