import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *

def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get()
        if Subject=="":
            t='Please enter the Password.'
            text_to_speech(t)
        os.chdir(
            f"C:\\Users\\kumar\\OneDrive\\Desktop\\UnauthorizedAccessDetection-UnauthorizedAccessDetection\\Attendance\\{Subject}"
        )
        filenames = glob(
            f"C:\\Users\\kumar\\OneDrive\\Desktop\\UnauthorizedAccessDetection-UnauthorizedAccessDetection\\Attendance\\{Subject}\\{Subject}*.csv"
        )
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
            #newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv("attendance.csv", index=False)

        root = tkinter.Tk()
        #root.title("Attendance of "+Subject)
        root.configure(background="black")
        cs = f"C:\\Users\\kumar\\OneDrive\\Desktop\\UnauthorizedAccessDetection-UnauthorizedAccessDetection\\Attendance\\{Subject}\\attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0
            columns=list(reader)

            for col_index in range(len(columns)):
                
                    col=columns[col_index]
                    c = 0
                    for row_index in range(len(col)-1):
                        row=col[row_index]
                        label = tkinter.Label(
                            root,
                            width=10,
                            height=1,
                            fg="yellow",
                            font=("times", 15, " bold "),
                            bg="black",
                            text=row,
                            relief=tkinter.RIDGE,
                        )
                        label.grid(row=r, column=c)
                        c += 1
                    r += 1
        root.mainloop()
        print(newdf)

    subject = Tk()
    # windo.iconbitmap("AMS.ico")
    subject.title("Intruder Detection...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")
    # subject_logo = Image.open("UI_Image/0004.png")
    # subject_logo = subject_logo.resize((50, 47), Image.ANTIALIAS)
    # subject_logo1 = ImageTk.PhotoImage(subject_logo)
    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(subject, image=subject_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = tk.Label(
        subject,
        text="       Acess Log Details",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)

    def Attf():
        sub = tx.get()
        if sub == "":
            t="Please enter Password!!!"
            text_to_speech(t)
        else:
            os.startfile(
            f"C:\\Users\\kumar\\OneDrive\\Desktop\\UnauthorizedAccessDetection-UnauthorizedAccessDetection\\Attendance\\{sub}"
            )


    '''attf = tk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=10,
        relief=RIDGE,
    )
    attf.place(x=360, y=170)'''

    sub = tk.Label(
        subject,
        text="Password",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="View log",
        command=calculate_attendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=265, y=170)
    subject.mainloop()
