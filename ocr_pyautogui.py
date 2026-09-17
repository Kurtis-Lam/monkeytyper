import time
import cv2
import pyautogui
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Point directly to your user AppData Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\KKLam\AppData\Local\Tesseract-OCR\tesseract.exe"

def run_monkeytype_ocr():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get("https://monkeytype.com")
    
    # 1. Wait 5 seconds for manual cookie acceptance
    print("Waiting 5 seconds for manual setup/cookies...")
    time.sleep(5)

    # 2. Target full words container
    words_element = driver.find_element(By.ID, "wordsWrapper")
    
    # 3. JavaScript click to bypass overlay click interception
    driver.execute_script("arguments[0].click();", words_element)
    time.sleep(0.5)

    # 4. Capture screenshot of the words container
    words_element.screenshot("monkeytype_words.png")
    
    # 5. Preprocess image for maximum OCR accuracy
    img = cv2.imread("monkeytype_words.png")
    
    # Upscale 2x for clearer character edge detection
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite("processed_words.png", thresh)

    # 6. Extract full block text across all lines
    extracted_text = pytesseract.image_to_string(thresh, config="--psm 6")
    cleaned_text = " ".join(extracted_text.split())
    
    print(f"Extracted Text ({len(cleaned_text)} characters):\n{cleaned_text}\n")

    # 7. Auto-type extracted characters
    typing_delay = 0.015  # Adjust delay between keystrokes

    for char in cleaned_text:
        pyautogui.write(char)
        time.sleep(typing_delay)

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    run_monkeytype_ocr()