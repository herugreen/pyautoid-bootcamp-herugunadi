from selenium import webdriver

driver =  webdriver.Chrome()
driver.maximize_window()

driver.get('https://demoqa.com/webtables')

users = [
        {'firstName':'Heru', 'lastName':'Gunadi', 'userEmail':'crayonshinchan@yahoo.com', 'age':'17', 'salary':'10000000', 'department':'IT'},
        {'firstName':'Dian', 'lastName':'Sastro', 'userEmail':'diansatrouhuy@gmail.com', 'age':'28', 'salary':'15000000', 'department':'IT'},
        {'firstName':'Den Bagus', 'lastName':'Tjokroaminoto', 'userEmail':'denbagus@gmail.com', 'age':'25', 'salary':'12000000', 'department':'IT'}
        ]

for user in users:

    driver.find_element_by_id('addNewRecordButton').click()

    for key in user:
        driver.find_element_by_id(key).send_keys(user[key])

    driver.find_element_by_id('submit').click()
