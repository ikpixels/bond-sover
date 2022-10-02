from tkinter import*
import time
import sqlite3
from tkinter.messagebox import*
import tkinter.ttk as ttk

#========================Main App===============================
root=Tk()
root.geometry("800x500+0+0")
root.title("Bonds Sover")
root.configure(background='black')

#========================Functions===============================
def qiut():
	q=showinfo('IKpixels',"Are you serious you want to Quit?")
	if q != 0:
		root.destroy()
C=IntVar()
F=IntVar()
R=IntVar()
T=IntVar()

def bond():
	
	if C.get()==0 or T.get()==0:
		showinfo("IKpixels_Tech","complete required fields!")
	else:
		text.delete("0.1",END)
		c=C.get()/100
		f=F.get()
		r=R.get()/100
		t=T.get()
		present_pmt=c*f*(1-((1+r)**-t))/r
		fixed=f/(1+r)**t
		present_bond=present_pmt+fixed
		text.insert(END," Present value of Bond ")
		text.insert(END,"\n\n")
		text.insert(END,"present value of a bond is\nMK" )
		text.insert(END,present_pmt)
		text.insert(END,"\n\n")
		text.insert(END,"Present Face Value of Bond is\nMK" )
		text.insert(END,fixed)
		text.insert(END,"\n\n")
		text.insert(END,"Present Value of Bond is\nMK" )
		text.insert(END,present_bond)
		C.set("")
		F.set("")
		R.set("")
		T.set("")
def bond2():
	
	if C.get()==0 or T.get()==0:
		showinfo("IKpixels_Tech","complete required fields!")
	else:
		text.delete("0.1",END)
		c=C.get()/100
		f=F.get()
		r=R.get()/100
		t=T.get()
		c2=c/2
		r2=r/2
		present_pmt=c2*f*(1-((1+r2)**-t))/r2
		fixed=f/(1+r2)**t
		present_bond=present_pmt+fixed
		text.insert(END," Present value of Bond ")
		text.insert(END,"\n\n")
		text.insert(END,"present value of a bond is MK" )
		text.insert(END,present_pmt)
		text.insert(END,"\n\n")
		text.insert(END,"Present Face Value of the Bond is MK" )
		text.insert(END,fixed)
		text.insert(END,"\n\n")
		text.insert(END,"Present Value of Bond is MK" )
		text.insert(END,present_bond)
		C.set("")
		F.set("")
		R.set("")
		T.set("")

def reset():
		C.set("")
		F.set("")
		R.set("")
		T.set("")
		text.delete("0.1",END)


def about_bond():
	text.delete("0.1",END)
	text.insert(END,"""A bond is a financial instrumentthat\nis issued for a specific period with thepurpose of borrowing money. When the bond is issued, it promises the holder, to pay a fixed sum of interest based  on the predefined interest rate (coupon rate)at specified dates, usually, semi-annually,annually,etc. until it matures and it repaysthe principle amount at the maturity.""")
	text.insert(END,"\n\n")
	text.insert(END,"""Present value is an alternative bond valuation method that calculates the current worth of the stream of future cash flows at a given rate of return. Cash flows on a bond are fairly certain. So, the present value of a bond is the value equal to the discounted interest payments (interest inflows) and the discounted redemption value of the face value of the bond certificate. These cash flows will be discounted based on the interest rate prevailing in the market at a particular instant""")
	text.insert(END,"\n\n")
	text.insert(END,"       @IKpixels-Tech 2018\n                 Demo APP")
#========================Disply=================================

la=Label(root, text="Present Value of a Bond",font=('times', 30 , 'bold'), bg='black', fg= 'white')
la.place(x=170, y= 10)
la=Label(root, text="IKpixels-Tech",font=('times', 15 , 'italic'), bg='black', fg= 'blue')
la.place(x=10, y= 10)

text=Text(root, width=32, height=14.3, font=('times', 18 , 'bold'))
text.place(x=360, y=60)
scro=Scrollbar(root)
scro.pack(side=RIGHT, fill=Y)
scro.config(command=text.yview)
text.config( yscrollcommand=scro.set)
#========================label=================================
la=Label(root, text="Coupon rate of the bond(C)", font=('arial', 10 , 'bold'), bg= 'black', fg='white')
la.place(x=10, y =70)
la2=Label(root, text="Face value of the bond(F)", font=('arial', 10 , 'bold'), bg= 'black', fg='white')
la2.place(x=10, y =140)
la3=Label(root, text="Rate of Period(R)", font=('arial', 10 , 'bold'), bg= 'black', fg='white')
la3.place(x=10, y =210)
la4=Label(root, text="Number of Periods(T)", font=('arial', 10 , 'bold'), bg= 'black', fg='white')
la4.place(x=10, y =280)

#========================entery==================================
ent=Entry(root, text="Coupon rate of the bond(C)", font=('arial', 18 , 'bold'), bd=1, textvariable=C)
ent.place(x=10, y =100)
ent2=Entry(root, text="Face value of the bond(F)", font=('arial', 18 , 'bold'), bd=1, textvariable=F)
ent2.place(x=10, y =170)
ent3=Entry(root, text="Market Interest(R)", font=('arial', 18 , 'bold'), bd=1, textvariable=R)
ent3.place(x=10, y =240)
ent4=Entry(root, text="Time(T)", font=('arial', 18 , 'bold'), bd=1, textvariable=T)
ent4.place(x=10, y =310)
#====================================Button==============================================
btn=Button(root, text='Present value\nof a bond', bd=5,fg="blue", font=('arial', 8 , 'bold'), command=bond)
btn.place(x=10, y=350)
btn2=Button(root, text='on\nsemi-annual', bd=5,fg="blue", font=('arial', 8 , 'bold'), command=bond2)
btn2.place(x=105, y=350)
btn2=Button(root, text='About\nBonds', bd=5,fg="blue", font=('arial', 8 , 'bold'),width=9, command=about_bond)
btn2.place(x=193, y=350)
btn2=Button(root, text='Reset', bd=5,fg="red", font=('arial', 8 , 'bold'), width=35, command=reset)
btn2.place(x=10, y=405)
btn2=Button(root, text='Quit', bd=5,fg="white", bg='red', font=('arial', 8 , 'bold'), width=35, command=qiut)
btn2.place(x=10, y=450)


#===========================================================================================

root.mainloop()