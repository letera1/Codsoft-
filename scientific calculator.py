from tkinter import *
import math
import tkinter.messagebox

# creating a window
window = Tk(className='Python Examples - Window Color')
pic = PhotoImage(file="123.png")
window.iconphoto(True, pic)
window.configure(bg="black")
window.title("Scientific Calculator")
window.geometry("750x850")
e = Entry(window, width=53, border=15, font="Verdana", bg="white", fg="black", justify=RIGHT, cursor="arrow")
e.grid(row=0, column=0, columnspan=6, padx=10, pady=20, ipady=18)
window.resizable(width=True, height=True)
class calculator:
    def _init_(self):
        pass
    def rad(self, num):
        try:
            p = num * (3.14 / 180)
            return p
        except:
            tkinter.messagebox.showerror("#Error", "Check Your values and operators")
    def butclick(self, numb):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(numb))

    def butclear(self):
        e.delete(0, END)

    def butequal(self):
        second = e.get()
        e.delete(0, END)
        if mathe == "Addition":
            try:
                e.insert(0, eval(second))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, second)
        if mathe == "Multiplication":
            try:
                e.insert(0, eval(second))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, (second))
        if mathe == "Subtraction":
            try:
                e.insert(0, eval(second))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, second)
        if mathe == "Division":
            try:
                e.insert(0, eval(second))

            except ZeroDivisionError:
                tkinter.messagebox.showerror("#Error", "Number cannot be divided by 0")
                e.insert(0, second)
        if mathe == "Power":
            try:
                e.insert(0, (eval(second)))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, second)
        if mathe == "Sqrt":
            try:
                e.insert(0, (eval(str(fnumb) + str(math.sqrt(eval(second))))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnum))
        if mathe == "Factorization":
            try:
                e.insert(0, eval(str(fnumb) + str(math.factorial(eval(second)))))
            except:

                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Sin":
            second = eval(second)
            try:
                if second % 90 == 0:
                    e.insert(0, eval(str(fnumb) + str(int(math.sin(math.radians(second))))))
                else:
                    e.insert(0, eval(str(fnumb) + str(math.sin(math.radians(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Cos":
            second = eval(second)
            try:
                if second % 90 == 0:
                    e.insert(0, eval(str(fnumb) + str(int(math.cos(math.radians(second))))))
                else:
                    e.insert(0, eval(str(fnumb) + str(math.cos(math.radians(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Tan":
            second = eval(second)
            try:
                if second % 90 == 0:
                    e.insert(0, eval(str(fnumb) + str(tan(math.cos(math.radians(second))))))
                else:
                    e.insert(0, eval(str(fnumb) + str(math.tan(math.radians(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Sinin":
            try:
                e.insert(0, eval(str(fnumb) + str(math.degrees(math.asin(eval(second))))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Cosin":
            try:
                e.insert(0, eval(str(fnumb) + str(math.degrees(math.acos(eval(second))))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Tanin":
            try:
                e.insert(0, eval(str(fnumb) + str(math.degrees(math.atan(eval(second))))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Log":
            try:
                e.insert(0, eval(str(fnumb) + str(math.log10(eval(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Round":
            try:
                e.insert(0, eval(str(fnumb) + str(round(eval(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Rad":
            try:
                e.insert(0, eval(str(fnumb) + str(math.radians(eval(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Ln":
            try:
                e.insert(0, eval(str(fnumb) + str(math.log(eval(second)))))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(fnumb))
        if mathe == "Modulus":
            try:
                e.insert(0, eval(second))
            except:
                tkinter.messagebox.showerror("#Error", "Check Your values and operators")
                e.insert(0, str(second))

        if mathe == "Remove":
            e.insert(0, math.degrees(math.atan(eval(second))))

    def butadd(self):

        fnumb = e.get()
        global fnum
        fnum = str(fnumb) + "+"
        e.delete(0, END)
        global mathe
        mathe = "Addition"
        e.insert(0, str(fnum))

    def butsub(self):
        fnumb = e.get()
        global fnum
        fnum = str(fnumb) + "-"
        e.delete(0, END)
        global mathe
        mathe = "Subtraction"
        e.insert(0, str(fnum))

    def butmul(self):
        fnumb = e.get()
        global fnum
        fnum = str(fnumb) + "*"
        e.delete(0, END)
        global mathe
        mathe = "Multiplication"
        e.insert(0, str(fnum))

    def butdiv(self):
        fnumb = e.get()
        global fnum
        fnum = str(fnumb) + "/"
        e.delete(0, END)
        global mathe
        mathe = "Division"
        e.insert(0, str(fnum))

    def butpow(self):
        fnumb = e.get()
        global fnum
        fnum = str(fnumb) + "**"
        e.delete(0, END)
        global mathe
        mathe = "Power"
        e.insert(0, str(fnum))

    def butsqrt(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Sqrt"

    def butfact(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Factorization"

    def butsin(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Sin"

    def butcos(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Cos"

    def buttan(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Tan"

    def butinsin(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Sinin"

    def butincos(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Cosin"

    def butintan(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Tanin"

    def butpi(self):
        fnumb = e.get()
        e.delete(0, END)
        e.insert(0, eval(str(fnumb) + str(math.pi)))

    def butlog(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Log"

    def butround(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Round"

    def butrad(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Rad"

    def butln(self):
        fnum = e.get()
        global fnumb
        fnumb = str(fnum)
        e.delete(0, END)
        global mathe
        mathe = "Ln"

    def butmod(self):
        fnumb = e.get()
        global fnum
        fnum = str(fnumb) + "%"
        e.delete(0, END)
        global mathe
        mathe = "Modulus"
        e.insert(0, str(fnum))

    def bute(self):
        fnumb = e.get()
        e.delete(0, END)
        e.insert(0, eval(str(fnumb) + str(math.e)))

    def butrem(self):
        leng = len(e.get())
        display = str(e.get())
        if display == '':
            e.insert(0, '')
        elif display == ' ':
            e.insert(0, '')
        elif display == '':
            pass
        else:
            e.delete(0, END)
            e.insert(0, display[0:leng - 1])
    def butabs(self):
        try:
            value = float(e.get())
            result = abs(value)
            e.delete(0, END)
            e.insert(0, result)
        except ValueError:
            tkinter.messagebox.showerror("#Error", "Invalid input")




    def rad_to_deg(self):
        try:
            radian = float(e.get())
            degree = math.degrees(radian)
            e.delete(0, END)
            e.insert(0, degree)
        except ValueError:
            tkinter.messagebox.showerror("#Error", "Invalid input")

    def close_calculator(self):
        window.destroy()
        sys.exit()

    def greatest_floor(self):
        try:
            value = float(e.get())
            result = math.floor(value)
            e.delete(0, END)
            e.insert(0, result)
        except ValueError:
            tkinter.messagebox.showerror("#Error", "Invalid input")


cal = calculator()

But1 = Button(window, text="1", padx=59, pady=20, bg="#4b4d4b", fg="white", font="5", command=lambda: cal.butclick(1))
But2 = Button(window, text="2", padx=59, pady=20, bg="#4b4d4b", fg="white", font="5", command=lambda: cal.butclick(2))
But3 = Button(window, text="3", padx=58, pady=20, bg="#4b4d4b", fg="white", font="5", command=lambda: cal.butclick(3))
But4 = Button(window, text="4", padx=59, pady=20, bg="#4b4d4b", fg="white", font="5", command=lambda: cal.butclick(4))
But5 = Button(window, text="5", padx=59, pady=20, bg="#4b4d4b", fg="white", font="5", command=lambda: cal.butclick(5))
But6 = Button(window, text="6", padx=58, pady=20, bg="#4b4d4b", fg="white", font="5", command=lambda: cal.butclick(6))
But7 = Button(window, text="7", padx=59, pady=20, bg="#4b4d4b", fg="white", font="5", command=lambda: cal.butclick(7))
But8 = Button(window, text="8", padx=59, pady=20, bg="#4b4d4b", fg="white", font="5", command=lambda: cal.butclick(8))
But9 = Button(window, text="9", padx=58, pady=20, bg="#4b4d4b", fg="white", font="5", command=lambda: cal.butclick(9))
But0 = Button(window, text="0", padx=59, pady=20, bg="#4b4d4b", fg="white", font="5", command=lambda: cal.butclick(0))
Butpoint = Button(window, text=".", padx=62, pady=20, bg="#4b4d4b", font="30", fg="white",command=lambda: cal.butclick("."))
Butleftb = Button(window, text=")", padx=66, pady=20, bg="#72a346", font="10", fg="white",command=lambda: cal.butclick(")"))
Butrightb = Button(window, text="(", padx=64, pady=20, bg="#72a346", font="10", fg="white",command=lambda: cal.butclick("("))
Butequal = Button(window, text="=", padx=64, pady=20, font="5", bg="#4b4d4b", fg="white", command=cal.butequal)
Butclear = Button(window, text="C", padx=63, pady=20, font="5", bg="red", fg="white", command=cal.butclear)

# simple math functions
Butadd = Button(window, text="+", padx=61, pady=20, bg="#4b4d4b", font="5", fg="white", command=cal.butadd)
Butsub = Button(window, text="- ", padx=63, pady=20, bg="#4b4d4b", fg="white", font="5", command=cal.butsub)
Butmul = Button(window, text="*", padx=63, pady=20, bg="#4b4d4b", fg="white", font="5", command=cal.butmul)
Butdiv = Button(window, text="/", padx=67, pady=20, bg="#4b4d4b", fg="white", font="5", command=cal.butdiv)
Butpower = Button(window, text="x^y ", padx=50, pady=20, bg="#72a346", fg="white", font="5", command=cal.butpow)
Butsqrt = Button(window, text=" √x", padx=52, pady=20, bg="#72a346", fg="white", font="5", command=cal.butsqrt)
Butfact = Button(window, text="X!", padx=54, pady=20, bg="#72a346", fg="white", font="5", command=cal.butfact)
But_greatest_floor = Button(window, text="⌊X⌋", padx=48, pady=20, bg="#72a346", fg="white", font="7", command=cal.greatest_floor)

# trignometry
Butsin = Button(window, text="Sin", padx=50, pady=20, bg="black", fg="white", font="5", command=cal.butsin)
Butcos = Button(window, text="Cos", padx=47, pady=20, bg="black", fg="white", font="5", command=cal.butcos)
Buttan = Button(window, text="Tan", padx=47, pady=20, bg="black", fg="white", font="5", command=cal.buttan)
Butinsin = Button(window, text="Sin^-1", padx=39, pady=20, bg="black", fg="white", font="5", command=cal.butinsin)
Butincos = Button(window, text="Cos^-1", padx=37, pady=20, bg="black", fg="white", font="5", command=cal.butincos)
Butintan = Button(window, text="Tan^-1", padx=34, pady=20, bg="black", fg="white", font="5", command=cal.butintan)

# pi
Butpi = Button(window, text="π", padx=60, pady=20, fg="white", bg="#72a346", font="5", command=cal.butpi)

# log
Butlog = Button(window, text=" Log", padx=47, pady=20, fg="white", bg="black", font="5", command=cal.butlog)

# round
Butround = Button(window, text="Round", padx=43, pady=20, fg="white", bg="black", font="5", command=cal.butround)

# rad
Butrad = Button(window, text="Rad", padx=48, pady=20, fg="white", bg="#72a346", font="5", command=cal.butrad)

# ln
Butln = Button(window, text="ln", padx=59, pady=20, fg="white", bg="black", font="5", command=cal.butln)

# modulus
Butmod = Button(window, text="%", padx=55, pady=20, fg="white", bg="#4b4d4b", font="5", command=cal.butmod)

# e
Bute = Button(window, text="e", padx=64, pady=20, fg="white", bg="#72a346", font="5", command=cal.bute)

# remove
Butrem = Button(window, text="⌫", padx=54, pady=20, fg="white", bg="red", font="5", command=cal.butrem)

#absolute value
Butabs = Button(window, text="|x|", padx=60, pady=20, bg="#4b4d4b", fg="white", font="5", command=cal.butabs)

#degree
But_rad_to_deg = Button(window, text="Deg", padx=48, pady=20, bg="#72a346", fg="white", font="5", command=cal.rad_to_deg)

#close
But_close = Button(window, text="X", padx=64, pady=20, bg="red", fg="white", font="5", command=cal.close_calculator)

# row1
Butcos.grid(row=1, column=1)
Butlog.grid(row=1, column=3)
Butsin.grid(row=1, column=0)
Buttan.grid(row=1, column=2)
But_close.grid(row=1, column=4)
# row2
Butln.grid(row=2, column=3)
Butround.grid(row=2, column=4)
Butinsin.grid(row=2, column=0)
Butintan.grid(row=2, column=2)
Butincos.grid(row=2, column=1)
# Row3
Bute.grid(row=3, column=4)
Butpi.grid(row=3, column=3)
Butsqrt.grid(row=3, column=1)
Butfact.grid(row=3, column=2)
Butpower.grid(row=3, column=0)
# row4
Butrad.grid(row=4, column=0)
Butrightb.grid(row=4, column=3)
Butleftb.grid(row=4, column=4)
But_rad_to_deg.grid(row=4, column=1)
But_greatest_floor.grid(row=4, column=2)
#row 5
But7.grid(row=5, column=0)
But8.grid(row=5, column=1)
But9.grid(row=5, column=2)
Butclear.grid(row=5, column=4)
Butrem.grid(row=5, column=3)
# row6
Butmul.grid(row=6, column=3)
Butdiv.grid(row=6, column=4)
But4.grid(row=6, column=0)
But5.grid(row=6, column=1)
But6.grid(row=6, column=2)
# row7
But1.grid(row=7, column=0)
But2.grid(row=7, column=1)
But3.grid(row=7, column=2)
Butadd.grid(row=7, column=3)
Butsub.grid(row=7, column=4)
#row 8
Butequal.grid(row=8, column=4)
Butmod.grid(row=8, column=2)
Butabs.grid(row=8, column=3)
Butpoint.grid(row=8, column=1)
But0.grid(row=8, column=0)

window.mainloop()
