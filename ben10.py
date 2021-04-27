from tkinter import *

root = Tk()

root.title("Omnitrix")
# root.attributes('-fullscreen', True)
count = 0


def count_up():
    global count
    count += 1
    print(count)

def count_down():
    global count
    count -= 1
    print(count)

def start():
    print("start")

root.geometry("640x480")
root.configure(bg="#70b607")

omnitrix_screen = PhotoImage(file="omnitrix.png")

omnitrix_button = Button(root, image=omnitrix_screen, bg="#70b607",
                         activebackground='#70b607', highlightthickness=0, bd=0, command=start)

omnitrix_button.place(relx=0.5, rely=0.5, anchor=CENTER)

quit_button = Button(root, text="X", fg="white",command=root.destroy)
quit_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

omnitrix_left = Button(root, text="<", fg="white",command=count_down, highlightthickness=0, bd=0)
omnitrix_right = Button(root, text=">", fg="white",command=count_up, highlightthickness=0, bd=0)

omnitrix_left.pack(side="left")
omnitrix_right.pack(side="right")

root.mainloop()

