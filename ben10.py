from tkinter import *
from aliens import alien_table
from functions import *

root = Tk()
root.title("Omnitrix")
# root.attributes('-fullscreen', True)
root.geometry("640x480")
root.configure(bg="#70b607")
# root window parameters


def button_press():
    transform()
    omnitrix_button.config(image=PhotoImage(file="res/heatblast.png"))
# changes image


omnitrix_screen = PhotoImage(file="res/omnitrix.png")
omnitrix_button = Button(root, image=omnitrix_screen, bg="#70b607",
                         activebackground='#70b607', highlightthickness=0, bd=0, command=button_press)
omnitrix_button.place(relx=0.5, rely=0.5, anchor=CENTER)
# middle button

omnitrix_left = Button(root, text="<", fg="white", bg="black",
                       command=count_down, highlightthickness=0, bd=0, height=40, width=4)
omnitrix_left.pack(side="left")
# changes alien button (left)

omnitrix_right = Button(root, text=">", fg="white",  bg="black",
                        command=count_up, highlightthickness=0, bd=0, height=40, width=4)
omnitrix_right.pack(side="right")
# changes alien button (right)

quit_button = Button(root, text="X", fg="white", bg="black",
                     command=root.destroy, highlightthickness=0, bd=0, width=7)
quit_button.pack(side="bottom")
# kills program

root.mainloop()
