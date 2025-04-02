import os

import pytest
from selene import browser, have


@pytest.fixture
def browser_setup():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.maximize_window()
    yield
    browser.quit()


def test_filling_all_fields(browser_setup):
    browser.element('#firstName').click().type("Иван")
    browser.element('#lastName').click().type("Иванов")
    browser.element('#userEmail').click().type("ivanov@ya.ru")
    browser.element('[value=Female]').double_click()
    browser.element('[id="userNumber"]').click().type("1234567890")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="2"]').click()
    browser.element('option[value="2000"]').click()
    browser.element('[aria-label = "Choose Thursday, March 2nd, 2000"]').click()
    browser.element('#subjectsInput').double_click().set("accounting")
    browser.element('#react-select-2-option-0').with_(timeout=browser.config.timeout * 2).double_click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture.jpeg'))
    browser.element('[placeholder="Current Address"]').click().type("Москва")
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
