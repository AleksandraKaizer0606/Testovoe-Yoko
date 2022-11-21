import time


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://hh.kz/")

time.sleep(5)

#Авторизация
button_login = driver.find_element_by_css_selector('[data-qa="login"]')
button_login.click()

time.sleep(5)

button_enter_by_password = driver.find_element_by_css_selector('[data-qa="expand-login-by-password"]')
button_enter_by_password.click()

field_login = driver.find_element_by_css_selector('[data-qa="login-input-username"]')
field_login.send_keys("binavas557@sunetoa.com")

field_password = driver.find_element_by_css_selector('[data-qa="login-input-password"]')
field_password.send_keys("ntcnntcn")

button_enter = driver.find_element_by_css_selector('[data-qa="account-login-submit"]')
button_enter.click()

time.sleep(5)

#Переход на главную страницу
driver.get("https://hh.kz/")

#В поиске найти компанию “Yoko”
find_field = driver.find_element_by_id('a11y-search-input')
find_field.click()
find_field.send_keys("Yoko")

find_button = driver.find_element_by_css_selector('[data-qa="search-button"]')
find_button.click()

time.sleep(5)

#Найти вакансию тестировщика
vacancy_link = driver.find_element_by_partial_link_text('Тестировщик')
vacancy_link.click()

time.sleep(5)

driver.switch_to.window(driver.window_handles[1])

#Добавить вакансию в избранное
heart_button = driver.find_element_by_css_selector('[data-qa="vacancy-body-mark-favorite_false"]')
heart_button.click()

time.sleep(5)

#Удостовериться что вакансия добавлена в избранные
favourite_vacancies_button = driver.find_element_by_css_selector('[data-qa="mainmenu_favVacancies"]')
favourite_vacancies_button.click()

time.sleep(5)

favourite_vacancy_QA = driver.find_element_by_css_selector('[data-qa="serp-item__title"]')

driver.quit()