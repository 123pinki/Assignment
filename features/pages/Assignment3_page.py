from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from faker import Faker
faker = Faker()


class Keyword:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_website(self):
        self.driver.get("https://stride.ai/texsie/")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def keyword_identifier(self, section_name):
        sleep(5)
        section = self.driver.find_elements_by_xpath("//*[@id='nav-2']/div")
        for name in section:
            print(name)
            if name.text == section_name:
                name.click()

    def random_text(self):
        self.driver.find_element_by_id("randomize_identify").click()

    def save_random_text1(self):
        ran_text = self.driver.find_element_by_id("text-identify")
        ran_text.get_attribute('value')

    def analyze_section(self):
        self.driver.find_element_by_id("analyze-identify").click()

    def identifier_text(self):
        add_text = self.driver.find_element_by_id("text-identify")
        add_text.clear()
        add_text.send_keys("Hello everyone")

    def compression_ratio(self):
        self.driver.find_element_by_css_selector("[title='20']").click()

    def summarization_text(self):
        summ_text = self.driver.find_element_by_id("text-summary")
        summ_text.send_keys("summarization section")

    def sentiment_analysis_text(self):
        sent_text = self.driver.find_element_by_id("text-sentiment")
        sent_text.send_keys("sentiment analysis section")

    def language(self):
        self.driver.find_element_by_id("sentiment-language").click()
        self.driver.find_element_by_id("sentiment-english").click()

    def click_on_settings(self, setting_name):
        sleep(5)
        settings = self.driver.find_elements_by_xpath("//*[@id='nav-link']/li/a")
        for item in settings:
            if item.text in setting_name:
                item.click()
                break

    def home_page(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "request-demo")))

    def about_page(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "aboutus")))

    def technology_page(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "technology")))

    def solution_page(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "sol-h1-D")))

    def team_page(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "team-h1-D")))

    def contact(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, "team-h1-D")))

    def full_name(self):
        settings = self.driver.find_element_by_xpath("//*[@id='nav-link']/li[6]/a")
        settings.send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        name = faker.name()
        full_name = self.driver.find_element_by_id("demo_name")
        full_name.send_keys(name)

    def email(self):
        email = faker.email()
        email_id = self.driver.find_element_by_name("email")
        email_id.send_keys(email)

    def phone_number(self):
        number = faker.phone_number()
        phn_number = self.driver.find_element_by_name("phone")
        phn_number.send_keys(number)

    def enter_text(self):
        text = faker.text()
        message = self.driver.find_element_by_name("message")
        message.send_keys(text)

    def save_detail(self):
        self.driver.find_element_by_class_name("btn-blue").click()

    def close_contact_section(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "close")))
        self.driver.find_element_by_class_name("close").click()
        self.driver.refresh()
