from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    window.after_cancel(timer) #çalışan sayacı sıfırlamak için kullanılır. çalışan sayaca timer adı verildi ve erişildi.
    global reps 
    reps = 0
    timerLabel.config(text="TIMER")
    canvas.itemconfig(timerText, text="00:00")
    pomodoroLabel.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        countDown(60)
        timerLabel.config(text="WORK" , fg=RED)
        reps += 1
    elif reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countDown(SHORT_BREAK_MIN * 60)
        timerLabel.config(text="BREAK")
        reps += 1
    else:
        countDown(LONG_BREAK_MIN * 60)
        timerLabel.config(text="LONG BREAK")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    countMin = math.floor(count / 60) #dakikaya ulaşmak için toplam saniyeyi 60 a bölüp tam kısmını alıyoruz.
    countSec = count % 60 #saniyeyi bulmak için mod 60 alıyoruz.
    if countSec < 10:
        countSec = f"0{countSec}" #tek basamak olmasın diye başına sıfır ekliyoruz.
    if countMin < 10:
        countMin = f"0{countMin}" #dakika tek basamak olunca başına sıfır ekliyor.
    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}") #canvası güncellemek için itemconfig kullanılıyor. 
    if count > 0:
        global timer
        timer = window.after(1000,countDown,count - 1) #1000 mili saniye bekleyerek recursive fonk çağırıyoruz. sayacı azaltıyoruz
    else:
        startTimer() #süre bittiğinde tekrar fonksiyon çalışsın ve bir sonraki adıma geçsin diye fonk tekrar çağırıyoruz.
        mark = ""
        workSessions = math.floor(reps/2) #hangi bölümde olduğunu anlamak için bu yapılıyor.
        for _ in range(workSessions):
            mark += "✔"
        pomodoroLabel.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50 , bg=YELLOW)

canvas = Canvas(width=200,height=230, bg=YELLOW, highlightthickness=0) #ekrana bir resim eklemek istediğimizde bu sınıfı kullanacağız.
#canvas içerisindeki simgelere kenarlık istemiyorsak highlightthickness 0 vermeliyiz.
tomatoPath = PhotoImage(file="tomato.png") #resmin olduğu dosya yoluna erişmek için kullanıyoruz.
canvas.create_image(100,115,image=tomatoPath) #hangi resmi kullanacağımızı ve konumladıracağımızı söylüyoruz.
timerText = canvas.create_text(100,130, text="00:00" ,fill="white", font=(FONT_NAME,30,"bold"))#metin ekliyoruz ve buna konum yazı rengi 
#yazı tipi gibi parametrelerle şekillendiriyoruz.
canvas.grid(column=1,row=1)

timerLabel = Label(text="Timer" , font=(FONT_NAME,40),fg=GREEN ,bg=YELLOW)
timerLabel.grid(column=1,row=0)

startButton = Button(text="Start",highlightthickness=0 , command=startTimer)
startButton.grid(column=0,row=2)

resetButton = Button(text="Reset",highlightthickness=0,command=resetTimer)
resetButton.grid(column=2,row=2)

pomodoroLabel = Label(font=(FONT_NAME,10),fg=GREEN,bg=YELLOW)
pomodoroLabel.grid(column=1,row=3)

window.mainloop()