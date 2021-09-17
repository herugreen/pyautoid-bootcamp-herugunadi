from selenium import webdriver
import time

driver =  webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe') 
driver.get('https://demoqa.com/webtables')

driver.maximize_window()

driver.find_element_by_id("addNewRecordButton").click()

#data1
driver.find_element_by_id("firstName").send_keys("Heru")
driver.find_element_by_id("lastName").send_keys("Gunadi")
driver.find_element_by_id("userEmail").send_keys("crayonshinchan@yahoo.com")
driver.find_element_by_id("age").send_keys("17")
driver.find_element_by_id("salary").send_keys("10000000")
driver.find_element_by_id("department").send_keys("IT")
driver.find_element_by_id("submit").click()

time.sleep(2)

driver.find_element_by_id("addNewRecordButton").click()

#data2
driver.find_element_by_id("firstName").send_keys("Dian")
driver.find_element_by_id("lastName").send_keys("Sastro")
driver.find_element_by_id("userEmail").send_keys("diansatrouhuy@gmail.com")
driver.find_element_by_id("age").send_keys("28")
driver.find_element_by_id("salary").send_keys("15000000")
driver.find_element_by_id("department").send_keys("Marketing")
driver.find_element_by_id("submit").click()

time.sleep(2)

driver.find_element_by_id("addNewRecordButton").click()

#data3
driver.find_element_by_id("firstName").send_keys("Den Bagus")
driver.find_element_by_id("lastName").send_keys("Tjokroaminoto")
driver.find_element_by_id("userEmail").send_keys("denbagus@gmail.com")
driver.find_element_by_id("age").send_keys("25")
driver.find_element_by_id("salary").send_keys("12000000")
driver.find_element_by_id("department").send_keys("Produksi")
driver.find_element_by_id("submit").click()
