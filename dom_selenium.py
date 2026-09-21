import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def run_monkeytype_fast():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)

    # Persists your cookies, local storage, and login session
    profile_path = os.path.join(os.getcwd(), "selenium_chrome_profile")
    options.add_argument(f"--user-data-dir={profile_path}")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get("https://monkeytype.com")
    print("Waiting 5 seconds for page load...")
    time.sleep(5)  # Wait for initial page load

    input_field = driver.find_element(By.ID, "wordsInput")
    print("Starting word-by-word typing...")

    while True:
        try:
            # Targets the specific word currently marked active by Monkeytype's DOM
            target_word = driver.execute_script(
                "const active = document.querySelector('#words .word.active');"
                "if (active) return active.textContent;"
                "const untyped = document.querySelector('#words .word:not(.correct):not(.error)');"
                "return untyped ? untyped.textContent : null;"
            )

            # If no active/untyped words remain, the test is complete
            if not target_word:
                break

            # Send single word + space to move to the next word
            input_field.send_keys(target_word + " ")

            # Short delay allowing React state and DOM animations to update seamlessly
            time.sleep(0.05)

        except Exception:
            print("Test finished!")
            break


if __name__ == "__main__":
    run_monkeytype_fast()