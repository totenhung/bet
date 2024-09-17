
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

if __name__ == "__main__":
    chrome_driver_path = r"D:\VSCode\Python\Chrome\chromedriver-128.exe"

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Khởi tạo trình duyệt Chrome sử dụng ChromeDriver đã cài đặt sẵn
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://sh16.co/")
    time.sleep(3)

    remove_modal_and_backdrop(driver)

    # Tìm nút theo văn bản
    button = driver.find_element(By.CSS_SELECTOR, '[ng-click="$ctrl.openLoginModal()"]')

    button.click()
    time.sleep(1)

    # Nhập tài khoản vào ô văn bản
    username_input = driver.find_element(By.CSS_SELECTOR, 'input[ng-model="$ctrl.user.account.value"]')
    username_input.send_keys("keocon09")
    time.sleep(0.2)

    # Nhập mật khẩu vào ô mật khẩu
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[ng-model="$ctrl.user.password.value"]')
    password_input.send_keys("keocon01@")
    time.sleep(0.2)

    captcha_field = driver.find_element(By.CSS_SELECTOR, 'input[ng-focus="$ctrl.captchaFocus()"]')
    captcha_field.click()

    time.sleep(1)

    # Tìm phần tử hình ảnh CAPTCHA
    captcha_img = driver.find_element(By.CSS_SELECTOR, 'img[ng-click="$ctrl.refreshCaptcha()"]')

    # Lấy URL của hình ảnh CAPTCHA
    captcha_img_url = captcha_img.get_attribute('ng-src')

    # Lấy mã CAPTCHA
    chrome_options_2 = Options()
    chrome_options_2.add_argument("--headless")  # Chạy chế độ headless

    # Khởi tạo trình duyệt Chrome
    driver_2 = webdriver.Chrome(service=service, options=chrome_options_2)

    # Mở một trang web khác
    driver_2.get("https://www.google.com/")
    time.sleep(1)

    button = driver_2.find_element(By.CSS_SELECTOR, 'div[aria-label="Tìm kiếm bằng hình ảnh"]')
    # Nhấn vào nút
    button.click()
    time.sleep(1)

    input_field = driver_2.find_element(By.CSS_SELECTOR, 'input[placeholder="Paste image link"]')
    # Nhập văn bản vào ô nhập liệu
    input_field.send_keys(captcha_img_url)
    time.sleep(1)

    buttons = driver_2.find_elements(By.XPATH, '//div[@role="button"]')
    # Duyệt qua các phần tử để tìm nút có nội dung là "Search"
    for button in buttons:
        if button.text.strip() == "Search":
            button.click()
            break
    time.sleep(1)

    button = driver_2.find_element(By.XPATH, '//button[@aria-label="Chuyển sang chế độ Văn bản"]')
    button.click()
    time.sleep(1)

    button = driver_2.find_element(By.XPATH, '//span[text()="Chọn toàn bộ văn bản"]')
    button.click()
    time.sleep(1)

    parent_element = driver_2.find_element(By.XPATH, '//h1[contains(text(), "Kết quả tìm kiếm bằng hình ảnh")]')

    # Tìm các thẻ con của thẻ chứa
    # Điều chỉnh XPath hoặc phương thức tìm kiếm nếu cần
    child_elements = parent_element.find_elements(By.XPATH, './/following-sibling::*')

    # Biểu thức chính quy để tìm số
    number_pattern = re.compile(r'\b\d+\b')

    # Tìm số đầu tiên trong các thẻ con
    captcha_number = None
    for child in child_elements:
        text = child.text
        match = number_pattern.search(text)
        if match:
            captcha_number = match.group()
            break

    captcha_field.send_keys(captcha_number)
    time.sleep(1)

    login_button = driver.find_element(By.CSS_SELECTOR, 'button[ng-class="$ctrl.styles[\'login-btn\']"]')
    login_button.click()
    time.sleep(1)

    remove_modal_and_backdrop(driver)