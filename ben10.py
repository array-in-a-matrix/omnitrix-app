from tkinter import *
from aliens import alien_table
from functions import *
from PIL import ImageTk, Image

start()
# start up sound effect

background = "#70b607"

root = Tk()
root.title("Omnitrix")
# root.attributes('-fullscreen', True)
root.geometry("640x480")
root.configure(bg=background)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
# root window parameters


path = "res/Omnitrix.png"
img = ImageTk.PhotoImage(Image.open(path))
omnitrix_button = Button(root, bg=background, image=img, activebackground=background,
                         highlightthickness=0, bd=0, command=button_press)
omnitrix_button.image = img
omnitrix_button.grid(column=1, row=0, rowspan=3, columnspan=2)
# middle button


omnitrix_left_skip = Button(root, text="<<<", fg="white", bg="black", command=lambda: alien_select(-5, omnitrix_button),
                            highlightthickness=0, bd=0, height=5, width=4)
omnitrix_left_skip.grid(column=0, row=0)
# bulk skip left button

omnitrix_right_skip = Button(root, text=">>>", fg="white",  bg="black", command=lambda: alien_select(5, omnitrix_button),
                             highlightthickness=0, bd=0, height=5, width=4)
omnitrix_right_skip.grid(column=3, row=0)
# bulk skip right button


omnitrix_left = Button(root, text="<", fg="white", bg="black",
                       command=lambda: alien_select(-1, omnitrix_button), highlightthickness=0, bd=0, height=30, width=4)
omnitrix_left.grid(column=0, row=1, rowspan=3)
# changes alien button (left)

omnitrix_right = Button(root, text=">", fg="white",  bg="black",
                        command=lambda: alien_select(1, omnitrix_button), highlightthickness=0, bd=0, height=30, width=4)
omnitrix_right.grid(column=3, row=1, rowspan=3)
# changes alien button (right)


quit_button = Button(root, text="X", fg="white", bg="black",
                     command=root.destroy, highlightthickness=0, bd=0, width=10, height=2)
quit_button.grid(column=1, row=3, columnspan=2)
# kills program

root.mainloop()
