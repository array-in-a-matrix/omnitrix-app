from aliens import *
from PIL import ImageTk, Image

counter = 0


def count_up(omnitrix_button):
    global counter
    counter += 1
    print(counter)
    if counter < 0:
        path = image_display(counter * -1)
    else:
        path = image_display(counter)
    img = ImageTk.PhotoImage(Image.open(path))
    omnitrix_button.configure(image=img)
    omnitrix_button.image = img  # keep a reference!


def count_down(omnitrix_button):
    global counter
    counter -= 1
    print(counter)
    if counter < 0:
        path = image_display(counter * -1)
    else:
        path = image_display(counter)
    img = ImageTk.PhotoImage(Image.open(path))
    omnitrix_button.configure(image=img)
    omnitrix_button.image = img  # keep a reference!


def button_press():
    if counter < 0:
        print(alien_table(counter * -1))
    elif counter == 0:
        print(alien_table(counter))
    elif counter > 0:
        print(alien_table(counter))
# ! replace with sound playing function


def skip_up(omnitrix_button):
    global counter
    counter += 5
    print(counter)
    if counter < 0:
        path = image_display(counter * -1)
    else:
        path = image_display(counter)
    img = ImageTk.PhotoImage(Image.open(path))
    omnitrix_button.configure(image=img)
    omnitrix_button.image = img  # keep a reference!


def skip_down(omnitrix_button):
    global counter
    counter -= 5
    print(counter)
    if counter < 0:
        path = image_display(counter * -1)
    else:
        path = image_display(counter)
    img = ImageTk.PhotoImage(Image.open(path))
    omnitrix_button.configure(image=img)
    omnitrix_button.image = img  # keep a reference!
