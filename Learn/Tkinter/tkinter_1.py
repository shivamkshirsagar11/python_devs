from tkinter import *
from PIL import Image,ImageTk
root = Tk()
#--------------------------------------------
#all code goes here
root.title("TicTacToe")
root.geometry("450x500")
Label(text="Copyright @github.com/shivamkshirsagar11",cursor="heart",bd=3,width=50,bg="pink",foreground="purple",relief=RAISED).pack()
Label(text="Tic Tac Toe",cursor="mouse",foreground="darkred",bg="yellow",relief=RIDGE,font=("sans",16)).pack()
photo = Image.open("t1.png")
photo2 = ImageTk.PhotoImage(photo)
pic_lable = Label(image = photo2,relief=SUNKEN)
pic_lable.pack()

root.minsize(200,200)
root.maxsize(600,500)

#--------------------------------------------
# end of app but iterate all 
root.mainloop()