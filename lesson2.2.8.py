from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('M')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("M")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("M")

    # генерация тестового файла
    with open('test1.txt', 'w') as file:
        file.write('test1 for mls 228')

    # прописываем путь к файлу
    import os

    path = os.getcwd() + '/' + file.name

    download = browser.find_element_by_id('file')
    # грузим файл на страницу и отправляем
    download.send_keys(path)

    button = browser.find_element_by_css_selector('button')
    button.click()
finally:
    time.sleep(30)
    browser.quit()