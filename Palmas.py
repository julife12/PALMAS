# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:19:10 2022

@author: julian
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
  
window = tk.Tk()
window.title("Palmas")
window.geometry('1000x550')
  

lbl1 = Label(window, text="Entradas", bg="gray")
lbl1.place(x=10, y=10, width=100, height=30)

lbl2 = Label(window, text="Proceso", bg="gray")
lbl2.place(x=450, y=10, width=100, height=30)

lbl3 = Label(window, text="Salida", bg="gray")
lbl3.place(x=890, y=10, width=100, height=30)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()
var9 = tk.IntVar()
var10 = tk.IntVar()
var11 = tk.IntVar()
var12 = tk.IntVar()
var13 = tk.IntVar()

#germen marron, fototoxicidad por pesticidas
c1 = tk.Checkbutton(window, text='Mancha de color crema',variable=var1, onvalue=1, offvalue=0)
c1.pack()
c1.place(x=10, y=50, height=30)

#germen marron
c2 = tk.Checkbutton(window, text='moho verde',variable=var2, onvalue=2, offvalue=0)
c2.place(x=10, y=80, height=30)
#fototoxicidad por pesticidas
c3 = tk.Checkbutton(window, text='Radícula marron',variable=var3, onvalue=3, offvalue=0)
c3.place(x=10, y=110, height=30)
#fototoxicidad por pesticidas
c4 = tk.Checkbutton(window, text='Radícula hinchada',variable=var4, onvalue=4, offvalue=0)
c4.place(x=10, y=140, height=30)
#Marchitez sorpresiva Phytomonas  P.   staheli  cogollo  
c5 = tk.Checkbutton(window, text='Colorización en los folíolos',variable=var5, onvalue=5, offvalue=0)
c5.place(x=10, y=170, height=30)
#Marchitez sorpresiva  P.   staheli
c6 = tk.Checkbutton(window, text='Comcpactación de folíolos',variable=var6, onvalue=6, offvalue=0)
c6.place(x=10, y=200, height=30)
#Marchitez sorpresiva Phytomonas
c7 = tk.Checkbutton(window, text='Secado de la lamina foliar',variable=var7, onvalue=7, offvalue=0)
c7.place(x=10, y=230, height=30)
#Marchitez sorpresiva  P.   staheli Phytomonas
c8 = tk.Checkbutton(window, text='pudrición ded raices',variable=var8, onvalue=8, offvalue=0)
c8.place(x=10, y=260, height=30)
#Marchitez sorpresiva Phytomonas
c9 = tk.Checkbutton(window, text='Necrosis en tejidos internos',variable=var9, onvalue=9, offvalue=0)
c9.place(x=10, y=290, height=30)
#cogollo  
c10 = tk.Checkbutton(window, text='Larvas en tejido podrido',variable=var10, onvalue=10, offvalue=0)
c10.place(x=10, y=320, height=30)
#cogollo  
c11 = tk.Checkbutton(window, text='hongos en foliolos',variable=var11, onvalue=11, offvalue=0)
c11.place(x=10, y=350, height=30)
#anillo marrón
c12 = tk.Checkbutton(window, text='Racimos secos',variable=var12, onvalue=12, offvalue=0)
c12.place(x=10, y=380, height=30)
#anillo marrón
c13 = tk.Checkbutton(window, text='zona circular marrón dentro del tronco',variable=var13, onvalue=13, offvalue=0)
c13.place(x=10, y=410, height=30)

entry = Text()
entry.place(x=750, y=50, height=280, width=220)
# Esta segunda caja de texto no puede recibir el foco
# vía la tecla Tab.
entry2 = Text()
entry2.place(x=750, y=350, height=150, width=220)

img = tk.PhotoImage('img1.jpeg')
lbl_img = tk.Label(window, image = img)
lbl_img.pack()

