from time import sleep

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Check:
    E, R, G, Y, B = '\033[0m', '\033[31m', '\033[32m', '\033[33m', '\033[34m'

    found = G + 'Found' + E

    def __init__(self, email, proxy, non_headless):
        self.email = email
        self.proxy = proxy
        self.non_headless = non_headless

        self.options = webdriver.FirefoxOptions()
        self.options.add_argument("--headless")

        self.fp = webdriver.FirefoxProfile()
        self.fp.set_preference('network.proxy.type', 1)
        self.fp.set_preference('network.proxy.ssl', '127.0.0.1')
        self.fp.set_preference('network.proxy.ssl_port', 8888)

        if self.proxy and self.non_headless:
            self.driver = webdriver.Firefox(firefox_profile=self.fp)

        elif self.proxy and not self.non_headless:
            self.driver = webdriver.Firefox(firefox_profile=self.fp, firefox_options=self.options)

        elif self.non_headless and not self.proxy:
            self.driver = webdriver.Firefox()

        else:
            self.driver = webdriver.Firefox(firefox_options=self.options)

    def quit_selenium(self):
        self.driver.quit()

    def instagram_check(self):
        try:
            # self.driver.get('https://whoer.net')
            # sleep(10)
            self.driver.get("https://www.instagram.com/accounts/login/")
        except WebDriverException:
            result = "Site could not be reached, try again"
            return result
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.NAME, 'username')))
        login_form = self.driver.find_element_by_name('username')
        pass_form = self.driver.find_element_by_name('password')
        login_form.send_keys(self.email)
        pass_form.send_keys('checkinstagram')
        pass_form.send_keys(Keys.RETURN)
        self.driver.delete_all_cookies()
        sleep(1)
        if 'Sorry, your password was incorrect' in self.driver.page_source:
            return Check.found
        else:
            return 'Not Found'

    def twitter_check(self):
        try:
            self.driver.get("https://twitter.com/account/begin_password_reset")
        except WebDriverException:
            result = "Site could not be reached, try again"
            return result
        try:
            assert "Password Reset" in self.driver.title
        except AssertionError:
            result = "Site could not be loaded properly, try again"
            return result
        sleep(1)
        user = self.driver.find_element_by_name("account_identifier")
        user.send_keys(self.email)
        self.driver.find_element_by_class_name("EdgeButton--primary").click()
        sleep(1)
        self.driver.delete_all_cookies()
        if "We couldn't find your account with that information" in self.driver.page_source:
            result = "Not Found"
            return result
        if "Enter your email, phone number, or username" not in self.driver.page_source and \
                "You've exceeded the number of attempts. Please try again later" not in self.driver.page_source:
            result = Check.found
            return result
        if "You've exceeded the number of attempts. Please try again later" in self.driver.page_source:
            result = Check.Y + "Exceeded maximum tries, try again later" + Check.E
            return result
        else:
            result = Check.Y + "Captcha encountered, you'll have to check this manually" + Check.E
            return result

    def snapchat_check(self):
        try:
            self.driver.get("https://accounts.snapchat.com/accounts/password_reset_request")
        except WebDriverException:
            result = "Site could not be reached, try again"
            return result
        try:
            assert "Reset Password" in self.driver.title
        except AssertionError:
            result = "Site could not be loaded properly, try again"
            return result
        sleep(1.5)
        user = self.driver.find_element_by_name("emailaddress")
        user.send_keys(self.email)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/article/div/div[3]/form/div["
                                          "3]/button").click()
        sleep(2)
        self.driver.delete_all_cookies()
        if "Email address is" in self.driver.page_source:
            result = "Not Found"
            return result
        if "Email address is invalid" not in self.driver.page_source and "If you know your current password, you may" \
                in self.driver.page_source:
            result = Check.Y + "Captcha encountered, you'll have to check this manually" + Check.E
            return result
        else:
            return Check.found

    def facebook_check(self):
        try:
            self.driver.get("https://www.facebook.com/login/device-based/regular/login")
        except WebDriverException:
            result = "Site could not be reached, try again"
            return result
        try:
            assert "Facebook" in self.driver.title
        except AssertionError:
            result = "Site could not be loaded properly, try again"
            return result
        sleep(1)
        login_form = self.driver.find_element_by_name('email')
        pass_form = self.driver.find_element_by_name('pass')
        login_form.send_keys(self.email)
        pass_form.send_keys('checkfacebook')
        pass_form.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'header_block')))
        self.driver.delete_all_cookies()
        sleep(5)
        if 'Log Into Facebook' in self.driver.page_source:
            return 'Not Found'
        else:
            name = self.driver.find_element_by_xpath("//div[@id='header_block']/span//span").text
            return Check.found + name  # String like 'Found Log in as FirstName LastName'

    def yougoogle_check(self):
        try:
            self.driver.get("https://accounts.google.com/signin/v2/identifier?hl=en")
        except WebDriverException:
            result = "Site could not be reached, try again"
            return result
        try:
            assert "Sign in" in self.driver.title
        except AssertionError:
            result = "Site could not be loaded properly, try again"
            return result
        sleep(1)
        user = self.driver.find_element_by_xpath('//input[@type="email"]')
        user.send_keys(self.email)
        user.send_keys(Keys.ENTER)
        self.driver.delete_all_cookies()
        sleep(1.5)
        try:
            self.driver.find_element_by_name("password")
            return Check.found
        except NoSuchElementException:
            try:
                captcha_enter = self.driver.find_element_by_name("ca")
                captcha_enter.send_keys("test")
                result = Check.Y + "Captcha encountered, you'll have to check this manually" + Check.E
                return result
            except ElementNotInteractableException:
                result = "Not Found"
                return result

    def twitch_check(self):
        try:
            self.driver.get("https://www.twitch.tv/")
        except WebDriverException:
            result = "Site could not be reached, try again"
            return result
        try:
            assert "Discover" in self.driver.page_source
        except AssertionError:
            result = "Site could not be loaded properly, try again"
            return result
        self.driver.find_element_by_xpath("//button[@data-a-target='login-button']").click()
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located
                                             ((By.XPATH, "//input[""@autocomplete='username']")))
        user = self.driver.find_element_by_xpath("//input[@autocomplete='username']")
        password = self.driver.find_element_by_xpath("//input[@type='password']")
        user.send_keys(self.email)
        password.send_keys("123456789")
        password.send_keys(Keys.ENTER)
        self.driver.delete_all_cookies()
        sleep(1.5)
        if "This email is not linked to a Twitch account. Please log in with a username instead." \
                in self.driver.page_source:
            result = "Not Found"
            return result
        else:

            return Check.found
