import time
from selenium.webdriver.common.keys import Keys # provee interaccion con el teclas especiales(ENTER, ALT, etc)


def login(driver, user, password):

    driver.get('https://www.linkedin.com/')

    mail = driver.find_element_by_id('session_key')
    mail.clear()
    mail.send_keys(user)

    clave = driver.find_element_by_id('session_password')
    clave.clear()
    clave.send_keys(password)

    time.sleep(3)
    summit = driver.find_element_by_css_selector('button.sign-in-form__submit-button')
    summit.click()


def search(driver, word):
    bar = driver.find_element_by_xpath('//*[@id="ember16"]/input')
    bar.clear()
    bar.send_keys(word)
    bar.send_keys(Keys.RETURN)


def filter(driver):

    driver.find_element_by_xpath('//*[@id="msg-overlay"]/div[1]/header').click()
    time.sleep(2)

    path = r'/html/body/div[7]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div[2]/ul/li[1]/form/'

    xpath = path + r'button/span'
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)

    xpath = path + r'div/fieldset/div/ul/li[1]/label/p/span'
    driver.find_element_by_xpath(xpath).click()
    time.sleep(2)

    xpath = path + r'div/fieldset/div/div/div/button[2]/span'
    driver.find_element_by_xpath(xpath).click()


def select(driver):
    a = 25
    xpath = r'/html/body/div[7]/div[3]/div[3]/div/div/div/div[1]/section/div/ul/'

    dic = []

    for i in list(range(1, a+1)):
        time.sleep(1)
        element = driver.find_element_by_xpath(xpath+'li[{}]/div/div'.format(i))
        element.click()
        tag = element.find_elements_by_tag_name('a')
        driver.execute_script("arguments[0].scrollIntoView()", element)

        dic.append(tag)

    return dic
