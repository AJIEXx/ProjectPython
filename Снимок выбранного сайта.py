# Будет лучше, если реализовать в headless режиме. Как идея — бот для автоматического создания контента:
#
# Взять текст, обработать его;
# По ключевому слову найти картинку;
# Заскринить её;
# Сформировать в единый пост;
# Нужен лишь selenium, для хеадлесс режима можно PhantomJS

import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


script_name = sys.argv[0]

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

try:
    url = sys.argv[1]

    driver.get(url)
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    driver.save_screenshot('screenshot.png')
    driver.quit()
    print("SUCCESS")

except IndexError:
    print('Usage: %s URL' % script_name)