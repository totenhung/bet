from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

USER_SWITCH_EXTENSION_ID = "bhchdcejhohfmigjafbampogmaanbfkg"
PROXY_EXTENSION_ID = "pmdlifofgdjcolhfjjfkojibiimoahlc"
TIME_REFRESH_PROXY = '28'

API_KEY = "a9a8c44027880da2475b3f5988a2a5f3"

def open_proxy_extension_popup(driver, extension_id):
    try:
        extension_url = f"chrome-extension://{extension_id}/popup.html"
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(extension_url)

        print("Đã mở tab mới và điều hướng đến URL của extension.")

    except Exception as e:
        print(f"Lỗi khi mở tab mới và điều hướng đến URL của extension: {e}")

def open_user_switch_extension_popup(driver, extension_id):
    try:
        extension_url = f"chrome-extension://{extension_id}/data/popup/index.html"
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(extension_url)

        print("Đã mở tab mới và điều hướng đến URL của extension.")

    except Exception as e:
        print(f"Lỗi khi mở tab mới và điều hướng đến URL của extension: {e}")

def enter_api_key(driver, api_key):
    try:
        # Đợi cho đến khi ô input với id='API-input' xuất hiện
        wait = WebDriverWait(driver, 10)
        api_input = wait.until(EC.element_to_be_clickable((By.ID, 'API-input')))
        api_input.send_keys(api_key)
        
        print(f"Đã nhập API key: {api_key}")
        
    except Exception as e:
        print(f"Lỗi khi nhập API key: {e}")

def click_connect_to_api_button(driver):
    try:
        # Đợi nút xuất hiện và có thể bấm được
        wait = WebDriverWait(driver, 10)
        connect_button = wait.until(EC.element_to_be_clickable((By.ID, 'auto-submit')))
        
        # Nhấn vào nút
        connect_button.click()
        print("Đã nhấn vào nút 'Connect to API'.")
        
    except Exception as e:
        print(f"Lỗi khi nhấn vào nút 'Connect to API': {e}")

def click_use_refresh_page(driver):
    try:
        wait = WebDriverWait(driver, 10)
        checkbox = wait.until(EC.presence_of_element_located((By.ID, 'use-refresh-page')))

        if not checkbox.is_selected():
            checkbox.click()
            print("Checkbox 'use-refresh-page' đã được chọn.")
        else:
            print("Checkbox 'use-refresh-page' đã được chọn sẵn.")
        
    except Exception as e:
        print(f"Lỗi khi bấm vào use-refresh-page: {e}")

def click_use_renew(driver):
    try:
        # Đợi cho đến khi checkbox với id='use-renew' xuất hiện
        wait = WebDriverWait(driver, 10)
        checkbox = wait.until(EC.presence_of_element_located((By.ID, 'use-renew')))
        
        # Kiểm tra xem checkbox đã được chọn chưa, nếu chưa thì click để chọn
        if not checkbox.is_selected():
            checkbox.click()
            print("Checkbox 'use-renew' đã được chọn.")
        else:
            print("Checkbox 'use-renew' đã được chọn sẵn.")
        
    except Exception as e:
        print(f"Lỗi khi bấm vào use-renew: {e}")

def enter_number(driver, value):
    try:
        # Đợi cho đến khi ô input số với id='time-input' xuất hiện
        wait = WebDriverWait(driver, 10)
        number_input = wait.until(EC.presence_of_element_located((By.ID, 'time-input')))
        
        # Nhập giá trị vào ô input số
        number_input.send_keys(value)
        print(f"Đã nhập giá trị '{value}' vào ô input số.")
        
    except Exception as e:
        print(f"Lỗi khi nhập giá trị vào ô input số: {e}")

def click_use_new_proxy(driver):
    try:
        # Đợi cho đến khi nút với id='use-new-proxy' xuất hiện
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.ID, 'use-new-proxy')))
        
        # Click vào nút
        button.click()
        print("Nút 'Use NEW Proxy' đã được bấm.")
        
    except Exception as e:
        print(f"Lỗi khi bấm vào nút 'Use NEW Proxy': {e}")

def turn_on_tm_proxy(driver):
    try:
        open_proxy_extension_popup (driver, PROXY_EXTENSION_ID)
        time.sleep(1)
        enter_api_key(driver, API_KEY)
        time.sleep(1)
        click_connect_to_api_button(driver)
        time.sleep(3)
        click_use_refresh_page(driver)
        time.sleep(1)
        click_use_renew(driver)
        time.sleep(1)
        enter_number(driver, TIME_REFRESH_PROXY)
        time.sleep(1)
        click_use_new_proxy(driver)

    except Exception as e:
        print(f"Lỗi khi cấu hình proxy: {e}")

def turn_on_usr_sw_proxy(driver):
    try:
        open_user_switch_extension_popup(driver, USER_SWITCH_EXTENSION_ID)
        select_option_ios(driver)
        select_option_1(driver)
        click_apply_button(driver)

    except Exception as e:
        print(f"Lỗi khi cấu hình user switch: {e}")\
        
def select_option_ios(driver):
    try:
        # Đợi cho đến khi thẻ <select> với id='os' xuất hiện
        wait = WebDriverWait(driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.ID, 'os')))
        
        # Tạo đối tượng Select từ thẻ <select>
        select = Select(select_element)
        
        # Chọn tùy chọn "iOS"
        select.select_by_visible_text("iOS")
        print("Đã chọn tùy chọn 'iOS'.")
        
    except Exception as e:
        print(f"Lỗi khi chọn tùy chọn 'iOS': {e}")

def select_option_1(driver):
    try:
        # Chờ cho bảng và các tùy chọn được tải hoàn tất
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.ID, "list")))
        
        # Tìm tất cả các hàng trong bảng
        rows = table.find_elements(By.TAG_NAME, "tr")
        
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 0:
                # Kiểm tra nếu ô đầu tiên có số "1"
                if cells[0].text.strip() == "1":
                    # Chọn radio button trong hàng đó
                    radio_button = cells[1].find_element(By.TAG_NAME, "input")
                    if not radio_button.is_selected():
                        radio_button.click()
                    break
    except Exception as e:
        print(f"An error occurred: {e}")

def click_apply_button(driver):
    try:
        # Chờ cho nút được tải hoàn tất
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-cmd="apply"]')))
        
        # Nhấp vào nút
        button.click()
        print("Đã apply cho tất cả các tab.")
        
    except Exception as e:
        print(f"An error occurred: {e}")