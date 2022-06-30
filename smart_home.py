from msilib import Table
import tkinter as tk
from xmlrpc.client import Boolean



root = tk.Tk()
root.title('Vrata')


status=[]

def key():
    rezultat_kuhinja.configure()

     

frame_vrata= tk.Frame(root,width=100,height=200, borderwidth=2, relief=tk.RIDGE)
frame_vrata.grid(row=0,column=0,padx=10,pady=10)

button_ulazna= tk.Button(frame_vrata, text="Ulazna",fg="purple")#funkcija!!!
button_ulazna.grid(column=0,row=1,padx=10,pady=10)
rezultat_ulazna= tk.Label(frame_vrata,text="Otključano")
rezultat_ulazna.grid(column=1,row=1,padx=10,pady=10)

button_kuhinja= tk.Button(frame_vrata, text="Kuhinja",fg="purple")#funkcija!!!
button_kuhinja.grid(column=0,row=2,padx=10,pady=10)
rezultat_kuhinja= tk.Label(frame_vrata,text="Otključano")
rezultat_kuhinja.grid(column=1,row=2,padx=10,pady=10)

button_kupaona= tk.Button(frame_vrata, text="Kupaonica",fg="purple")#funkcija!!!
button_kupaona.grid(column=0,row=3,padx=10,pady=10)
rezultat_kupaona= tk.Label(frame_vrata,text="Otključano")
rezultat_kupaona.grid(column=1,row=3,padx=10,pady=10)

button_spavaca= tk.Button(frame_vrata, text="Spavaća soba",fg="purple")#funkcija!!!
button_spavaca.grid(column=0,row=4,padx=10,pady=10)
rezultat_spavaca= tk.Label(frame_vrata,text="Otključano")
rezultat_spavaca.grid(column=1,row=4,padx=10,pady=10)

button_dnevna= tk.Button(frame_vrata, text="Dnevna soba",fg="purple")#funkcija!!!
button_dnevna.grid(column=0,row=5,padx=10,pady=10)
rezultat_dnevna= tk.Label(frame_vrata,text="Otključano")
rezultat_dnevna.grid(column=1,row=5,padx=10,pady=10)

button_balkon= tk.Button(frame_vrata, text="Balkon",fg="purple")#funkcija!!!
button_balkon.grid(column=0,row=6,padx=10,pady=10)
rezultat_balkon= tk.Label(frame_vrata,text="Otključano")
rezultat_balkon.grid(column=1,row=6,padx=10,pady=10)









root.mainloop()