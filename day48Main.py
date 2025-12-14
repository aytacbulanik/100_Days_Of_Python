from selenium import webdriver
from selenium.webdriver.common.by import By #By modülünü import etme
from selenium.webdriver.common.keys import Keys #Keys modülünü import etme
import time
#otomatik kapanmayı engelleme
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions) #option parametresini gönderiyoruz
# driver.get("https://www.python.org/")
# # priceTL = driver.find_element(By.CLASS_NAME, value="a-price-whole") #sınıf adına göre elementi bulma
# # priceKurus = driver.find_element(By.CLASS_NAME, value="a-price-fraction") #sınıf adına göre elementi bulma
# # print(f"Fiyat: {priceTL.text},{priceKurus.text} TL")

# searchBox = driver.find_element(By.NAME, value="q") #name attribute'una göre elementi bulma
# print(searchBox.get_attribute("placeholder")) #elementin placeholderı yazdırma
# button = driver.find_element(By.ID, value="submit") #id attribute'una göre elementi bulma
# print(button.size) #elementin boyutlarını yazdırma
# documentationLink = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a") #bir class içerisinde bulunan a etiketine göre elementi bulma
# print(documentationLink.text) #elementin textini yazdırma

# #sitedeki elementin yolunu kullanarakta erişim sağlayabiliriz. copy dedikten sonra xpath seçilmeli
# bugLink = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[2]/a')
# print(bugLink.text) #elementin textini yazdırma

# eventLink = driver.find_element(By.CSS_SELECTOR , value=".event-widget li a") #event-widget class'ı altındaki tüm li etiketlerindeki a etiketlerini bulma
# enentTime = driver.find_elements(By.CSS_SELECTOR , value=".event-widget time") #event-widget class'ı altındaki tüm li etiketlerindeki time etiketlerini bulma
# events = {}
# for n in range(len(eventLink)):
#     events[n] = {
#         "time": enentTime[n].text,
#         "name": eventLink[n].text
#     }
# print(events)
# driver.quit()
# linkGo = driver.find_element(By.LINK_TEXT , value="Python Meeting Düsseldorf") #link text kullanarak elementi bulma
# linkGo.click() #elemente tıklama işlemi

# driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
# search = driver.find_element(By.NAME , value="search")
# search.send_keys("Python",Keys.ENTER) #elemente metin gönderme işlemi
driver.get("https://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element(By.NAME , value="fName")
fName.send_keys("John")
lName = driver.find_element(By.NAME , value="lName")
lName.send_keys("Waiting")
email = driver.find_element(By.NAME , value="email")
email.send_keys("a@domain.com")
button = driver.find_element(By.XPATH, value='/html/body/form/button')
button.click()