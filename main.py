from tkinter import*
from tkinter import Tk,StringVar,ttk
import urllib.request
import json
#----------------frame calling--------
def raise_frame(frame):
    frame.tkraise()
#------------train route-----------
def TrainRoute():
    resp=str()
    global e
    train_num=e.get()
    global f2
    url="https://api.railwayapi.com/v2/route/train/"+str(train_num)+"/apikey/4ng2pv0vx8/"
    req=urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page=response.read()
        resp=json.loads(the_page)
        arr=resp['route']
        result=str()
        num=1
        for a in arr:
            result+=str(num)+'   '+'\t\t\t'+a['station']['name']+"\n"
            num+=1
        global label
        label.config(text=result)
        label.update()
#-----------train-details-----------
def TrainDetails():
    resp=str()
    global e3
    train_number=e3.get()
    global e4
    stn_code=e4.get()
    global e5
    dest_code=e5.get()
    global e6
    age=e6.get()
    global e7
    class_code=e7.get()
    global e8
    quota_code=e8.get()
    global e9
    dd_mm_yyyy=e9.get()
    global f3
    url="https://api.railwayapi.com/v2/fare/train/"+str(train_number)+"/source/"+str(stn_code)+"/dest/"+str(dest_code)+"/age/"+str(age)+"/pref/"+str(class_code)+"/quota/"+str(quota_code)+"/date/"+str(dd_mm_yyyy)+"/apikey/4ng2pv0vx8/"
    req=urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page=response.read()
        resp=json.loads(the_page)
        arr=resp['train']
        result="\tName\t"+str(arr['classes'])+ "\tname \t"+str(arr['name'])+"\n\n"
        global label4
        label4.config(text=result)
        label4.update()
#------------pnr---------------------
def PNR():
    resp=str()
    global e2
    pnr=e2.get()
    global f4
    url="https://api.railwayapi.com/v2/pnr-status/pnr/"+str(pnr)+"/apikey/4ng2pv0vx8/"
    req=urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page=response.read()
        resp=json.loads(the_page)
        arr=resp['from_station']
        result="\tName\t"+str(arr['name'])+ "\tcode \t"+str(arr['code'])+"\n\n"
        global label3
        label3.config(text=result)
        label3.update()                   
#--------------seat availability.-------
def SeatAvailability():
    resp=str()
    global e10
    train_number=e10.get()
    global e11
    stn_code=e11.get()
    global e12
    dest_code=e12.get()
    global e13
    dd_mm_yyyy=e13.get()
    global e14
    class_code=e14.get()
    global e15
    quota_code=e15.get()  
    global f5
    url="https://api.railwayapi.com/v2/check-seat/train/"+str(train_number)+"/source/"+str(stn_code)+"/dest/"+str(dest_code)+"/date/"+str(dd_mm_yyyy)+"/pref/"+str(class_code)+"/quota/"+str(quota_code)+"/apikey/4ng2pv0vx8/"
    req=urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page=response.read()
        resp=json.loads(the_page)
        arr=resp['availability']
        result=str()
        num=1
        for a in arr:
            result+=str(num)+'   '+'\t\t\t'+a['status']+"\n"
            num+=1
        global label5
        label5.config(text=result)
        label5.update()
#------------live--status-------------        
def LiveStatus():
    resp=str()
    global e16
    train_number=e16.get()
    global e17
    stn_code=e17.get()
    global e18
    dd_mm_yyyy=e18.get()
    global f5
    url="https://api.railwayapi.com/v2/live/train/"+str(train_number)+"/station/"+str(stn_code)+"/date/"+str(dd_mm_yyyy)+"/apikey/4ng2pv0vx8/"
    req=urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page=response.read()
        resp=json.loads(the_page)
        arr=resp['status']
        result="\thas_departed\t"+str(arr['has_departed'])+ "\tscharr_date \t"+str(arr['scharr_date'])+ "\tlatemin \t"+str(arr['latemin'])+ "\tscharr \t"+str(arr['scharr'])+ "\tactarr_date \t"+str(arr['actarr_date'])+ "\tactdep \t"+str(arr['actdep'])+ "\tactarr \t"+str(arr['actarr'])+ "\thas_arrived \t"+str(arr['has_arrived'])+ "\tschdep \t"+str(arr['schdep'])+"\n\n"
        global label6
        label6.config(text=result)
        label6.update()
#-----------------Train--Between--2----
def bt2():
    resp=str()
    global e19
    stn_code=e19.get()
    global e20
    dest_code=e20.get()
    global e21
    dd_mm_yyyy=e21.get()
    global f8
    url="https://api.railwayapi.com/v2/between/source/"+str(stn_code)+"/dest/"+str(dest_code)+"/date/"+str(dd_mm_yyyy)+"/apikey/4ng2pv0vx8/"
    req=urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page=response.read()
        resp=json.loads(the_page)
        arr=resp['trains']
        result=str()
        num=1
        for a in arr:
            result+=str(num)+'   '+'\t\t\t'+ a['name']+"\n"
            num+=1
        global label8
        label8.config(text=result)
        label8.update()    
