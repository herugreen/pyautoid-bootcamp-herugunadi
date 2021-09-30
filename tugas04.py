from selenium import webdriver

driver =  webdriver.Chrome()
driver.maximize_window()

driver.get('https://demoqa.com/text-box')

driver.find_element_by_id("userName").send_keys("Heru")
driver.find_element_by_id("userEmail").send_keys("herugunadi@yahoo.com")
driver.find_element_by_id("currentAddress").send_keys("Jl. Kesempatan Kedua")
driver.find_element_by_id("permanentAddress").send_keys("Jl. Kesempatan Kedua Bahagia No. 46")

driver.find_element_by_id('submit').click()

print("Berhasil")