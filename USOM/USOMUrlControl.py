from tkinter import*
import datetime

def kontrol_et():
    dosya = open("USOM/usom.txt", "r")
    icerik = dosya.read()
    dosya.close()
    ip = entry1.get()
    bugun = datetime.datetime.now()
    if str(ip) in icerik:
        dosya=open("USOM/log.txt", "a")
        yazi = str(ip) + " -> zararlı\ntarih: "+str(bugun)+"\n\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararlıdır")
    else:
        dosya = open("USOM/log.txt", "a")
        yazi = str(ip) + " -> zararlı değil\ntarih: "+str(bugun)+"\n\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararlı değildir")

top = Tk()
top.title("USOM IP Kontrol")
B = Button(top, text="Kontrol et", command= kontrol_et)
B.place(x=50, y=50)
B.pack()
label1 = Label(top, text="Kontrol edilecek URL'i giriniz: ")
label1.place(x=50, y=70)
entry1 = Entry(top)
entry1.place(x=50, y=90)
v = StringVar()
entry2 = Entry(top, textvariable=v)
entry2.place(x=50, y=100)
entry2.pack()
top.mainloop()