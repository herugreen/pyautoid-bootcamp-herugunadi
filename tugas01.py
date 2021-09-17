from selenium import webdriver

url_list = [
            'https://www.noobtest.id',
            'https://www.erzaf.com',
            'https://www.orangsiber.com',
            'https://www.demoqa.com',
            'https://www.automatetheboringstuff.com'
]

driver = webdriver.Chrome()
driver.minimize_window()

for url in url_list:
    driver.get(url)
    Title = driver.title
    Name = url.replace('https://','')
    print(Name, '-', Title)

driver.close()
