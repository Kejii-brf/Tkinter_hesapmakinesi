#Hesap Makinesi

from tkinter import *

pencere = Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("300x400")
pencere.resizable(FALSE, FALSE)

def hesapmak():
    listsonuc.delete(0, END)
    sayı1 = float(giriş1.get())
    sayı2 = float(giriş2.get())
    sonuc1 = sayı1+sayı2
    sonuc2 = sayı1-sayı2
    sonuc3 = sayı1*sayı2
    sonuc4 = sayı1/sayı2
    try:
        listsonuc.insert(END, f"Toplam: {sonuc1}")
        listsonuc.insert(END, "")
        listsonuc.insert(END, f"Fark: {sonuc2}")
        listsonuc.insert(END, "")
        listsonuc.insert(END, f"Çarpım: {sonuc3}")
        listsonuc.insert(END, "")
        listsonuc.insert(END, f"Bölüm: {sonuc4}")
    except:
        print("Bir hata oluştu!")

sayi = Label(pencere, text="Sayıları girin", font="Verdana 15 bold")
sayi.pack()

sayi1 = Label(pencere, text="Sayı →", font="Verdana 12 italic")
sayi1.place(x=5, y=50)
sayi2 = Label(pencere, text="Sayı →", font="Verdana 12 italic")
sayi2.place(x=5, y=90)

giriş1 = Entry(pencere, font="Verdana 12 bold", fg="blue", justify="center", bg="light gray", width=18)
giriş1.place(x=70, y=55)

giriş2 = Entry(pencere, font="Verdana 12 bold", fg="blue", justify="center", bg="light gray", width=18)
giriş2.place(x=70, y=95)

hesap = Button(pencere, text="Hesapla!", fg="white", bg="gray", font="Verdana 12 bold", command=hesapmak)
hesap.place(x=100, y=135)

sonuç = Label(pencere, text="Sonuç", font="Verdana 15 bold")
sonuç.place(x=105, y=175)

listsonuc = Listbox(pencere, font="Verdana 12 bold", width=23, height=8, fg="white", bg="gray")
listsonuc.place(x=24, y=220)


pencere.mainloop()
