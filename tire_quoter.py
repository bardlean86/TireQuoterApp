from tkinter import *

color1 = '#155BBB'
color2 = '#555FFF'

### Initialize the main loop ###
app = Tk()
app.title("Deluxe Tire Quote Assistant - Created by Branden")
app.geometry("790x390+500+300")
app.configure(background=color1)

### Create the main frame within which we will place our calculator ###
frame = Frame(app,
              width=400,
              height=350,
              bg=color2,
              relief=SUNKEN,
              bd=5)


### Create canvas to display Tireman logo ###
img1 = PhotoImage(file="tireman.png")
canvas = Canvas(app,
                width=325,
                height=180,
                bg=color1,
                highlightthickness=0,
                relief=RIDGE)

canvas.place(x=440, y=0)

### Create our variables ###
var_base = StringVar(app, value=None)
var_quantity = IntVar(app, value=0)
var_FTG = IntVar(app, value=0)
var_coupon = IntVar(app, value=0)
var_total = StringVar(app, value=0)

def calculate_total():
    ### Output final cost of tires based on a string of parameters and options ###
    i = var_base.get()
    i = float(i)  

    tax = 1.0675
    disposal = 2.50
    fee = 1.00

    v = var_FTG.get()

    coupon = (int(var_coupon.get()))/4

    base = float(ent_base.get())
    quantity = int(ent_quantity.get())

    ftg = 0

    if i <= 83.35:
        ftg = 12.50

    else:
        ftg = 1.15

    if v == 1:

        if ftg == 1.15:
            base = base*ftg
            if var_coupon:
                total = base-coupon
                print(base)
            total = total + (fee+disposal)
            print(total)
            total = total*quantity
            print(total)
            total = round((total*tax),2)
            print(total)

        if ftg == 12.50:
            base = base+ftg
            if var_coupon:
                total = base-coupon
                print(base)
            total = total + (fee+disposal)
            print(total)
            total = total*quantity
            print(total)
            total = round((total*tax),2)
            print(total)

    else:
        if var_coupon:
            total = base-coupon
            print(base)
        total = total + (fee+disposal)
        print(total)
        total = total*quantity
        print(total)
        total = round((total*tax),2)
        print(total)
        
    total = "$" + str(total)
    print(total)
    lbl_total.config(text=total)

    app.update()

def create_window():
    ### Create a new window with a funny comic ###
    window = Toplevel(app, width=346, height=480)
    window.title("New Window")
    
    img_comic = PhotoImage(file="tired.png")
    
    comic = Canvas(window,
                   width=img_comic.width(),
                   height=img_comic.height())

    comic.create_image(0,0,
                       anchor=NW,
                       image=img_comic)
    comic.pack()

    window.mainloop()
    
    
### Box where you enter base tire cost ###
ent_base = Entry(frame,
                 textvariable=var_base,
                 width=20)

ent_base.place(x=20,y=20)
ent_base.focus()

lbl_base = Label(frame,
                 text=" : ENTER BASE PRICE",
                 bg=color2)

lbl_base.place(x=185, y=18)

### Box where you enter number of tires ###
ent_quantity = Entry(frame,
                     width=20)

ent_quantity.place(x=20, y=70)

lbl_quantity = Label(frame,
                     text=" : NUMBER OF TIRES",
                     bg=color2)

lbl_quantity.place(x=185, y=68)

### Radio buttons where you select which coupon to use ###
rdo_nocpn = Radiobutton(frame,
                        text="NO COUPON",
                        bg=color2,
                        variable=var_coupon,
                        value=0)

rdo_nocpn.place(x=15, y=110)

rdo_cpn_30 = Radiobutton(frame,
                         text="$30 OFF COUPON",
                         bg=color2,
                         variable=var_coupon,
                         value=30)

rdo_cpn_30.place(x=15,y=150)

rdo_cpn_40 = Radiobutton(frame,
                         text="$40 OFF COUPON",
                         bg=color2,
                         variable=var_coupon,
                         value=40)

rdo_cpn_40.place(x=15,y=180)

rdo_cpn_50 = Radiobutton(frame,
                         text="$50 OFF COUPON",
                         bg=color2,
                         variable=var_coupon,
                         value=50)

rdo_cpn_50.place(x=15,y=210)

### Radio buttons to select whether or not to apply Free Tire Guarantee ###
rdo_FTG_yes = Radiobutton(frame,
                          text="YES",
                          bg=color2,
                          variable=var_FTG,
                          value=1)

rdo_FTG_yes.place(x=15,y=250)

rdo_FTG_no = Radiobutton(frame,
                         text="NO",
                         bg=color2,
                         variable=var_FTG,
                         value=0)

rdo_FTG_no.place(x=100,y=250)

lbl_FTG = Label(frame,
                text=" : ADD FREE TIRE GUARANTEE?",
                bg=color2)

lbl_FTG.place(x=170,y=252)

### Calculate and display final total ###
btn_calc = Button(frame,
                  text="CALCULATE",
                  command=calculate_total)

btn_calc.place(x=20,y=295)

lbl_total = Label(frame,
                  width=20,
                  relief=SUNKEN,
                  bd=5)

lbl_total.place(x=190, y=295)

### Code used to place images and info outside of the main frame ###
frame.place(x=15, y=20)

canvas.create_image(0,20,
                    anchor=NW,
                    image=img1)

lbl_credit = Label(app,
                   text="Copyright © 2020 Branden Ardelean.",
                   bg=color1,
                   fg='white')

lbl_credit.place(x=480, y=180)

btn_bonus = Button(app,
                   text="Click me!",
                   bg=color1,
                   command=create_window)

btn_bonus.place(x=560, y=325)

app.mainloop()
