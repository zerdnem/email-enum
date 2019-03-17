from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
#driver = webdriver.Firefox()

def quitSelenium():
    driver.quit()

def instagramCheck(email):
    try:
        driver.get("https://www.instagram.com/accounts/password/reset/")
    except WebDriverException:
        result = "Site could not be reached, try again"
        return result
    try:
        assert "Reset Password" in driver.title
    except AssertionError:
        result = "Site could not be loaded properly, try again"
        return result
    sleep(1.5)
    user = driver.find_element_by_id("cppEmailOrUsername")
    user.send_keys(email)
    user.send_keys(Keys.RETURN)
    #driver.find_element_by_tag_name("button").click()
    sleep(2)
    if "Thanks! Please check" in driver.page_source:
        result = "Found"
    else:
        result = "Not Found"
    return result

def twitterCheck(email):
    try:
        driver.get("https://twitter.com/account/begin_password_reset")
    except WebDriverException:
        result = "Site could not be reached, try again"
        return result
    try:
        assert "Password Reset" in driver.title
    except AssertionError:
        result = "Site could not be loaded properly, try again"
        return result
    sleep(1)
    user = driver.find_element_by_name("account_identifier")
    user.send_keys(email)
    driver.find_element_by_class_name("EdgeButton--primary").click()
    sleep(1)
    if "We couldn't find your account with that information" in driver.page_source:
        result = "Not Found"
        return result
    if "Enter your email, phone number, or username" not in driver.page_source and "You've exceeded the number of attempts. Please try again later" not in driver.page_source:
        result = "Found"
        return result
    if "You've exceeded the number of attempts. Please try again later" in driver.page_source:
        result = "Exceeded maximum tries, try again later"
        return result
    else:
        result = "Captcha encountered, you'll have to check this manually"
        return result

def snapchatCheck(email):
    try:
        driver.get("https://accounts.snapchat.com/accounts/password_reset_request")
    except WebDriverException:
        result = "Site could not be reached, try again"
        return result
    try:
        assert "Reset Password" in driver.title
    except AssertionError:
        result = "Site could not be loaded properly, try again"
        return result
    sleep(1.5)
    user = driver.find_element_by_name("emailaddress")
    user.send_keys(email)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/article/div/div[3]/form/div[3]/button").click()
    sleep(2)
    if "Email address is" in driver.page_source:
        result = "Not Found"
        return result
    if "Email address is invalid" not in driver.page_source and "If you know your current password, you may" in driver.page_source:
        result = "Captcha encountered, you'll have to check this manually"
        return result
    else:
        result = "Found"
        return result

def facebookCheck(email):
    try:
        driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar")
    except WebDriverException:
        result = "Site could not be reached, try again"
        return result
    try:
        assert "Forgot Password" in driver.title
    except AssertionError:
        result = "Site could not be loaded properly, try again"
        return result
    sleep(1)
    user = driver.find_element_by_xpath('//*[@id="identify_email"]')
    user.send_keys(email)
    user.send_keys(Keys.ENTER)
    #driver.find_element_by_xpath('//*[@id="u_0_2"]').click()
    sleep(2)
    if "No Search Results" in driver.page_source:
        result = "Not Found"
        return result
    if "No Search Results" and "No longer have access to these?" in driver.page_source:
        result = "Found"
        return result
    else:
        result = "Captcha encountered, you'll have to check this manually"
        return result

def yougoogleCheck(email):
    try:
        driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    except WebDriverException:
        result = "Site could not be reached, try again"
        return result
    try:
        assert "Sign in" in driver.title
    except AssertionError:
        result = "Site could not be loaded properly, try again"
        return result
    sleep(1)
    user = driver.find_element_by_name("identifier")
    user.send_keys(email)
    user.send_keys(Keys.ENTER)
    sleep(1.5)
    try:
        password  = driver.find_element_by_name("password")
        result = "Found"
        return result
    except NoSuchElementException as notfound:
        try:
            captcha_enter = driver.find_element_by_name("ca")
            captcha_enter.send_keys("test")
            result = "Captcha encountered, you'll have to check this manually"
            return result
        except ElementNotInteractableException as notfoundcaptcha:
            result = "Not Found"
            return result

def twitchCheck(email):
    try:
        driver.get("https://www.twitch.tv/")
    except WebDriverException:
        result = "Site could not be reached, try again"
        return result
    try:
        assert "Discover" in driver.page_source
    except AssertionError:
        result = "Site could not be loaded properly, try again"
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div/div[5]/div/div[1]/button").click()
    waitforuser = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/form/div/div[1]/div/div[2]/input")))
    user = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/form/div/div[1]/div/div[2]/input")
    password = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div/div[1]/div[2]/div[1]/input")
    user.send_keys(email)
    password.send_keys("123456789")
    password.send_keys(Keys.ENTER)
    sleep(1.5)
    if "This email is not linked to a Twitch account. Please log in with a username instead." in driver.page_source:
        result = "Not Found"
        return result
    else:
        result = "Found"
        return result


