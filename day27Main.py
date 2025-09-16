import tkinter

window = tkinter.Tk()
window.title("My First GUI Program") #açılan ekrana başlık veriliyor.
window.minsize(width=500,height=300) #ekranın en az bu boyutlarda olması tanımlanıyor.
myLabel = tkinter.Label(text="I am a Label",font=("Arial" , 25 , "bold")) #label için değişken oluşturduk ve text kısmına ne yazacağını belirttik. 
#font parametresi ile yazıtipi özelliklerini veriyoruz
myLabel.pack() #label in ekranda ortaya otomatik olarak yerleşmesini sağladı





window.mainloop() #bu kod ekranla her zaman etkileşime girmek için ve nesnleri dinlemek için yazılmalır. en sonda olmalıdır.