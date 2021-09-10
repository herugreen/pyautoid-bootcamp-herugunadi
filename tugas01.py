from selenium import webdriver
import time

driver =  webdriver.Chrome(executable_path='C://chromedriver_win32/chromedriver.exe') 

driver.get('https://www.noobtest.id')
driver.get('https://www.erzaf.com')
driver.get('https://www.orangsiber.com')
driver.get('https://www.demoqa.com')
driver.get('https://www.automatetheboringstuff.com')

driver.close()

webtester = ('noobtest.id - Noob Test | A Platform for Noob Software Testers',
            'erzaf.com - Erzaf - an IT Engginer',
            'orangsiber.com - Home - Orang Siber',
            'demoqa.com  ToolsQA',
            'automatetheboringstuff.com - Automate the Boring Stuff with Python')

time.sleep(2)

for web in webtester:
    print(web)
