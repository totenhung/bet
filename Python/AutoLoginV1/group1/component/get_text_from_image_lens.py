from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyperclip
import re

chrome_driver_path = r"D:\VSCode\Python\Chrome\chromedriver-128.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#chrome_options.add_argument("--headless")  # Chạy chế độ headless

# Khởi tạo trình duyệt Chrome sử dụng ChromeDriver đã cài đặt sẵn
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)



# Mở một trang web khác trong tab mới
driver.get("https://www.google.com/")
time.sleep(1)

button = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Tìm kiếm bằng hình ảnh"]')
# Nhấn vào nút
button.click()
time.sleep(1)

input_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Paste image link"]')
# Nhập văn bản vào ô nhập liệu
input_field.send_keys("data:image/png;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAASACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0C6j1Emyi060sg0sZLzzjeqAbeSgwWJ6cHjJOexyNP1bUNUTT7a0ttOjupEn8yeVC8TLE6pvVQQW3EjHzcZPJ7375bwPHGdAg1Sxmtv8AVIYw28EZL+YQpB+XGMkHNY/9hXsNlpUEukrqLx2zeXLDetC8TlgcO+VZowCo4yfl6dKJTd3r3/8AbvMypQjyq6X9W8v68+ulZa5E2hw381lC0o8y3ESHJnlVwmF47kZGegJJIAJqC0vtTuvDFjq7tpVkDbSTzGa2eVfLBBU8Opzt+uc9B0qmfBtzaaFbrp07/boNPkSJIxDskduScPGdpJbHBHAxkVonQZjaaDpiwpPZw4eeSQqCyxgMgOFH8W3oDwOepNNyet3+Pr5jUKa279umnl6fMvaCuoz6day6pa2QuJI2cJGhTC/Lt3Alvmx157kduStCGHP2f/RoDmInk9fu8njr/jRWVaWu/wCPm/7xNJXTdvw8l/dJIIIT9mzEhzCScqOT8tEEEJ+zZiQ5hJOVHJ+WiivQfX+u55q6f12CCCE/ZsxIcwknKjk/LRBBCfs2YkOYSTlRyflooofX+u4Lp/XYIIIT9mzEhzCScqOT8tFFFZ1N/wCu5pT2/rsj/9k=")
time.sleep(1)

buttons = driver.find_elements(By.XPATH, '//div[@role="button"]')
# Duyệt qua các phần tử để tìm nút có nội dung là "Search"
for button in buttons:
    if button.text.strip() == "Search":
        button.click()
        break
time.sleep(1)

button = driver.find_element(By.XPATH, '//button[@aria-label="Chuyển sang chế độ Văn bản"]')
button.click()
time.sleep(1)

button = driver.find_element(By.XPATH, '//span[text()="Chọn toàn bộ văn bản"]')
button.click()
time.sleep(1)

parent_element = driver.find_element(By.XPATH, '//h1[contains(text(), "Kết quả tìm kiếm bằng hình ảnh")]')

# Tìm các thẻ con của thẻ chứa
# Điều chỉnh XPath hoặc phương thức tìm kiếm nếu cần
child_elements = parent_element.find_elements(By.XPATH, './/following-sibling::*')

# Biểu thức chính quy để tìm số
number_pattern = re.compile(r'\b\d+\b')

# Tìm và in tất cả các số trong các thẻ con
first_number = None
for child in child_elements:
    text = child.text
    match = number_pattern.search(text)
    if match:
        first_number = match.group()
        break

if first_number:
    print('Số đầu tiên tìm được:', first_number)
else:
    print('Không tìm thấy số.')