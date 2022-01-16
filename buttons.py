from tkinter import *

from PIL import ImageTk, Image
gui = Tk()
#set window size
gui.geometry("1550x800")
gui.title("Menu")
gui.bg =ImageTk.PhotoImage(file='C:\\Users\\genius computer\\Desktop\HMS(gui).FA21-BCS-034\\hotel login\\blury.png')
gui.bg_image=Label(gui,image=gui.bg).place(x=0, y=0, relwidth=1, relheight=1)
       
# Open the Image File
bg = ImageTk.PhotoImage(file="blury.png")

# Create a Canvas
canvas = Canvas(gui, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("blury.png")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
gui.bind("<Configure>", resize_image)

#image on button
image = Image.open('manager.png')
#Resize the Image
image = image.resize((50,50), Image.ANTIALIAS)
#Convert the image to PhotoImage
img_but= ImageTk.PhotoImage(image)



login_but=Button(gui,cursor="hand2",text="Hotel Manager" ,bg="grey",fg="black",font=("Helvetica",20,"bold"),image=img_but,compound=LEFT).place(x=250,y=300,width=300,height=200)

image = Image.open('customer.png')
#Resize the Image
image = image.resize((50,50), Image.ANTIALIAS)
#Convert the image to PhotoImage
img= ImageTk.PhotoImage(image) 
login_but=Button(gui,cursor="hand2",text="Customer" ,bg="grey",fg="black",font=("Helvetica",20,"bold"),image=img, compound=LEFT).place(x=800,y=300,width=300,height=200)  

gui.mainloop()