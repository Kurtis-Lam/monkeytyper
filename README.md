# MonkeyType Automation Scripts: OCR vs. DOM Approaches

This repository contains two distinct automated typing demonstration scripts for [Monkeytype](https://monkeytype.com). Each script showcases a different automation philosophy—one relying on **Computer Vision & Optical Character Recognition (OCR)** with physical keystroke emulation, and the other leveraging **Direct DOM Querying & Selenium Web Driver Automation**.

---

## 📋 Overview & Approach Comparison

| Feature / Aspect | Script 1: Computer Vision & OCR (`ocr_pyautogui.py`) | Script 2: DOM Extraction & Direct Selenium (`dom_selenium.py`) |
| :--- | :--- | :--- |
| **Primary Method** | OpenCV Image Processing + Tesseract OCR | JavaScript DOM Querying (`querySelector`) |
| **Typing Mechanism** | OS-Level Keystrokes (`pyautogui`) | Browser Input Field Direct Injection (`send_keys`) |
| **Accuracy** | Dependent on OCR quality (~90-98%) | Perfect (100% text extraction from DOM) |
| **Execution Speed** | Moderate (character-by-character delay) | Extremely Fast (word-by-word injection) |
| **Dependencies** | OpenCV, Tesseract OCR Engine, PyAutoGUI, Selenium | Selenium, WebDriver Manager |
| **DOM Dependency** | Low (only targets container element) | High (relies on specific DOM CSS classes) |
| **Session Persistence** | Standard temporary session | Persistent Chrome Profile (`user-data-dir`) |

---

## 🔬 Detailed Breakdown

### 1. Vision & OCR Approach (`ocr_pyautogui.py`)

#### How It Works
1. **Browser Initialization**: Launches Google Chrome via Selenium and navigates to MonkeyType.
2. **Container Capture**: Focuses on `#wordsWrapper` and captures a localized screenshot (`monkeytype_words.png`).
3. **Image Preprocessing**: Upscales the image 2x with bicubic interpolation, converts it to grayscale, and applies binary inversion thresholding via OpenCV to maximize contrast for character recognition.
4. **Text Extraction**: Runs Tesseract OCR (`pytesseract`) configured for single-uniform-block text (`--psm 6`) to recognize printed text.
5. **Keystroke Simulation**: Iterates through each extracted character and sends hardware-level keypresses via `pyautogui` with a controlled timing delay.

#### Advantages
* **Decoupled from Internal Web Logic**: Does not rely on reading internal variables, individual word spans, or hidden DOM states to fetch text.
* **Demonstrates Full CV/OCR Pipeline**: Excellent example of integrating real-time image acquisition, image thresholding, OCR extraction, and physical input emulation.
* **Human-like OS Input**: Uses actual simulated keystrokes at the operating system level rather than browser-event injections.

---

### 2. Direct DOM & Selenium Approach (`dom_selenium.py`)

#### How It Works
1. **Persistent Session**: Configures Chrome to use a local user profile directory (`selenium_chrome_profile`), allowing persistent login status, settings, and cookies.
2. **Real-time DOM Querying**: Runs an inline JavaScript query continuously inside the browser:
   ```javascript
   const active = document.querySelector('#words .word.active');
   if (active) return active.textContent;
   const untyped = document.querySelector('#words .word:not(.correct):not(.error)');
   return untyped ? untyped.textContent : null;
   ```
3. **Direct Word Injection**: Passes the exact string directly into Monkeytype's `#wordsInput` element followed by a space.
4. **Instant Progression**: Triggers internal React state updates seamlessly for high-speed typing.

#### Advantages
* **100% Text Accuracy**: Eliminates character misinterpretation entirely by fetching exact text strings straight from the application's DOM tree.
* **Maximum Performance & Speed**: Capable of achieving ultra-high WPM (Words Per Minute) speeds with minimal delay between word submissions.
* **Session & Cookie Retention**: Retains custom Monkeytype themes, user profiles, and preference configurations across executions.
* **No External OCR Installation**: Runs out-of-the-box with standard Python packages without requiring external software like Tesseract binaries.

---

## 🛠️ Prerequisites & Installation

### Option A: Requirements for DOM Approach (`dom_selenium.py`)
```bash
pip install selenium webdriver-manager
```

### Option B: Requirements for OCR Approach (`ocr_pyautogui.py`)
1. **Python Packages**:
   ```bash
   pip install selenium webdriver-manager opencv-python pytesseract pyautogui
   ```
2. **Tesseract-OCR Engine**:
   - Download and install Tesseract binary for Windows (e.g., from UB-Mannheim).
   - Ensure the path in `ocr_pyautogui.py` points to your installed `tesseract.exe`:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Users\<YourUsername>\AppData\Local\Tesseract-OCR\tesseract.exe"
     ```

---

## 🚀 How to Run

1. Run the DOM-based fast script:
   ```bash
   python dom_selenium.py
   ```
2. Run the OCR & Vision-based script:
   ```bash
   python ocr_pyautogui.py
   ```

---

## ⚠️ Educational Disclaimer

> **FOR EDUCATIONAL PURPOSES ONLY**
> 
> The code provided in this repository is intended **strictly for academic, educational, and research purposes** to demonstrate concepts in web automation, Computer Vision (CV), Optical Character Recognition (OCR), and Document Object Model (DOM) interaction techniques.
>
> * **Terms of Service**: Automated interactions with third-party web applications may violate their respective Terms of Service.
> * **Fair Play**: Do not use these scripts to compete on public leaderboards, falsify benchmark scores, or disrupt online typing communities.
> * **Responsibility**: The author accepts no responsibility or liability for account suspensions, bans, or any misuse of these scripts. Use this at your own risk

---

## 📄 License

This application's source code is shared under the **PolyForm Noncommercial License 1.0.0**. 

* **Personal & Educational Use:** Free to use, modify, and explore. You must give credit to the original author.
* **Commercial Use:** If you intend to use this code to earn revenue, build a commercial product, or use it within a business, you **must purchase a commercial license**.

For commercial licensing terms and pricing, please contact me at: `kurtislam100@gmail.com`

---

## 🙌 Acknowledgements

Built with ❤️ by Kurtis.