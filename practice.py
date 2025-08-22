with open("myFile.txt") as file:
    content = file.read()
    print(content)

with open("myFile.txt",mode="a") as file:
    content = file.write("bu dosyaya yeni yazılan şeydir.")