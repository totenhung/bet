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
MAIN_URL = "https://789ce.com/"
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

def remove_modal_and_backdrop(driver):
    wait = WebDriverWait(driver, 10)
    try:
        for i in range(2):
            try:
                modal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="dialog"]')))
                driver.execute_script("arguments[0].remove();", modal)
                print("Thẻ modal đã được xóa.")
            except Exception as e:
                print(f"Lỗi khi xóa modal lần {i+1}: {e}")
            time.sleep(1)
        
        # Tìm thẻ modal-backdrop
        backdrop = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.modal-backdrop')))
        
        # Xóa thẻ modal-backdrop bằng JavaScript
        driver.execute_script("arguments[0].remove();", backdrop)
        print("Thẻ modal-backdrop đã được xóa.")
        time.sleep(1)
    
    except Exception as e:
        print(f"Không thể xóa thẻ modal hoặc modal backdrop: {e}")

def remove_modal_and_backdrop_after_login(driver):
    remove_modal_and_backdrop(driver)
    try:
        button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[ng-click="$ctrl.ok()"]')))
        button.click()
    except Exception as e:
        print(f"Lỗi khi nhấp vào nút x: {e}")

def get_captcha_image_url(driver):
    try:
        # Tìm thẻ img chứa thuộc tính ng-src
        captcha_img = driver.find_element(By.CSS_SELECTOR, 'img[ng-class="$ctrl.styles.captcha"]')
        # Lấy giá trị thuộc tính ng-src
        captcha_img_url = captcha_img.get_attribute('ng-src')
        if captcha_img_url:
            return captcha_img_url
        else:
            print("Không thể lấy URL hình ảnh CAPTCHA.")
            return None
    except Exception as e:
        print(f"Lỗi khi lấy URL hình ảnh CAPTCHA: {e}")
        return None
    
def get_captcha_number(captcha_img_url):
    driver_2 = create_chrome_driver(headless=True)
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

        parent_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//h1[contains(text(), "Kết quả tìm kiếm bằng hình ảnh")]')))
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
    driver = create_chrome_driver(detach=True)
    try:
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, WAIT_TIMEOUT)

        remove_modal_and_backdrop(driver)

        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[ng-click="$ctrl.openLoginModal()"]')))
        login_button.click()

        username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[ng-model="$ctrl.user.account.value"]')))
        username_input.send_keys("keocon09")

        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[ng-model="$ctrl.user.password.value"]')))
        password_input.send_keys("keocon01@")

        captcha_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[ng-focus="$ctrl.captchaFocus()"]')))
        captcha_field.click()

        time.sleep(1)

        captcha_img_url = get_captcha_image_url(driver)

        if captcha_img_url:
            captcha_number = get_captcha_number(captcha_img_url)
            if captcha_number:
                captcha_field.send_keys(captcha_number)
            else:
                print("Không thể lấy mã CAPTCHA.")
                return
        else:
            print("URL hình ảnh CAPTCHA không được tìm thấy.")
            return

        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[ng-class="$ctrl.styles[\'login-btn\']"]')))
        login_button.click()

        wait = WebDriverWait(driver, 10)
        remove_modal_and_backdrop_after_login(driver)

    finally:
        #driver.quit()
        pass

if __name__ == "__main__":
    main()