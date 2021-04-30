from tkinter import *
from aliens import alien_table
from functions import *
from PIL import ImageTk, Image

root = Tk()
root.title("Omnitrix")
# root.attributes('-fullscreen', True)
root.geometry("640x480")
root.configure(bg="#70b607")
# root window parameters


# grid to hold buttons

path = "res/omnitrix.png"
img = ImageTk.PhotoImage(Image.open(path))

omnitrix_button = Button(root, bg="#70b607", image=img,
                         activebackground='#70b607', highlightthickness=0, bd=0, command=button_press)
# TODO: make sound when pressed

omnitrix_button.image = img
# omnitrix_button.place(relx=0.5, rely=0.5, anchor=CENTER)
omnitrix_button.grid(column=1, row=1, rowspan=2, columnspan=2)
# middle button

omnitrix_left_skip = Button(root, text="<<<", fg="white", bg="black",
                            highlightthickness=0, bd=0, height=10, width=4)
# omnitrix_left_skip.pack(side="left")
omnitrix_left_skip.grid(column=0, row=0,  sticky=NW)
# bulk skip left button

omnitrix_right_skip = Button(root, text=">>>", fg="white",  bg="black",
                             highlightthickness=0, bd=0, height=10, width=4)
# omnitrix_right_skip.pack(side="right")
omnitrix_right_skip.grid(column=3, row=0,  sticky=NE)
# bulk skip right button

omnitrix_left = Button(root, text="<", fg="white", bg="black",
                       command=lambda: count_down(omnitrix_button), highlightthickness=0, bd=0, height=10, width=4)
# omnitrix_left.pack(side="left")
omnitrix_left.grid(column=0, row=1, sticky=W, rowspan=2)
# changes alien button (left)

omnitrix_right = Button(root, text=">", fg="white",  bg="black",
                        command=lambda: count_up(omnitrix_button), highlightthickness=0, bd=0, height=10, width=4)
# omnitrix_right.pack(side="right")
omnitrix_right.grid(column=3, row=1, sticky=E, rowspan=2)
# changes alien button (right)

quit_button = Button(root, text="X", fg="white", bg="black",
                     command=root.destroy, highlightthickness=0, bd=0, width=7)
# quit_button.pack(side="bottom")
quit_button.grid(column=1, row=3, sticky=S, columnspan=2)
# kills program

change_entry = Entry(root,fg="black", bg="white",
                     highlightthickness=0, bd=0, width=7)
# quit_button.pack(side="bottom")
change_entry.grid(column=1, row=0, sticky=N, columnspan=2)
#
root.mainloop()
