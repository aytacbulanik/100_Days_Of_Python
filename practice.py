from selenium import webdriver
from selenium.webdriver.common.by import By #By modülünü import etme

#otomatik kapanmayı engelleme
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions) #option parametresini gönderiyoruz
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")

articelsCount = driver.find_element(By.CSS_SELECTOR, value=".main-plainlist b a")
print(articelsCount.text)
driver.quit()