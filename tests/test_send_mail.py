from src.MailPages import MainPage, InboxPage
from constants import *


def test_send_mail(browser):
    main_page = MainPage(browser)
    main_page.go_to_site(MAIN_URL)
    assert main_page.is_title_match(), 'Заголовок не соответствует ожидаемому'
    main_page.set_email(EMAIL)
    main_page.select_domain(EMAIL_DOMAIN)
    main_page.click_enter_email_button()
    main_page.set_password(PASSWORD)
    main_page.click_authorize_button()
    inbox_page = InboxPage(browser)
    inbox_page.click_compose_button()
    inbox_page.set_recipient_field(RECIPIENT)
    inbox_page.set_subject_field(SUBJECT)
    inbox_page.set_text_field(TEXT)
    inbox_page.click_send_button()
