#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot  as plt
import tkinter
import seaborn as sns
import pandas as pd
import pickle


data=pd.read_json("data_for_plotting2.json.gz",compression="bz2")
#print(data.head())

class MyApp(tkinter.Frame):
  
  def __init__(self, master):
   self.month=1
   self.week_of_year=0
   self.u_hour=23
   self.l_hour=0
   self.day_of_week_U=6
   self.day_of_week_L=0
   self.week_of_year=1
   self.day_of_month_U=30
   self.day_of_month_L=1
   self.minute_U=60
   self.minute_L=0
   self.hue="passenger_count"
   self.a=tkinter.IntVar()
   self.b=tkinter.IntVar()
   tkinter.Frame.__init__(self, master)
   master.title("Filter_Data")
   master.minsize(width=250, height=100)
   self.grid()
   self.frame0=tkinter.Frame(master,bg="#CCFFE5")
   self.frame0.grid(row=0, column=0, columnspan=2,rowspan=1, sticky='ew')
   lablet = tkinter.Label(self.frame0,text="Click Update",font=("Courier",18),bg="#CCFFE5")
   lablet.text ="Filter"
   lablet.grid(row=1, column=0)
   
   #frame 1
   self.frame1=tkinter.Frame(master,bg="#FFFFFF")
   self.frame1.grid(row=2, column=0, columnspan=2,rowspan=1, sticky='ew')
   self.month_slider=tkinter.Scale(self.frame1,label="Month",from_=1, to=6,orient="horizontal",bg="#FFFFFF")
   self.month_slider.grid(row=2,column=1)
   self.Go_month=tkinter.Button(self.frame1,text="Update_Month", command=self.use_month,bg="#FFFFFF")
   self.Go_month.grid(row=2,column=0)
   
   self.lablem = tkinter.Label(text=self.month,font=("Courier",20))
   self.lablem.text =self.month
   self.lablem.grid(row=2, column=3)
   
   self.day_month_slider_U=tkinter.Scale(self.frame1,label="Upper",from_=1, to=30,orient="horizontal",background="#FFFFFF")
   self.day_month_slider_U.grid(row=3,column=1)
   self.day_month_slider_U.set(30)
   self.day_month_slider_L=tkinter.Scale(self.frame1,label="Lower",from_=1, to=30,orient="horizontal",background="#FFFFFF")
   self.day_month_slider_L.grid(row=4,column=1)
   self.Go_day_month=tkinter.Button(self.frame1,text="Update___Day", command=self.day_of_month,background="#FFFFFF")
   self.Go_day_month.grid(row=5,column=0)
   
   self.Radio_month=tkinter.Radiobutton(text="Use Month",command=self.Radio_month_func,variable=self.a,value=4)
   self.Radio_month.grid(row=2,column=2)
   self.Radio_month.select()
   
   
   
   
   
   #frame2
   self.frame2=tkinter.Frame(master,bg="#C0C0C0")
   self.frame2.grid(row=6, column=0, columnspan=2,rowspan=1, sticky='ew')
      
   self.week_of_year_slider=tkinter.Scale(self.frame2,label="Week_of_year",from_=1, to=25,orient="horizontal",background="#C0C0C0")
   self.week_of_year_slider.grid(row=6,column=1)
   self.Go_week_of_year=tkinter.Button(self.frame2,text="Update_Week", command=self.use_week,background="#C0C0C0")
   self.Go_week_of_year.grid(row=7,column=0)
   
   self.Radio_week=tkinter.Radiobutton(text="Use week",command=self.Radio_week_func,variable=self.a,value=2)
   self.Radio_week.grid(row=6,column=2)
   
   self.lablew = tkinter.Label(text=self.week_of_year,font=("Courier",20))
   self.lablew.text =self.week_of_year
   self.lablew.grid(row=6, column=3)
   #frame3
   #self.frame3=tkinter.Frame(master,bg="#ffe7ca")
   #self.frame3.grid(row=8, column=0, columnspan=2,rowspan=2, sticky='ew')
   
   self.day_week_slider_U=tkinter.Scale(self.frame2,label="Upper",from_=0, to=6,orient="horizontal",background="#C0C0C0")
   self.day_week_slider_U.grid(row=8,column=1)
   self.day_week_slider_U.set(6)
   self.day_week_slider_L=tkinter.Scale(self.frame2,label="Lower",from_=0, to=6,orient="horizontal",background="#C0C0C0")
   self.day_week_slider_L.grid(row=9,column=1)
   self.Go_day_week=tkinter.Button(self.frame2,text="Update___Day", command=self.day_of_week,background="#C0C0C0")
   self.Go_day_week.grid(row=9,column=0)
   
   #self.Radio_day=tkinter.Radiobutton(text="Use Weekday",command=self.Radio_day_func,variable=self.a,value=3)
   #self.Radio_day.grid(row=8,column=2)
   
   #frame 4
   self.frame4=tkinter.Frame(master,bg="#5bd0ea")
   self.frame4.grid(row=10, column=0, columnspan=2,rowspan=2, sticky='ew')
   self.hour_slider_U=tkinter.Scale(self.frame4,label="Upper",from_=0, to=23,orient="horizontal",background="#5bd0ea")
   self.hour_slider_U.grid(row=10,column=1)
   self.hour_slider_U.set(23)
   self.hour_slider_L=tkinter.Scale(self.frame4,label="Lower",from_=0, to=23,orient="horizontal",background="#5bd0ea")
   self.hour_slider_L.grid(row=11,column=1)
   self.Go_hour=tkinter.Button(self.frame4,text="Update_Hour", command=self.use_hour,background="#5bd0ea")
   self.Go_hour.grid(row=11,column=0)
   
   self.minute_slider_U=tkinter.Scale(self.frame4,label="Upper",from_=0, to=59,orient="horizontal",background="#5bd0ea")
   self.minute_slider_U.grid(row=12,column=1)
   self.minute_slider_U.set(60)
   self.minute_slider_L=tkinter.Scale(self.frame4,label="Lower",from_=0, to=59,orient="horizontal",background="#5bd0ea")
   self.minute_slider_L.grid(row=13,column=1)
   self.Go_minute=tkinter.Button(self.frame4,text="Update_minute", command=self.use_minute,background="#5bd0ea")
   self.Go_minute.grid(row=13,column=0)
   
   self.Go_plot=tkinter.Button(text="Generate_plot", command=self.generate_plot)
   self.Go_plot.grid(row=11,column=2)
   
   #self.lablehue = tkinter.Label(text="Use_Hue",font=("Courier",15))
   #self.lablehue.text ="Use_Hue"
   #self.lablehue.grid(row=10, column=2)
   self.Radio_week=tkinter.Radiobutton(text="Plot_passenger_count",command=self.Pasenger_count,variable=self.b,value=2)
   self.Radio_week.grid(row=10,column=2)
   self.Radio_week=tkinter.Radiobutton(text="Plot_Trip_duration",command=self.Trip_duration,variable=self.b,value=3)
   self.Radio_week.grid(row=10,column=3)
   #def set_week_month(self,):
   #self.month=self.month_slider.get()
   #self.week=self.week_slider.get()
   self.Radio_month_func()
  def Pasenger_count(self,):
   self.hue="passenger_count"
  def Trip_duration(self,):
   self.hue="lables_duration"
  def use_minute(self,):
   self.minute_U=self.minute_slider_U.get()
   self.minute_L=self.minute_slider_L.get()
   print(self.minute_U,self.minute_L,"minute_U,minute_L")
  def use_month(self,):
    self.month=self.month_slider.get()
    self.lablem.configure(text=self.month)
    print(self.month,"month")
  def day_of_month(self,):
    self.day_of_month_U=self.day_month_slider_U.get()
    self.day_of_month_L=self.day_month_slider_L.get()
    print(self.day_of_month_U,self.day_of_month_L,"L_day_month,U_day_month")
  def use_week(self,):
    self.week_of_year=self.week_of_year_slider.get()
    self.lablew.configure(text=self.week_of_year)
    print(self.week_of_year,"week_of_year")
	
  def day_of_week(self,):
    self.day_of_week_U=self.day_week_slider_U.get()
    self.day_of_week_L=self.day_week_slider_L.get()
    print(self.day_of_week_U,self.day_of_week_L,"U-day_week,L-day_week")
	
  def use_hour(self,):
    self.u_hour=self.hour_slider_U.get()
    self.l_hour=self.hour_slider_L.get()
    print(self.u_hour,self.l_hour,"U-hour,L-hour")
	
  def Radio_month_func(self,):
    self.month_lock=0
    self.week_lock=1
    self.week_of_year_slider.set(0)
    self.day_week_slider_U.set(6)
    self.day_week_slider_L.set(0)
    
    for child in self.frame2.winfo_children():
        child.configure(state="disabled")
    for child in self.frame1.winfo_children():
        child.configure(state="normal")
        
  def Radio_week_func(self,):
    self.week_lock=0
    self.month_lock=1
    self.month_slider.set(0)
    self.day_week_slider_U.set(6)
    self.day_week_slider_L.set(0)
    self.day_month_slider_U.set(30)
    self.day_month_slider_L.set(1)	
    for child in self.frame1.winfo_children():
        child.configure(state="disabled")
    
    for child in self.frame2.winfo_children():
        child.configure(state="normal",)
	 
  """'def Radio_day_func(self,):
    self.week_lock=1
    self.month_lock=1
    self.month_slider.set(0)
    self.week_of_year_slider.set(0)
    self.day_month_slider_U.set(30) 
    self.day_month_slider_L.set(1)
    for child in self.frame1.winfo_children():
        child.configure(state="disabled")
    for child in self.frame2.winfo_children():
        child.configure(state="disabled")
    for child in self.frame3.winfo_children():
        child.configure(state="normal")"""
  def generate_plot(self,):
   if self.month_lock==0:
    if self.day_of_month_L>self.day_of_month_U:
     temp1=self.day_of_month_L
     temp2=self.day_of_month_U
     self.day_of_month_U=temp1
     self.day_of_month_L=temp2
    if self.l_hour>self.u_hour:
     temp1=self.l_hour
     temp2=self.u_hour
     self.u_hour=temp1
     self.l_hour=temp2
    if self.minute_L>self.minute_U:
     temp1=self.minute_L
     temp2=self.minute_U
     self.minute_U=temp1
     self.minute_L=temp2
    tempdf1=pd.DataFrame(data[data['month']==self.month])
    tempdf2=tempdf1[tempdf1['day_of_motnth'].between(self.day_of_month_L,self.day_of_month_U,inclusive=True)]
    tempdf3=tempdf2[tempdf2['hour'].between(self.l_hour,self.u_hour,inclusive=True)]
    tempdf4=tempdf3[tempdf3['minute'].between(self.minute_L,self.minute_U,inclusive=True)]
    sns.factorplot(data=tempdf4,x="day_of_motnth",y="hour",hue=self.hue,kind="point")
    plt.show()
   #elif self.day_lock==0:
    
   elif self.week_lock==0:
    if self.day_of_week_L>self.day_of_week_U:
     temp1=self.day_of_week_L
     temp2=self.day_of_week_U
     self.day_of_week_U=temp1
     self.day_of_week_L=temp2
    if self.l_hour>self.u_hour:
     temp1=self.l_hour
     temp2=self.u_hour
     self.u_hour=temp1
     self.l_hour=temp2
    tempdf0=data[data['week_of_year']==self.week_of_year]
    tempdf1=tempdf0[tempdf0['day_of_week'].between(self.day_of_week_L,self.day_of_week_U,inclusive=True)]
    tempdf2=tempdf1[tempdf1['hour'].between(self.l_hour,self.u_hour,inclusive=True)]
    sns.factorplot(data=tempdf2,x="day_of_week",y="hour",hue=self.hue,kind="point")
    plt.show()
    


    
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()	
 