#----------CANCELLED TRAINS-----------
def CanTrain():
    global e22
    dd_mm_yyyy=e22.get()
    global f7
    url="https://api.railwayapi.com/v2/cancelled/date/"+str(dd_mm_yyyy)+"/apikey/4ng2pv0vx8/"
    req=urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page=response.read()
        resp=json.loads(the_page)
        arr=resp['trains']
        result=str()
        num=1
        for a in arr:
            result+=str(num)+'   '+'\t\t\t'+ a['name']+"\n"
            num+=1
        global label7
        label7.config(text=result)
        label7.update()
#----------RESCHEDULED TRAINS-----------
def RESTrain():
    global e23
    dd_mm_yyyy=e23.get()
    global f9
    url="https://api.railwayapi.com/v2/rescheduled/date/"+str(dd_mm_yyyy)+"/apikey/4ng2pv0vx8/"
    req=urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page=response.read()
        resp=json.loads(the_page)
        arr=resp['trains']
        result=str()
        num=1
        for a in arr:
            result+=str(num)+'   '+'\t\t\t\t\t\t\t\t'+ a['name']['rescheduled_time']['rescheduled_date']['number']['to_station']['time_diff']['from_station']+"\n\n\n\n\n\n\n"
            num+=1
        global label9
        label9.config(text=result)
        label9.update()        

#----------------------frame----------
root=Tk()
root.geometry("800x800+0+0")
f1=Frame(root,width=600,height=600,relief=SUNKEN)
f2=Frame(root)
f3=Frame(root)
f4=Frame(root)
f5=Frame(root)
f6=Frame(root)
f7=Frame(root)
f8=Frame(root)
f9=Frame(root)
for frame in(f1,f2,f3,f4,f5,f6,f7,f8,f9):
    frame.config(background='white')
    root.config(background='white')
    frame.grid(row=0,column=1,sticky='news')
