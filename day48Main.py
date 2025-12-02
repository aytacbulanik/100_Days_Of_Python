from selenium import webdriver
from selenium.webdriver.common.by import By #By modülünü import etme

#otomatik kapanmayı engelleme
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions) #option parametresini gönderiyoruz
driver.get("https://www.python.org/")
# priceTL = driver.find_element(By.CLASS_NAME, value="a-price-whole") #sınıf adına göre elementi bulma
# priceKurus = driver.find_element(By.CLASS_NAME, value="a-price-fraction") #sınıf adına göre elementi bulma
# print(f"Fiyat: {priceTL.text},{priceKurus.text} TL")

searchBox = driver.find_element(By.NAME, value="q") #name attribute'una göre elementi bulma
print(searchBox.tag_name) #elementin etiket ismini yazdırma
driver.quit()