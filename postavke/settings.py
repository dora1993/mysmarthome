from msilib import Table
import tkinter as tk
import datetime as dt
from tkinter.colorchooser import askcolor

root = tk.Tk()
root.title('Vrata')

boje=["#F8BBD0","#81D4FA","#80DEEA","#B39DDB","#C5E1A5"]
def pozadina():
    colors = askcolor(title="Tkinter Color Chooser")
    root.configure(bg=colors[1])
        
        
        

def key():
    rezultat_ulazna.configure("Zaključano")
    rezultat_kuhinja.configure("Zaključano")
    rezultat_kupaona.configure("Zaključano")
    rezultat_spavaca.configure("Zaključano")
    rezultat_dnevna.configure("Zaključano")
    rezultat_balkon.configure("Zaključano")

def clock():
        date_time = dt.datetime.now().strftime("%A, %d.%B.%Y, %H:%M:%S")
        date,time1 = date_time.split()
        time2,time3 = time1.split('/')
        hour,minutes,seconds =  time2.split(':')
        if int(hour) > 12 and int(hour) < 24:
                time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
        else:
                time = time2 + ' ' + time3
        frame_vrime.config(text = time)
        frame_vrime.config(text= date)
        frame_vrime.after(1000, clock)

frame_vrijeme= tk.Frame(root,width=200,height=100, borderwidth=2, relief=tk.RIDGE)
frame_vrijeme.grid(row=0,column=1,padx=10,pady=10)
vrijeme=dt.datetime.now().strftime("%A, %d.%B.%Y, %H:%M:%S") 
frame_vrime= tk.Label(frame_vrijeme,text=vrijeme,font=("Ariel",15))

frame_vrime.grid(row=0,column=1,padx=10,pady=10) 

frame_boje =tk.Frame(root,width=200,height=100)
frame_boje.grid(row=1,column=1,padx=10,pady=10)
boje_poz=tk.Button(frame_boje,text="Promijeni boju",command=pozadina)#funkcija
boje_poz.grid(row=1,column=1,padx=10,pady=10)

frame_vrata= tk.Frame(root,width=100,height=200, borderwidth=2, relief=tk.RIDGE)
frame_vrata.grid(row=0,column=0,padx=10,pady=10)

button_ulazna= tk.Button(frame_vrata, text="Ulazna",fg="purple",command=key)#funkcija!!!
button_ulazna.grid(column=0,row=1,padx=10,pady=10)
rezultat_ulazna= tk.Label(frame_vrata,text="Otključano")
rezultat_ulazna.grid(column=1,row=1,padx=10,pady=10)

button_kuhinja= tk.Button(frame_vrata, text="Kuhinja",fg="purple",command=key)#funkcija!!!
button_kuhinja.grid(column=0,row=2,padx=10,pady=10)
rezultat_kuhinja= tk.Label(frame_vrata,text="Otključano")
rezultat_kuhinja.grid(column=1,row=2,padx=10,pady=10)

button_kupaona= tk.Button(frame_vrata, text="Kupaonica",fg="purple",command=key)#funkcija!!!
button_kupaona.grid(column=0,row=3,padx=10,pady=10)
rezultat_kupaona= tk.Label(frame_vrata,text="Otključano")
rezultat_kupaona.grid(column=1,row=3,padx=10,pady=10)

button_spavaca= tk.Button(frame_vrata, text="Spavaća soba",fg="purple",command=key)#funkcija!!!
button_spavaca.grid(column=0,row=4,padx=10,pady=10)
rezultat_spavaca= tk.Label(frame_vrata,text="Otključano")
rezultat_spavaca.grid(column=1,row=4,padx=10,pady=10)

button_dnevna= tk.Button(frame_vrata, text="Dnevna soba",fg="purple",command=key)#funkcija!!!
button_dnevna.grid(column=0,row=5,padx=10,pady=10)
rezultat_dnevna= tk.Label(frame_vrata,text="Otključano")
rezultat_dnevna.grid(column=1,row=5,padx=10,pady=10)

button_balkon= tk.Button(frame_vrata, text="Balkon",fg="purple",command=key)#funkcija!!!
button_balkon.grid(column=0,row=6,padx=10,pady=10)
rezultat_balkon= tk.Label(frame_vrata,text="Otključano")
rezultat_balkon.grid(column=1,row=6,padx=10,pady=10)









root.mainloop()