from tkinter import *
from aliens import alien_table
from functions import *
from PIL import ImageTk, Image

root = Tk()
root.title("Omnitrix")
root.attributes('-fullscreen', True)
root.geometry("640x480")
root.configure(bg="#70b607")
# root window parameters

path = "res/omnitrix.png"
img = ImageTk.PhotoImage(Image.open(path))

omnitrix_button = Button(root, bg="#70b607", image=img,
                         activebackground='#70b607', highlightthickness=0, bd=0,command=button_press)  
# TODO: make sound when pressed

omnitrix_button.image = img
omnitrix_button.place(relx=0.5, rely=0.5, anchor=CENTER)
# middle button

omnitrix_left = Button(root, text="<", fg="white", bg="black",
                       command=lambda: count_down(omnitrix_button), highlightthickness=0, bd=0, height=40, width=4)
omnitrix_left.pack(side="left")
# changes alien button (left)

skip_left = Button(root, text="<<<", fg="white", bg="black", highlightthickness=0, bd=0, width=4)
skip_left.pack()

omnitrix_right = Button(root, text=">", fg="white",  bg="black",
                        command=lambda: count_up(omnitrix_button), highlightthickness=0, bd=0, height=40, width=4)
omnitrix_right.pack(side="right")
# changes alien button (right)

skip_right = Button(root, text=">>>", fg="white", bg="black", highlightthickness=0, bd=0, width=4)
skip_right.pack()

quit_button = Button(root, text="X", fg="white", bg="black",
                     command=root.destroy, highlightthickness=0, bd=0, width=7)
quit_button.pack(side="bottom")
# kills program

root.mainloop()