#--------------------f1----------------------
Label(f1,text='INDIAN RAILWAY ENQUAIRY',width=50,height=2,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()
Button(f1,text='Train Route',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f2)).pack()
Label(f1,bg='white').pack()
Button(f1,text='Train Details',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f3)).pack()
Label(f1,bg='white').pack()
Button(f1,text='PNR Status',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f4)).pack()
Label(f1,bg='white').pack()
Button(f1,text='Seat Avaialabilty',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f5)).pack()
Label(f1,bg='white').pack()
Button(f1,text='Find Train Status',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f6)).pack()
Label(f1,bg='white').pack()
Button(f1,text='Canclled Train',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f7)).pack()
Label(f1,bg='white').pack()
Button(f1,text='Rescheduled Trains',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f9)).pack()
Label(f1,bg='white').pack()
Button(f1,text='Train Between Stations',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f8)).pack()
#----------------------f2----------------------
Label(f2,text='INDIAN RAILWAY ENQUAIRY',width=50,height=2,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()
Label(f2,text='Enter Train Number',width=50,height=2,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()
e=Entry(f2,font=('arial',14,'bold'),bd=5,insertwidth=3)
e.pack()
Button(f2,text='Find Route',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",command=TrainRoute).pack()
label=Label(f2,fg="black",bg="#ffffff",text='')
label.pack()
Button(f2,text='Home',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f1)).pack()

#---------------------f3------------------------
Label(f3,text='INDIAN RAILWAY ENQUAIRY',width=50,height=2,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()
Label(f3,text='Enter train number',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e3=Entry(f3,font=('arial',14,'bold'),bd=10,insertwidth=1)
e3.pack()
Label(f3,text='Enter strating station code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e4=Entry(f3,font=('arial',14,'bold'),bd=10,insertwidth=1)
e4.pack()
Label(f3,text='Enter destination station code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()
e5=Entry(f3,font=('arial',14,'bold'),bd=10,insertwidth=1)
e5.pack()
Label(f3,text='Enter your age',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e6=Entry(f3,font=('arial',14,'bold'),bd=10,insertwidth=1)
e6.pack()
Label(f3,text='Enter class code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e7=Entry(f3,font=('arial',14,'bold'),bd=10,insertwidth=1)
e7.pack()
Label(f3,text='Enter Quota code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e8=Entry(f3,font=('arial',14,'bold'),bd=10,insertwidth=1)
e8.pack()
Label(f3,text='Enter date in (dd-mm-yyyy)',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e9=Entry(f3,font=('arial',14,'bold'),bd=10,insertwidth=1)
e9.pack()
Button(f3,text='Get train details',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",command=TrainDetails).pack()
label4=Label(f3,fg="black",bg="#ffffff",text='')
label4.pack()
Button(f3,text='Home',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f1)).pack()
#--------------------f4-------------------------
Label(f4,text='INDIAN RAILWAY ENQUAIRY',width=50,height=2,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()
e2=Entry(f4,font=('arial',14,'bold'),bd=10,insertwidth=3)
e2.pack()
Button(f4,text='Find PNR',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",command=PNR).pack()
label3=Label(f4,fg="black",bg="#ffffff",text='')
label3.pack()
Button(f4,text='Home',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f1)).pack()

#--------------------f5-------------------------
Label(f5,text='INDIAN RAILWAY ENQUAIRY',width=50,height=2,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()

Label(f5,text='Enter train number',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e10=Entry(f5,font=('arial',14,'bold'),bd=10,insertwidth=3)
e10.pack()
Label(f5,text='Enter strating station code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e11=Entry(f5,font=('arial',14,'bold'),bd=10,insertwidth=3)
e11.pack()
Label(f5,text='Enter destination station code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e12=Entry(f5,font=('arial',14,'bold'),bd=10,insertwidth=3)
e12.pack()
Label(f5,text='Enter date in (dd-mm-yyyy)',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e13=Entry(f5,font=('arial',14,'bold'),bd=10,insertwidth=3)
e13.pack()
Label(f5,text='Enter class code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e14=Entry(f5,font=('arial',14,'bold'),bd=10,insertwidth=3)
e14.pack()
Label(f5,text='Enter Quota code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e15=Entry(f5,font=('arial',14,'bold'),bd=10,insertwidth=3)
e15.pack()
Button(f5,text='Get train details',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold").pack()
label5=Label(f5,fg="black",bg="#ffffff",text='')
label5.pack()
Button(f5,text='Home',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f1)).pack()
#------------------f6---------------------------
Label(f6,text='INDIAN RAILWAY ENQUAIRY',width=50,height=2,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()
Label(f6,text='Enter train number',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e16=Entry(f6,font=('arial',14,'bold'),bd=10,insertwidth=3)
e16.pack()
Label(f6,text='Enter strating station code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e17=Entry(f6,font=('arial',14,'bold'),bd=10,insertwidth=3)
e17.pack()
Label(f6,text='Enter date in (dd-mm-yyyy)',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e18=Entry(f6,font=('arial',14,'bold'),bd=10,insertwidth=3)
e18.pack()
Button(f6,text='Get train details',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",command=LiveStatus).pack()
label6=Label(f6,fg="black",bg="#ffffff",text='')
label6.pack()
Button(f6,text='Home',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f1)).pack()
#-------------------f7--------------------------
Label(f7,text='INDIAN RAILWAY ENQUAIRY',width=50,height=2,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()
Button(f7,text='Home',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f1)).pack()
Label(f7,text='Enter date in (dd-mm-yyyy)',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e22=Entry(f7,font=('arial',14,'bold'),bd=10,insertwidth=3)
e22.pack()
Button(f7,text='Get train details',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",command=CanTrain).pack()
label7=Label(f7,fg="black",bg="#ffffff",text='')
label7.pack()
#--------------------f8-------------------------
Label(f8,text='INDIAN RAILWAY ENQUAIRY',width=50,height=2,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()
Button(f8,text='Home',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f1)).pack()
Label(f8,text='Enter strating station code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e19=Entry(f8,font=('arial',14,'bold'),bd=10,insertwidth=3)
e19.pack()
Label(f8,text='Enter destination station code',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e20=Entry(f8,font=('arial',14,'bold'),bd=10,insertwidth=3)
e20.pack()
Label(f8,text='Enter date in (dd-mm-yyyy)',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e21=Entry(f8,font=('arial',14,'bold'),bd=10,insertwidth=3)
e21.pack()
Button(f8,text='Get train details',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",command=bt2).pack()
label8=Label(f8,fg="black",bg="#ffffff",text='')
label8.pack()
#-------------------f9--------------------------
Label(f9,text='INDIAN RAILWAY ENQUAIRY',width=50,height=2,bg='white',fg='#0d4f3a',font="Helvetica 18 bold").pack()
Button(f9,text='Home',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",
       command=lambda:raise_frame(f1)).pack()
Label(f9,text='Enter date in (dd-mm-yyyy)',width=50,height=1,bg='white',fg='#0d4f3a',font="Helvetica 15 bold").pack()
e23=Entry(f9,font=('arial',14,'bold'),bd=10,insertwidth=3)
e23.pack()
Button(f9,text='Get train details',bg="#1eb887",fg="#ffffff",width=20,height=1,font="calibri 15 bold",command=RESTrain).pack()
label9=Label(f9,fg="black",bg="#ffffff",text='')
label9.pack()
#-----------------------------------------------
raise_frame(f1)
root.mainloop()
