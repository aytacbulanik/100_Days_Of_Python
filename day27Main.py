from tkinter import * #tkinter modülündeki herşeyi import ediyoruz.

window = Tk()
window.title("My First GUI Program") #açılan ekrana başlık veriliyor.
window.minsize(width=500,height=300) #ekranın en az bu boyutlarda olması tanımlanıyor.
myLabel = Label(text="I am a Label",font=("Arial" , 25 , "bold")) #label için değişken oluşturduk ve text kısmına ne yazacağını belirttik. 
#font parametresi ile yazıtipi özelliklerini veriyoruz
myLabel.pack() #label in ekranda ortaya otomatik olarak yerleşmesini sağladı
#Labelda olan yazıya atama yapıyoruz
def clickedButton():
    myLabel.config(text="Button Clicked")
def clickedButton2():
    myLabel.config(text=myTextField.get()) #entry in get metodu o anki yazılanı almaya yarıyor.
myButton = Button(text="Click Me",command=clickedButton2) #command propertisi her tıklanmada çalışacak fonksiyonu alıyor.
myButton.pack()

#Entry textfield gibi kullanıcıdan veri almaya yarıyor.
myTextField = Entry()
myTextField.insert(END,"please some things")
myTextField.pack()

#textview olarak da Text componenti kullanılmaktadır.
myText = Text(width=20,height=5)
myText.insert(END,"")
myText.focus() #cursor un direk bu componente odaklanmasını sağlıyor
myText.get("1.0",END) #textView da olan değeri almaya yarıyor
myText.pack()
#spinboxtaki her tıklanmada o anki değeri almaya yarayan fonksyondur.
def getSayac():
    print(mySpinbox.get())
#spinbox sayac gibi olan componenti belirtmektedir.
mySpinbox = Spinbox(from_=0,to=5,width=3,command=getSayac)
mySpinbox.pack()

def getScale(value):
    print(value) #scale de mevcud değeri almak için bu parametre kullanılıyor.
#scale comp kaydırmalı bir çubuk olarak tanımlanıyor.
myScale = Scale(from_=0,to=50,command=getScale)
myScale.pack()

def getCheckValue():
    print(checkedState.get()) #kapalı yada açık değeri 1 ve 0 olarak veriyor
#tek checkbox için bu şekilde tanımlanıyor.
checkedState = IntVar() #kapalı açık durumu checkbox ta bu değişkenle takip edeceğiz.
myCheckButton = Checkbutton(text="is On",variable=checkedState,command=getCheckValue)
myCheckButton.pack()


def checkRadioState():
    print(radioState.get()) #hangi değerin seçili olduğunu yakalayan bir code
radioState = IntVar()
# checkbox ın gruplanmış halidir.value değeri benzersi olmalı ki hangi değerin seçildiği anlaşılsın.variable ise Intvar tipinde
# olup değeri yakalıyor. checkRadioState fonksiyonu ise değer değiştiğinde çağrılan fonksiyondur.
radioButton1 = Radiobutton(text="Değer 1",value=1,variable=radioState,command=checkRadioState) 
radioButton2 = Radiobutton(text="Değer 2",value=2,variable=radioState,command=checkRadioState)
radioButton3 = Radiobutton(text="Değer 3",value=3,variable=radioState,command=checkRadioState)
radioButton1.pack()
radioButton2.pack()
radioButton3.pack()

def listboxUsed(event):
    print(myListBox.get(myListBox.curselection())) #listbox da seçili değeri almak için bu kodu yazıyoruz.

myListBox = Listbox(height=4) #oluşturuken genel yüksekliği veriliyor.
furits = ["Elma","Kayısı","Şeftali","Çilek"] #listbox ın içerisinde yazılacak değerler
for item in furits:
    myListBox.insert(furits.index(item) , item) #döngüye sokarak listedeki değerler listbox a ekleniyor.
myListBox.bind("<<ListboxSelect>>" , listboxUsed) 
myListBox.pack()

window.mainloop() #bu kod ekranla her zaman etkileşime girmek için ve nesnleri dinlemek için yazılmalır. en sonda olmalıdır.