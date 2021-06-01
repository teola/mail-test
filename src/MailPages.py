from src.BaseApp import BasePage
from selenium.webdriver.common.by import By
from constants import *


class MailLocators:
    LOCATOR_EMAIL_FIELD = (By.CSS_SELECTOR, '.email-input')
    LOCATOR_EMAIL_MAIL_DOMAIN = (By.CSS_SELECTOR, '.domain-select > option:nth-child(1)')
    LOCATOR_EMAIL_INBOX_DOMAIN = (By.CSS_SELECTOR, '.domain-select > option:nth-child(2)')
    LOCATOR_EMAIL_LIST_DOMAIN = (By.CSS_SELECTOR, '.domain-select > option:nth-child(3)')
    LOCATOR_EMAIL_BK_DOMAIN = (By.CSS_SELECTOR, '.domain-select > option:nth-child(4)')
    LOCATOR_EMAIL_INTERNET_DOMAIN = (By.CSS_SELECTOR, '.domain-select > option:nth-child(5)')
    LOCATOR_ENTER_EMAIL_BUTTON = (By.CSS_SELECTOR, '.button')
    LOCATOR_PASSWORD_FIELD = (By.CSS_SELECTOR, '.password-input')
    LOCATOR_AUTHORIZE_BUTTON = (By.CSS_SELECTOR, '.second-button')


class MainPage(BasePage):

    def set_email(self, email):
        element = self.find_element(MailLocators.LOCATOR_EMAIL_FIELD)
        element.click()
        element.send_keys(email)
        return element

    def select_domain(self, domain):
        if domain == MAIL_DOMAIN:
            return self.select_mail_domain()
        elif domain == INBOX_DOMAIN:
            return self.select_inbox_domain()
        elif domain == LIST_DOMAIN:
            return self.select_list_domain()
        elif domain == BK_DOMAIN:
            return self.select_bk_domain()
        elif domain == INTERNET_DOMAIN:
            return self.select_internet_domain()
        else:
            raise ValueError(domain + ' is unacceptable domain name.')

    def select_mail_domain(self):
        element = self.find_element(MailLocators.LOCATOR_EMAIL_MAIL_DOMAIN)
        element.click()
        return element

    def select_inbox_domain(self):
        element = self.find_element(MailLocators.LOCATOR_EMAIL_INBOX_DOMAIN)
        element.click()
        return element

    def select_list_domain(self):
        element = self.find_element(MailLocators.LOCATOR_EMAIL_LIST_DOMAIN)
        element.click()
        return element

    def select_bk_domain(self):
        element = self.find_element(MailLocators.LOCATOR_EMAIL_BK_DOMAIN)
        element.click()
        return element

    def select_internet_domain(self):
        element = self.find_element(MailLocators.LOCATOR_EMAIL_INTERNET_DOMAIN)
        element.click()
        return element

    def click_enter_email_button(self):
        return self.find_element(MailLocators.LOCATOR_ENTER_EMAIL_BUTTON).click()

    def set_password(self, password):
        element = self.find_element(MailLocators.LOCATOR_PASSWORD_FIELD)
        element.click()
        element.send_keys(password)
        return element

    def click_authorize_button(self):
        return self.find_element(MailLocators.LOCATOR_AUTHORIZE_BUTTON).click()

    def is_title_match(self):
        return MAIN_TITLE in self.driver.title


class InboxLocators:
    LOCATOR_COMPOSE_BUTTON = (By.CSS_SELECTOR, '.compose-button__txt')
    LOCATOR_RECIPIENT_FIELD = (By.CSS_SELECTOR, '.container--ItIg4 > div:nth-child(1) > input:nth-child(1)')
    LOCATOR_SUBJECT_FIELD = (By.CSS_SELECTOR, '.container--3QXHv > div:nth-child(1) > input:nth-child(1)')
    LOCATOR_TEXT_FIELD = (By.XPATH, '/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]')
    LOCATOR_SEND_BUTTON = (By.CSS_SELECTOR, 'span.button2_base:nth-child(1) > span:nth-child(1)')


class InboxPage(BasePage):
    def click_compose_button(self):
        return self.find_element(InboxLocators.LOCATOR_COMPOSE_BUTTON).click()

    def set_recipient_field(self, recipient):
        element = self.find_element(InboxLocators.LOCATOR_RECIPIENT_FIELD)
        element.click()
        element.send_keys(recipient)
        return element

    def set_subject_field(self, subject):
        element = self.find_element(InboxLocators.LOCATOR_SUBJECT_FIELD)
        element.click()
        element.send_keys(subject)
        return element

    def set_text_field(self, text):

        element = self.find_element(InboxLocators.LOCATOR_TEXT_FIELD)
        element.send_keys(text)
        return element

    def click_send_button(self):
        return self.find_element(InboxLocators.LOCATOR_SEND_BUTTON).click()
