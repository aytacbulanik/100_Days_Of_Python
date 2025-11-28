from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title) #ekitekin tamamını alır
print(soup.title.string) #ekitekin sadece stringini alır
print(soup.prettify()) #html kodunu düzgün bir şekilde yazdırır
#findall methodu tüm tagleri bulur
all_anchor_tags = soup.find_all(name="a") #tüm a taglerini alır. dizi olarak verir

for tag in all_anchor_tags:
    print(tag.getText()) #taglerin içindeki yazıları alır
    print(tag.get("href")) #taglerin href attribute'ünü alır
#find methodu ilk bulduğu tagi alır
heading = soup.find(name="h1", id="name") #id kısmıyla eşleşen belirli bir tagi alır
print(heading.string)

section_heading = soup.find(name="h3", class_="heading") #class kısmıyla eşleşen belirli bir tagi alır
print(section_heading.string)
company_url = soup.select_one(selector="p a") #css selector kullanarak belirli bir tagi alır
print(company_url)
all_headings = soup.select(selector=".heading") #css selector kullanarak tüm eşleşen tagleri alır
