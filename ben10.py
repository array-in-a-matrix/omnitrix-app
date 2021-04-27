from tkinter import *

root = Tk()

root.title("Omnitrix")
root.attributes('-fullscreen', True)
count = 0


def count_up():
    global count
    count += 1
    print(count)


root.geometry("640x480")
root.configure(bg="#70b607")

omnitrix = PhotoImage(file="omnitrix.png")

omnitrix_button = Button(root, image=omnitrix, bg="#70b607",
                         activebackground='#70b607', highlightthickness=0, bd=0, command=count_up)

omnitrix_button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
