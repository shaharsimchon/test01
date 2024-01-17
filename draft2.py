from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def registration_business_step1(browser, personal_info):
    wait = WebDriverWait(browser, 5)
    browser.maximize_window()

    elem_fname = browser.find_element(By.ID, "fname")
    elem_fname.click()
    elem_fname.send_keys(personal_info["firstname"])

    elem_Mname = browser.find_element(By.ID, "mname")
    elem_Mname.click()
    elem_Mname.send_keys(personal_info["midlename"])

    elem_lname = browser.find_element(By.ID, "lname")
    elem_lname.click()
    elem_lname.send_keys(personal_info["lastname"])

    gender_radio = browser.find_element(By.XPATH, f"//label[contains(text(), '{personal_info['gender']}')]")
    gender_radio.click()

    birth_day = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'Day')]")
    birth_day.click()
    birth_day.send_keys(personal_info["birthday"])

    birth_month = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'Month')]")
    birth_month.click()
    birth_month.send_keys(personal_info["birthmounth"])

    birth_year = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'Year')]")
    birth_year.click()
    birth_year.send_keys(personal_info["birthyear"])

    email_input = browser.find_element(By.ID, "email")
    email_input.click()
    email_input.send_keys(personal_info["EmailAddress"])

    browser.execute_script("document.querySelector('#country-select-test').click()")
    country = browser.find_element(By.XPATH, f"//*[contains(@class, 'country-name') and contains(text(), '{personal_info['Coutrydropname']}')]")
    country.click()

    residence_address = browser.find_element(By.ID, "raddress")
    browser.execute_script("arguments[0].click();", residence_address)
    residence_address.send_keys(personal_info["ResidenceAddressP"])

    residence_city = browser.find_element(By.ID, "rcity")
    browser.execute_script("arguments[0].click();", residence_city)
    residence_city.send_keys(personal_info["ResidenceCity"])

    residence_post = browser.find_element(By.ID, "rpost")
    browser.execute_script("arguments[0].click();", residence_post)
    residence_post.send_keys(personal_info["ResidencePostalCode"])

    government_radio = browser.find_element(By.XPATH, '//*[@id="form"]/div/div[12]//label[contains(text(), "Yes")]')
    browser.execute_script("arguments[0].click();", government_radio)

    browser.execute_script("document.querySelector('[data-IqqVEXye=payment-agreement] input').click()")

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "policy-card")))

    browser.execute_script(
        """
        arguments[0].scrollTop = arguments[0].scrollHeight;
        setTimeout(function() {
            var checkbox = document.querySelector('.agree .wittix-checkbox');
             checkbox.click();
        }, 3000);
        """,
        browser.find_element(By.CLASS_NAME, "policy-card")
    )

    agree_checkbox = browser.find_element(By.XPATH, "//input[@id='t-agree-checkbox']")
    time.sleep(2)
    agree_checkbox.click()

    ok_button = browser.find_element(By.XPATH, '//button[contains(text(), "OK")]')
    ok_button.click()

    browser.execute_script("document.querySelector('[data-IqqVEXye=newsletter] input').click()")
    time.sleep(2)

    continue_step1 = browser.find_element(By.XPATH, '//button[span[text()="Continue"]]')

    # Uncomment the line below to perform the click action
    # continue_step1.click()

    time.sleep(5)

# Example usage:
# registration_business_step1(browser, personal_info)
