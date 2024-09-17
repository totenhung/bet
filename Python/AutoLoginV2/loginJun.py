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
MAIN_URL = "https://www.jun889.love/"
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

def remove_ad_center(driver):
    try:
        wait = WebDriverWait(driver, 10)
        ad_center = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.ad-center')))
        driver.execute_script("arguments[0].remove();", ad_center)
        print("Thẻ 'ad-center' đã được xóa.")
    except Exception as e:
        print(f"Lỗi khi xóa thẻ 'ad-center': {e}")

def click_login_button(driver):
    try:
        # Đợi cho đến khi nút đăng nhập xuất hiện và có thể bấm được
        wait = WebDriverWait(driver, 10)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn-big.login')))
        
        # Nhấn vào nút đăng nhập
        login_button.click()
        print("Đã nhấn vào nút Đăng nhập.")
        
    except Exception as e:
        print(f"Lỗi khi nhấn vào nút Đăng nhập: {e}")
        
def enter_username(driver, username):
    try:
        # Đợi cho đến khi ô nhập tên đăng nhập xuất hiện
        wait = WebDriverWait(driver, 10)
        username_input = wait.until(EC.presence_of_element_located((By.ID, 'login')))
        
        # Xóa nội dung cũ (nếu có) và điền tên đăng nhập mới
        username_input.clear()
        username_input.send_keys(username)
        print(f"Đã điền tên đăng nhập: {username}")
        
    except Exception as e:
        print(f"Lỗi khi điền tên đăng nhập: {e}")

def enter_password(driver, password):
    try:
        # Đợi cho đến khi ô nhập mật khẩu xuất hiện
        wait = WebDriverWait(driver, 10)
        password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))
        
        # Xóa nội dung cũ (nếu có) và điền mật khẩu mới
        password_input.clear()
        password_input.send_keys(password)
        print("Đã điền mật khẩu.")
        
    except Exception as e:
        print(f"Lỗi khi điền mật khẩu: {e}")

def click_login_submit_button(driver):
    try:
        # Đợi cho đến khi nút đăng nhập có thể bấm được
        wait = WebDriverWait(driver, 2)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.nrc-button')))
        
        # Nhấn vào nút đăng nhập
        login_button.click()
        print("Đã nhấn vào nút Đăng Nhập.")
        
    except Exception as e:
        print(f"Lỗi khi nhấn vào nút Đăng Nhập: {e}")

def remove_mission_calendar(driver):
    try:
        # Đợi cho đến khi phần tử cần xóa xuất hiện
        wait = WebDriverWait(driver, 10)
        mission_calendar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.hover-container.mission-calendar')))
        
        # Sử dụng JavaScript để xóa phần tử này khỏi DOM
        driver.execute_script("arguments[0].remove();", mission_calendar)
        print("Đã xóa thẻ mission-calendar.")
        
    except Exception as e:
        print(f"Lỗi khi xóa thẻ mission-calendar: {e}")

def loginJun(driver):
    try:
        driver.execute_script("window.open('');")  # Mở tab mới
        driver.switch_to.window(driver.window_handles[-1])

        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, WAIT_TIMEOUT)

        remove_ad_center(driver)

        click_login_button(driver)

        enter_username(driver, "keocon09")

        enter_password(driver, "keocon01@")

        time.sleep(2)
        
        click_login_submit_button(driver)

        time.sleep(2)

        remove_mission_calendar(driver)

    finally:
        #driver.quit()
        pass