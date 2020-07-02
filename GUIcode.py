from pyModbusTCP.client import ModbusClient
c = ModbusClient(host="localhost", port=502, auto_open=True)



import tkinter
top = tkinter.Tk()
top.title("Absorber Rod Driving Mechanism Flask Display Station")
#top.minsize(width="1300", height="600")
frame=tkinter.Frame(top, width=1000, height=800)

logo = tkinter.PhotoImage(file="aqi-transparent.png")
w1 = tkinter.Label(top, width="100", height="110", image=logo)
#w1.grid(row=0,column=0)
w1.place(x=0,y=0)

logo1 = tkinter.PhotoImage(file="unnamed.png")
w2 = tkinter.Label(top, width="1000", height="1100", image=logo1)
#w2.grid(row=0,column=10)
w2.place(x=900,y=0)

#logo1 = tkinter.PhotoImage(file="bha.png")
#w2 = tkinter.Label(top, image=logo1).pack(side="left",anchor='nw')

w = tkinter.Label(top, text="Air Quality Assessment", foreground="blue", font=("Helvetica", 45))
#w.pack()
w.place(x=125,y=0)
w4 = tkinter.Label(top, text="Save degrading Air Quality", foreground="green", font=("Helvetica", 20))
w4.place(x=185,y=70)

hoisttop=tkinter.Label(top,text="CARBON DIOXIDE",font=('Comic Sans MS',10))
#titleLabel1.grid(row=1,column=0)
hoisttop.place(x=10,y=150)

w3 = tkinter.Label(top, width="2", height="1", bg="grey")
#w2.grid(row=0,column=10)
w3.place(x=210,y=150)

w4 = tkinter.Label(top, width="2", height="1", bg="grey")
#w2.grid(row=0,column=10)
w4.place(x=245,y=150)

hoistrest=tkinter.Label(top,text="PPM",font=('Comic Sans MS',10))
#titleLabel1.grid(row=1,column=0)
hoistrest.place(x=10,y=180)

w5 = tkinter.Label(top, width="2", height="1", bg="grey")
#w2.grid(row=0,column=10)
w5.place(x=210,y=180)

w6 = tkinter.Label(top, width="2", height="1", bg="grey")
#w2.grid(row=0,column=10)
w6.place(x=245,y=180)

hoistbottom=tkinter.Label(top,text="Carbon Monooxide",font=('Comic Sans MS',10))
#titleLabel1.grid(row=1,column=0)
hoistbottom.place(x=10,y=210)

w7 = tkinter.Label(top, width="2", height="1", bg="grey")
#w2.grid(row=0,column=10)
w7.place(x=245,y=210)

titleLabel1=tkinter.Label(top,text="Suspended particles",font=('Comic Sans MS',10))
#titleLabel1.grid(row=1,column=0)
titleLabel1.place(x=330,y=150)

writeLabel1=tkinter.Label(top,text=" ",font=('Comic Sans MS',10))
#writeLabel1.grid(row=1,column=1)
writeLabel1.place(x=540,y=150)

ms1e=tkinter.Label(top,text="Visibility",font=('Comic Sans MS',10))
#titleLabel1.grid(row=1,column=0)
ms1e.place(x=600,y=150)

w8 = tkinter.Label(top, width="2", height="1", bg="grey")
#w2.grid(row=0,column=10)
w8.place(x=810,y=150)

w9 = tkinter.Label(top, width="2", height="1", bg="grey")
#w2.grid(row=0,column=10)
w9.place(x=845,y=150)

frame.pack()

while(1):
   regs = c.read_holding_registers(0, 63)
   #print(regs)
   try:
      #print(ad)
      
      d1=regs[0]
      d1=int(d1)
      d1d=d1/10;
      d1d=str(d1d)
      d2=regs[1]
      d3=regs[2]
      d4=regs[3]
      d5=regs[4]
      d6=regs[5]
         
         
      writeLabel1.config(text=d1d)
      writeLabel1.update_idletasks()
      top.update()

      if d2==0 :
         
         w3 = tkinter.Label(top, width="2", height="1", bg="grey")
#w2.grid(row=0,column=10)
         w3.place(x=210,y=150)
         top.update()

      if d2==1 :
         
         w3 = tkinter.Label(top, width="2", height="1", bg="red")
#w2.grid(row=0,column=10)
         w3.place(x=210,y=150)
         top.update()    

      if d3==0 :
         
         w4 = tkinter.Label(top, width="2", height="1", bg="grey")
#w2.grid(row=0,column=10)
         w4.place(x=245,y=150)
         top.update()

      if d3==1 :
         
         w4 = tkinter.Label(top, width="2", height="1", bg="red")
#w2.grid(row=0,column=10)
         w4.place(x=245,y=150)
         top.update()

      if d4==0 :
         
         w5 = tkinter.Label(top, width="2", height="1", bg="grey")
#w2.grid(row=0,column=10)
         w5.place(x=210,y=180)
         top.update()

      if d4==1 :
         
         w5 = tkinter.Label(top, width="2", height="1", bg="red")
#w2.grid(row=0,column=10)
         w5.place(x=210,y=180)
         top.update()

      if d5==0 :
         
         w5 = tkinter.Label(top, width="2", height="1", bg="grey")
         w5.place(x=245,y=180)
         top.update()

      if d5==1 :
         
         w5 = tkinter.Label(top, width="2", height="1", bg="red")
         w5.place(x=245,y=180)
         top.update()

      if d6==0 :
         
         w7 = tkinter.Label(top, width="2", height="1", bg="grey")
         w7.place(x=245,y=210)
         top.update()

      if d6==1 :
         
         w7 = tkinter.Label(top, width="2", height="1", bg="red")
         w7.place(x=245,y=210)
         top.update()
                  
         
   except:
      pass


top.mainloop()
