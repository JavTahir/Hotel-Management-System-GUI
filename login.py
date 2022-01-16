from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="",
  database="hotel management system"
 
)

mycursor = mydb.cursor()

selectquery="SELECT * FROM `hotel manager`"
mycursor.execute(selectquery)
records=mycursor.fetchall()
print("login details",mycursor.rowcount)

for row in records:
    print("manager_name",row[0])
    print("manager_id",row[1])
   
    print()
mycursor.close()
mydb.close()


class Login:
   def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1199x600+100+50")
        self.root.configure(bg='red')
        self.root.resizable(False,False)
        self.bg =ImageTk.PhotoImage(file='C:\\Users\\genius computer\\Desktop\\HMS(gui).FA21-BCS-034\\hotel login\\hotel.png')
        self.bg_image=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
       
        

#login frame
        frame_login=Frame(self.root,bg="white")
        frame_login.place(x=10,y=100,height=340,width=400)

        title=Label(frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(frame_login,text="Enter your login details Here",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=80,y=100)
        lbl_user=Label(frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=80,y=140)
        self.txt_user=Entry(frame_login ,font=("times new roman",15),bg="lightgrey")
        self.txt_user.place(x=80,y=170,width=300,height=35)

        lbl_pass=Label(frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=80,y=210)
        self.txt_pass=Entry(frame_login ,font=("times new roman",15),bg="lightgrey",show="*")
        self.txt_pass.place(x=80,y=240,width=300,height=35)

    
        forget=Button(frame_login,text="Forget Passward?",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=80,y=280)
        login_but=Button(self.root,cursor="hand2",text="login",bg="#d77337",fg="white",font=("times new roman",20)).place(x=170,y=430,width=180,height=40)  

root=Tk()
obj=Login(root)
root.mainloop()
