import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Hằng số cấu hình
CHROME_DRIVER_PATH = r"D:\VSCode\Python\Chrome\chromedriver-128.exe"
MAIN_URL = "https://sh16.co/"
GOOGLE_URL = "https://www.google.com/"
WAIT_TIMEOUT = 10

def create_chrome_driver(headless=False, detach=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    if detach:
        chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=CHROME_DRIVER_PATH)
    return webdriver.Chrome(service=service, options=chrome_options)

def get_captcha_number(captcha_img_url):
    driver_2 = create_chrome_driver(detach=True, headless=False)
    try:
        driver_2.get(GOOGLE_URL)
        wait = WebDriverWait(driver_2, WAIT_TIMEOUT)

        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Tìm kiếm bằng hình ảnh"]')))
        button.click()

        input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Paste image link"]')))
        input_field.send_keys(captcha_img_url)

        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and text()="Search"]')))
        search_button.click()

        text_mode_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Chuyển sang chế độ Văn bản"]')))
        text_mode_button.click()

        select_all_text_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Chọn toàn bộ văn bản"]')))
        select_all_text_button.click()

        parent_element = wait.until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Kết quả tìm kiếm bằng hình ảnh")]')))
        child_elements = parent_element.find_elements(By.XPATH, './/following-sibling::*')

        number_pattern = re.compile(r'\b\d+\b')
        for child in child_elements:
            text = child.text
            match = number_pattern.search(text)
            if match:
                return match.group()
    finally:
        driver_2.quit()
    return None


def main():
    captcha_img_url = "data:image/png;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDt/EfiS58N7JItImubKLaJrgSBBGGP3VT+MgdxwO560mreKf7KvZLS1tBP9ktftU+6Ux7Ys/dRduGYKDjkYx160zxI+qtcW9lZaA2oWcbhnD3UcKSEEMECnqBjPTqO4DA1Nd0C81O8X7LDNZ3Etp9luLkSRiJoz8zRrGQSxAyARtHXLcVxRUWlfzPT06lzWfFT6Rp9rf2emS3liyxsZhIIwqORhVX+M4xjGcdz1za1nxHbaIbe3UIbuUfuIZplgULkE7i2FAAwARk5yADg1neINJkvrBtDj0V5YoIRHY3vnovlyYyOCVIwAOV3cZ96pa34d1QXc/kQ/wBoLdaV/Z4ZmRCkgO4HDFcrjnIyRg+nIlB/iC6XO1iMiQoHVEkVQAitlc9Sq5CggAYB+vvRUGnWz6dplpZtKZZLaFIQx48wgDIA4HQcH6+hyVk0r6ErVbFo/JewRp8sfkv8o4HBTHFB+S9gjT5Y/Jf5RwOCmOKKKT/r8Qf9fiB+S9gjT5Y/Jf5RwOCmOKD8l7BGnyx+S/yjgcFMcUUUP+vxB/1+IH5L2CNPlj8l/lHA4KY4ooopS3Jluf/Z"

    number_pattern = get_captcha_number(captcha_img_url)

    print(number_pattern)

if __name__ == "__main__":
    main()