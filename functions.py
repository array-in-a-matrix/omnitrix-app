from aliens import *
from PIL import ImageTk, Image
from playsound import playsound as sound 

counter = 0

def count_up(omnitrix_button):
    sound("res/sound_switch.mp3")
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
    sound("res/sound_switch.mp3")
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
    sound("res/sound_transformation.mp3")



def skip_up(omnitrix_button):
    sound("res/sound_switch.mp3")
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
    sound("res/sound_switch.mp3")
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


def start():
    sound("res/sound_startup.mp3")


def image_display(index):
    alien = alien_table(index)
    if(alien == 0):
        global counter
        counter = 0
        return "res/Omnitrix.png"
    else:
        image_location = "res/" + alien + ".png"
        return image_location
