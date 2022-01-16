from tkinter import *

from tkinter import ttk


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Manager")
        self.root.geometry("1550x800+0+0")

        lbltitle=Label(self.root,text="HOTEL MANAGER",bg="black",fg="red",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="red")
        frame.place(x=0,y=130,width=1543,height=400)
        lblNo_of_rooms_available = Label(frame,bg="red",text="Rooms available",font=("times new roman",15,"bold"),padx=10,pady=24)
        lblNo_of_rooms_available.grid(row=1,column=0,sticky=W)
        txtNo_of_rooms_available=Entry(frame,font=("times new roman",15,"bold"),width=29)
        txtNo_of_rooms_available.grid(row=1,column=1)

        lblNo_of_dishes_perevent=Label(frame,bg="red",text="No of Dishes per event",font=("times new roman",15,"bold"),padx=5, pady=24)
        lblNo_of_dishes_perevent.grid(row=2,column=0,sticky=W)
        txtNo_of_dishes_perevent = Entry(frame,font=("times new roman", 15, "bold"),width=29)
        txtNo_of_dishes_perevent.grid(row=2,column=1)

        lblInfrastructure_required=Label(frame,bg="red",text="Infrastructure req",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblInfrastructure_required.grid(row=3,column=0,sticky=W)

        comMember= ttk.Combobox(frame,font=("times new roman",15,"bold"),width=27,state="readonly")
        comMember["value"]=("decorations", "tables","chairs","washroom supplies","grocery")
        comMember.grid(row=3,column=1)

        lblNo_of_Bookings = Label(frame,bg="red",text="Bookings",font=("times new roman",15,"bold"),padx=100,pady=24)
        lblNo_of_Bookings.grid(row=1,column=4,sticky=W)
        txtNo_of_Bookings=Entry(frame,font=("times new roman",15,"bold"),width=29)
        txtNo_of_Bookings.grid(row=1,column=5)

        lblNo_of_Employees=Label(frame,bg="red",text="No of Employees",font=("times new roman",15,"bold"),padx=100, pady=24)
        lblNo_of_Employees.grid(row=2,column=4,sticky=W)
        txtNo_of_Employees = Entry(frame,font=("times new roman", 15, "bold"),width=29)
        txtNo_of_Employees.grid(row=2,column=5)

        lblNo_of_events =Label(frame,bg="red",text="No of Events",font=("times new roman", 15,"bold"),padx=100, pady=24)
        lblNo_of_events.grid(row=3, column=4, sticky=W)
        txtNo_of_events = Entry(frame, font=("times new roman", 15, "bold"), width=29)
        txtNo_of_events.grid(row=3, column=5)

        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="black")
        Framebutton.place(x=0, y=530, width=1543, height=70)

        btnAddData=Button(Framebutton,text="Add Data",font=("arial",12,"bold"),width=20,bg="yellow",fg="black")
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


#Information frame

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="black")
        FrameDetails.place(x=0, y=600, width=1543, height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="black")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.hotel_table=ttk.Treeview(Table_frame,column=("Rooms available","Bookings","No of dishes per event","No of Employees","Infrastructure req","No of Events"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.hotel_table.xview)
        yscroll.config(command=self.hotel_table.yview)


        self.hotel_table.heading("Rooms available",text="Rooms Available")
        self.hotel_table.heading("Bookings", text="Bookings")
        self.hotel_table.heading("No of dishes per event", text="No of dishes per event")
        self.hotel_table.heading("No of Employees", text="No of Employees")
        self.hotel_table.heading("Infrastructure req", text="Infrastructure req")
        self.hotel_table.heading("No of Events", text="No of Events")
        

        self.hotel_table["show"] ="headings"
        self.hotel_table.pack(fill=BOTH , expand=1)

        self.hotel_table.column("Rooms available",width=30)
        self.hotel_table.column("Bookings", width=30)
        self.hotel_table.column("No of dishes per event", width=30)
        self.hotel_table.column("No of Employees", width=30)
        self.hotel_table.column("Infrastructure req", width=30)
        self.hotel_table.column("No of Events",width=170)
        




        


       
if __name__== "__main__":
           root=Tk()
           obj=HotelManagementSystem(root)
           root.mainloop()

