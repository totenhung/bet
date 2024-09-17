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
    "https://www.78win3.life/"
]
GOOGLE_URL = "https://www.google.com/"
WAIT_TIMEOUT = 10

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

def remove_announcement_dialog(driver):
    try:
        # Chờ cho phần tử có class 'float-center-ads-modal' được tải hoàn tất
        wait = WebDriverWait(driver, 10)
        
        # Tìm phần tử có class 'float-center-ads-modal'
        ads_modal = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'float-center-ads-modal')))
        
        # Xóa phần tử 'float-center-ads-modal' bằng JavaScript
        driver.execute_script("arguments[0].remove();", ads_modal)
        
        print("Thẻ 'float-center-ads-modal' đã được xóa thành công.")
    except Exception as e:
        print(f"Lỗi khi xoá quảng cáo: {e}")

def click_register_button(driver):
    try:
        # Chờ cho phần tử có class 'tools-item' và href '/signup' xuất hiện
        wait = WebDriverWait(driver, 10)
        
        # Tìm thẻ <a> với class 'tools-item' và href '/signup'
        signup_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.tools-item[href='/signup']")))
        signup_link.click()
        
        print("Đã nhấn nút 'Đăng ký'.")
    except Exception as e:
        print(f"Lỗi khi nhấn Đăng ký: {e}")
        return None

def enter_username(driver, username):
    try:
        # Chờ cho phần tử được tải hoàn tất
        wait = WebDriverWait(driver, 10)
        
        # Tìm trường nhập tên tài khoản bằng cách sử dụng formcontrolname
        username_input = wait.until(EC.presence_of_element_located((By.ID, 'playerid')))
 
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
        password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))
        
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
        confirm_password_input = wait.until(EC.presence_of_element_located((By.ID, 'confirmpassword')))
        
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
        name_input = wait.until(EC.presence_of_element_located((By.ID, 'firstname')))
        
        # Xóa giá trị hiện tại và nhập tên mới
        name_input.clear()
        name_input.send_keys(name)
        
        print(f"Tên đã được nhập.")
    except Exception as e:
        print(f"An error occurred: {e}")

def enter_mobile_number(driver, mobile_number):
    try:
        # Bỏ số 0 ở đầu số điện thoại đầu vào nếu có
        if mobile_number.startswith('0'):
            mobile_number = mobile_number[1:]

        # Chờ cho phần tử được tải hoàn tất
        wait = WebDriverWait(driver, 10)
        
        # Tìm trường nhập số điện thoại bằng cách sử dụng formcontrolname
        mobile_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control')))
        
        # Xóa giá trị hiện tại và nhập số điện thoại mới
        mobile_input.clear()
        mobile_input.send_keys(mobile_number)
        
        print(f"Số điện thoại đã được nhập.")
    except Exception as e:
        print(f"An error occurred: {e}")

def click_submit_button(driver):
    try:
        wait = WebDriverWait(driver, 10)
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Đăng ký ngay')]")))
        submit_button.click()
        
        print("Đã bấm vào nút ĐĂNG KÝ NGAY.")
    
    except Exception as e:
        print(f"Lỗi khi bấm nút: {str(e)}")


def sign_up_to_site(driver, url):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)

    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    remove_announcement_dialog(driver)

    click_register_button(driver)

    enter_username(driver, "keocon09")

    enter_password(driver, "keocon01@")

    enter_confirm_password(driver, "keocon01@")

    enter_name(driver, "HA MANH HUNG")

    enter_mobile_number(driver, "0987457798")

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

