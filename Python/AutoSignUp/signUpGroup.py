import json
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import setUpExtensions as setupEx

# Hằng số cấu hình
CHROME_DRIVER_PATH = r"D:\VSCode\Python\Chrome\chromedriver-128.exe"
USER_SWITCH_EXTENSION_PATH = r"D:\VSCode\Python\Chrome\User-Agent Switcher and Manager.crx"
PROXY_EXTENSION_PATH = r"D:\VSCode\Python\Chrome\TM Proxy.crx"

MAIN_URLS = [
    "https://m.sh16.co/Account/Register",
    "https://m.hi774.com/Account/Register",
    "https://m.f8bet10.vip/Account/Register",
    "https://m.new8862.vip/Account/Register",
    "https://m.789ce.com/Account/Register"
]

GOOGLE_URL = "https://www.google.com/"
WAIT_TIMEOUT = 10

def load_config(file_path):
    """Load configuration from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)
    
def create_chrome_driver(headless=False, detach=False):
    chrome_options = Options()
    chrome_options.add_extension(USER_SWITCH_EXTENSION_PATH)
    chrome_options.add_extension(PROXY_EXTENSION_PATH)
    
    if headless:
        chrome_options.add_argument("--headless")
    if detach:
        chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=CHROME_DRIVER_PATH)
    return webdriver.Chrome(service=service, options=chrome_options)

def get_captcha_image_url(driver):
    try:
        # Đợi 2 giây để reload captcha
        time.sleep(3)  

        wait = WebDriverWait(driver, 10)
        img_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.absolute.right-7.top-1")))
        img_url = img_element.get_attribute('src')

        return img_url
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_captcha_number(captcha_img_url):
    driver_2 = create_chrome_driver(headless=True)
    try:
        driver_2.get(GOOGLE_URL)
        wait = WebDriverWait(driver_2, WAIT_TIMEOUT)

        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Tìm kiếm bằng hình ảnh"]')))
        button.click()

        time.sleep(2)

        input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Paste image link"]')))
        input_field.send_keys(captcha_img_url)

        time.sleep(1)

        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and text()="Search"]')))
        search_button.click()

        time.sleep(2)

        text_mode_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Chuyển sang chế độ Văn bản"]')))
        text_mode_button.click()

        time.sleep(2)

        select_all_text_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Chọn toàn bộ văn bản"]')))
        select_all_text_button.click()

        time.sleep(2)

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

def enter_username(driver, username):
    try:
        # Chờ cho phần tử được tải hoàn tất
        wait = WebDriverWait(driver, 10)
        
        # Tìm trường nhập tên tài khoản bằng cách sử dụng formcontrolname
        username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="account"]')))
        
        # Xóa giá trị hiện tại và nhập tên tài khoản mới
        username_input.clear()
        username_input.send_keys(username)
        
        print(f"Username '{username}' đã được nhập.")
    except Exception as e:
        print(f"An error occurred: {e}")

def enter_password(driver, password):
    try:
        # Chờ cho phần tử được tải hoàn tất
        wait = WebDriverWait(driver, 10)
        
        # Tìm trường nhập mật khẩu bằng cách sử dụng formcontrolname
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]')))
        
        # Xóa giá trị hiện tại và nhập mật khẩu mới
        password_input.clear()
        password_input.send_keys(password)
        
        print(f"Password đã được nhập.")
    except Exception as e:
        print(f"An error occurred: {e}")

def enter_confirm_password(driver, confirm_password):
    try:
        # Chờ cho phần tử được tải hoàn tất
        wait = WebDriverWait(driver, 10)
        
        # Tìm trường nhập xác nhận mật khẩu bằng cách sử dụng formcontrolname
        confirm_password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="confirmPassword"]')))
        
        # Xóa giá trị hiện tại và nhập xác nhận mật khẩu mới
        confirm_password_input.clear()
        confirm_password_input.send_keys(confirm_password)
        
        print(f"Xác nhận mật khẩu đã được nhập.")
    except Exception as e:
        print(f"An error occurred: {e}")

def enter_name(driver, name):
    try:
        # Chờ cho phần tử được tải hoàn tất
        wait = WebDriverWait(driver, 10)
        
        # Tìm trường nhập tên bằng cách sử dụng formcontrolname
        name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="name"]')))
        
        # Xóa giá trị hiện tại và nhập tên mới
        name_input.clear()
        name_input.send_keys(name)
        
        print(f"Tên đã được nhập.")
    except Exception as e:
        print(f"An error occurred: {e}")

def enter_mobile_number(driver, mobile_number):
    try:
        # Chờ cho phần tử được tải hoàn tất
        wait = WebDriverWait(driver, 10)
        
        # Tìm trường nhập số điện thoại bằng cách sử dụng formcontrolname
        mobile_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="mobile"]')))
        
        # Xóa giá trị hiện tại và nhập số điện thoại mới
        mobile_input.clear()
        mobile_input.send_keys(mobile_number)
        
        print(f"Số điện thoại đã được nhập.")
    except Exception as e:
        print(f"An error occurred: {e}")

def click_check_code_input(driver):
    try:
        # Chờ cho phần tử input có mặt trên trang
        wait = WebDriverWait(driver, 10)
        
        # Tìm input có formcontrolname là checkCode
        check_code_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[formcontrolname="checkCode"]')))
        
        # Nhấn vào input
        check_code_input.click()
        
        print("Đã nhấn vào ô mã xác minh.")
    except Exception as e:
        print(f"Lỗi khi nhấn vào ô mã xác minh: {e}")


def fill_check_code_input(driver, captcha_number):
    try:
        wait = WebDriverWait(driver, 10)
        check_code_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[formcontrolname="checkCode"]')))
        check_code_input.send_keys(captcha_number)
        print("Đã điền mã xác minh.")
    except Exception as e:
        print(f"Lỗi khi điền mã xác minh: {e}")

def click_submit_button(driver):
    try:
        wait = WebDriverWait(driver, 10)
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-btn')))
        submit_button.click()
        
        print("Đã bấm vào nút ĐĂNG KÝ NGAY.")
    
    except Exception as e:
        print(f"Lỗi khi bấm nút: {str(e)}")


def sign_up_to_site(driver, url):
    config = load_config('config.json')

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)

    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    enter_username(driver, config["username"])
    enter_password(driver, config["password"])
    enter_confirm_password(driver, config["confirm_password"])
    enter_name(driver, config["name"])
    enter_mobile_number(driver, config["mobile_number"])
    
    click_check_code_input(driver)

    captcha_img_url = get_captcha_image_url(driver)

    captcha_number = get_captcha_number(captcha_img_url)

    fill_check_code_input(driver, captcha_number)

    click_submit_button(driver)

def loginGroup(driver):
    try:
        setupEx.turn_on_usr_sw_proxy(driver)

        time.sleep(1)
        
        setupEx.turn_on_tm_proxy(driver)

        time.sleep(3)
        
        for url in MAIN_URLS:
            sign_up_to_site(driver, url)
  
    finally:
        pass

if __name__ == "__main__":
    driver = create_chrome_driver(detach=True)
    loginGroup(driver)

