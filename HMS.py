from tkinter import*
from tkinter import ttk
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="",
  database="hotel management system"
 
)

mycursor = mydb.cursor()

selectquery="SELECT * FROM customer_info"
mycursor.execute(selectquery)
records=mycursor.fetchall()
print("Customer info",mycursor.rowcount)

for row in records:
    print("first name",row[0])
    print("last name",row[1])
    print("customer id",row[2])
    print("contact_no",row[4])
    print()
mycursor.close()
mydb.close()


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

       
        

        lbltitle=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",bg="black",fg="red",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="black")
        frame.place(x=0,y=130,width=1543,height=400)
        # ==================================DateFrameLeft========================================
        DataFrameLeft=LabelFrame(frame,text="Hotel Membership Information",bg="red",fg="black",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)


        lblMember=Label(DataFrameLeft,bg="red",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember= ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff", "customer")
        comMember.grid(row=0,column=1)

        lblFirst_Name = Label(DataFrameLeft,bg="red",text="First Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblFirst_Name.grid(row=1,column=0,sticky=W)
        txtFirst_Name=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=29)
        txtFirst_Name.grid(row=1,column=1)

        lblLast_Name=Label(DataFrameLeft,bg="red",text="Last Name",font=("times new roman",15,"bold"),padx=2, pady=6)
        lblLast_Name.grid(row=2,column=0,sticky=W)
        txtLast_Name = Entry(DataFrameLeft,font=("times new roman", 15, "bold"),width=29)
        txtLast_Name.grid(row=2,column=1)

        lblID_No =Label(DataFrameLeft,bg="red",text="ID No",font=("times new roman", 15,"bold"),padx=2, pady=6)
        lblID_No.grid(row=3, column=0, sticky=W)
        txtID_No = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        txtID_No.grid(row=3, column=1)

        lblReservation =Label(DataFrameLeft,bg="red",text="Reservation",font=("times new roman", 15, "bold"),padx=2,pady=6)
        lblReservation.grid(row=4, column=0, sticky=W)
        txtReservation = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        txtReservation.grid(row=4, column=1)

        lblContact_no =Label(DataFrameLeft,bg="red",text="Contact no",font=("times new roman", 15,"bold"),padx=2,pady=6)
        lblContact_no.grid(row=5, column=0, sticky=W)
        txtContact_no = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        txtContact_no.grid(row=5, column=1)

        lblAddress=Label(DataFrameLeft,bg="red",text="Address",font=("times new roman", 15,"bold"),padx=2,pady=6)
        lblAddress.grid(row=6, column=0, sticky=W)
        txtAddress = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        txtAddress.grid(row=6, column=1)

        lblRoom_id =Label(DataFrameLeft,bg="red",text="Room Id",font=("times new roman", 15,"bold"),padx=2,pady=6)
        lblRoom_id.grid(row=7, column=0, sticky=W)
        txtRoom_id = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        txtRoom_id.grid(row=7, column=1)

        lblDate_in =Label(DataFrameLeft,bg="red",text="Date in",font=("times new roman", 15,"bold"),padx=2,pady=6)
        lblDate_in.grid(row=0, column=2, sticky=W)
        txtDate_in = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        txtDate_in.grid(row=0, column=3)

        lblDate_out =Label(DataFrameLeft,bg="red",text="Date out",font=("times new roman", 15,"bold"),padx=2,pady=6)
        lblDate_out.grid(row=0, column=2, sticky=W)
        txtDate_out = Entry(DataFrameLeft, font=("times new roman", 15, "bold"), width=29)
        txtDate_out.grid(row=0, column=3)



        # ===============================DataFrameRight========================================

        DataFrameRight=LabelFrame(frame,text="Room Details",bg="black",fg="red",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)



        listRoomTypes=['Luxury','Classic','Single','Quad','Queen','Twin','Studio']

        
        



                



        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        
        listBox.grid(row=0,column=0,padx=4)

        for item in listRoomTypes:
            listBox.insert(END,item)

        # ============================Buttons Frame======================================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="black")
        Framebutton.place(x=0, y=530, width=1543, height=70)

        btnAddData=Button(Framebutton,font=("arial",12,"bold"),width=20,bg="yellow",fg="black")
        btnAddData.grid(row=0,column=0)

        btnAddData = Button(Framebutton, text="Show Data", font=("arial", 12, "bold"), width=20, bg="yellow", fg="black")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(Framebutton, text="Update", font=("arial", 12, "bold"), width=20, bg="yellow", fg="black")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(Framebutton, text="Delete", font=("arial", 12, "bold"), width=20, bg="yellow", fg="black")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(Framebutton, text="Reset", font=("arial", 12, "bold"), width=20, bg="yellow", fg="black")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(Framebutton, text="Exit", font=("arial", 12, "bold"), width=20, bg="yellow", fg="black")
        btnAddData.grid(row=0, column=5)



        # ============================Information Frame======================================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="black")
        FrameDetails.place(x=0, y=600, width=1543, height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="black")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.hotel_table=ttk.Treeview(Table_frame,column=("MemberType","FirstName","LastName","IDNo","Reservation","Contact_no","Address","Room_id","Date_in","Date_out"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.hotel_table.xview)
        yscroll.config(command=self.hotel_table.yview)


        self.hotel_table.heading("MemberType",text="Member Type")
        self.hotel_table.heading("FirstName", text="First Name")
        self.hotel_table.heading("LastName", text="Last Name")
        self.hotel_table.heading("IDNo", text="ID No")
        self.hotel_table.heading("Reservation", text="Reservation")
        self.hotel_table.heading("Contact_no", text="Contact_no")
        self.hotel_table.heading("Address", text="Address")
        self.hotel_table.heading("Room_id", text="Room_id")
        self.hotel_table.heading("Date_in", text="Date_in")
        self.hotel_table.heading("Date_out", text="Date_out")

        self.hotel_table["show"] ="headings"
        self.hotel_table.pack(fill=BOTH , expand=1)

        self.hotel_table.column("MemberType",width=50)
        self.hotel_table.column("FirstName", width=50)
        self.hotel_table.column("LastName", width=50)
        self.hotel_table.column("IDNo", width=50)
        self.hotel_table.column("Reservation", width=50)
        self.hotel_table.column("Contact_no",width=50)
        self.hotel_table.column("Address", width=50)
        self.hotel_table.column("Room_id", width=50)
        self.hotel_table.column("Date_in", width=50)
        self.hotel_table.column("Date_out", width=50)


    


if __name__== "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

