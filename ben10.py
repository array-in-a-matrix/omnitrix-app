from tkinter import *
from aliens import alien_table
from functions import *
root = Tk()

root.title("Omnitrix")
# root.attributes('-fullscreen', True)

root.geometry("640x480")
root.configure(bg="#70b607")

omnitrix_screen = PhotoImage(file="omnitrix.png")

omnitrix_button = Button(root, image=omnitrix_screen, bg="#70b607",
                         activebackground='#70b607', highlightthickness=0, bd=0, command=transform)

omnitrix_button.place(relx=0.5, rely=0.5, anchor=CENTER)

quit_button = Button(root, text="X", fg="white",command=root.destroy, highlightthickness=0, bd=0)
quit_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

omnitrix_left = Button(root, text="<", fg="white", bg="black" ,command=count_down, highlightthickness=0, bd=0, height = 20)
omnitrix_right = Button(root, text=">", fg="white",  bg="black" ,command=count_up, highlightthickness=0, bd=0, height = 20)

omnitrix_left.pack(side="left")
omnitrix_right.pack(side="right")

root.mainloop()