def saludar():
    entry.delete('1.0',END)
    entry2.delete('1.0',END)
    if var1.get() == 1:       
        
        if (var2.get()==2) & (var3.get()!= 3):

            entry.insert(tk.INSERT,"GERMEN MARRON              Explicación: Afecciones caudatas  por los hongos Aspergilus sp y Penicilium")
            entry2.insert(tk.INSERT,"Prevención: Humedad de la semilla por debajo de 19% y tratamiento con mezcla fungicida-bacteriana (Thiram más Estreptomicina).")
        elif var3.get() ==3:
            if var4.get()==4:
                entry.insert(tk.INSERT,"FITOTOXICIDAD           Algunos  productos  que se emplean  en  el  tratamiento   de    las   semillas   tienen   efectos  fitotóxicos.   Se   mencionan   aquellos  a  base  de  BHC-gama,  cobre  y  mercurio. ")
                entry2.insert(tk.INSERT,"Prevención: Cambiar los  pesticidas o llegar a la fuente de la intoxicación de la planta.")

                
    elif var5.get() == 5:
        if var6.get() == 6:
            if var7.get() == 7:
                if (var12.get() == 12) & (var10.get() == 10) & (var13.get() == 13):
                    entry.insert(tk.INSERT,"Anillo MARRON              Explicación:Esta enfermedad es causada por el nematodo Bursaphelenchus cocophilus, cuyo vector es el insecto picudo negro, Rhynchophorus palmarum.  ")
                    entry2.insert(tk.INSERT,"PREVENCIÓN: Maneje los desechos de poda, cosecha o prácticas agronómicas. Implemente trampeo perimetral del insecto vector. No ubique trampas dentro del lote.")

                elif var8.get() == 8:
                    if var9.get() == 9:
                        entry.insert(tk.INSERT,"MARCHITEZ SORPRESIVA POR Phytomonas  P: Explicación: La Marchitez sorpresiva (MS) es una enfermedad letal que está presente en las cuatro zonas palmeras del país. Afecta principalmente las palmas jóvenes desde el inicio de su etapa productiva. Ha sido asociada a un protozoario flagelado (Phytomonas sp.) que se localiza en el floema de la palma. ")
                        entry2.insert(tk.INSERT,"PREVENCIÓN:Detecte la palma enferma y delimite dos anillos de palma para aplicar un insecticida con registro ICA, cubriendo los follajes y la vegetación circundante.  Elimine la palma enferma.")

            elif var8.get() == 8 :
                entry.insert(tk.INSERT,"MARCHITEZ SORPRESIVA POR P.   staheli:  La Marchitez sorpresiva (MS) es una enfermedad letal que está presente en las cuatro zonas palmeras del país. Afecta principalmente las palmas jóvenes desde el inicio de su etapa productiva.")
                entry2.insert(tk.INSERT,"PREVENCIÓN:Detecte la palma enferma y delimite dos anillos de palma para aplicar un insecticida con registro ICA, cubriendo los follajes y la vegetación circundante.  Elimine la palma enferma.")

        elif var11.get() == 11:
            if var8.get() == 8:
                if var9.get() == 9:
                    if var10.get() == 10:
                        entry.insert(tk.INSERT,"COGOLLO:                  EXPLICACIÓN: La Pudrición del Cogollo (PC) ha sido la plaga más devastadora de la palma de aceite en América Latina. Los síntomas de la enfermedad se caracterizan por la pudrición de todos los nuevos tejidos, conservándose las hojas que se formaron antes de la infección.")
                        entry2.insert(tk.INSERT,"PREVENCIÓN: Elimine las palmas con grados de severidad 4, 5, cráter y con síntoma de hoja clorótica. Utilice los métodos mecánicos avalados por el ICA. Carbonice los cogollos y tejidos afectados. Realice censos fitosanitarios cada 8 días, remueva el tejido enfermo en palmas con grado de severidad 1, 2 y 3.")
                elif var10.get() == 10:
                    entry.insert(tk.INSERT,"COGOLLO:                  EXPLICACIÓN: La Pudrición del Cogollo (PC) ha sido la plaga más devastadora de la palma de aceite en América Latina. Los síntomas de la enfermedad se caracterizan por la pudrición de todos los nuevos tejidos, conservándose las hojas que se formaron antes de la infección.")
                    entry2.insert(tk.INSERT,"PREVENCIÓN: Elimine las palmas con grados de severidad 4, 5, cráter y con síntoma de hoja clorótica. Utilice los métodos mecánicos avalados por el ICA. Carbonice los cogollos y tejidos afectados. Realice censos fitosanitarios cada 8 días, remueva el tejido enfermo en palmas con grado de severidad 1, 2 y 3.")
                    
                
                        
                        
                    
                    
                    

boton = ttk.Button(text="¡Hola, mundo!", command=saludar)
boton.place(x=900, y=510)
      
window.mainloop()
