def remove_modal_and_backdrop_after_login(driver):
    remove_modal_and_backdrop(driver)
    try:
        button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[ng-click="$ctrl.ok()"]')))
        button.click()
    except Exception as e:
        print(f"Lỗi khi nhấp vào nút OK: {e}")