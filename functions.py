from aliens import *
from PIL import ImageTk, Image
from boombox import BoomBox 

counter = 0
# determans which image is shown

def count_up(omnitrix_button):
    BoomBox("res/sound_switch.mp3").play()
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
# whenever "omnitrix_left" button is pressed, plays sound effect, adds 1 to the counter and change the image  

def count_down(omnitrix_button):
    BoomBox("res/sound_switch.mp3").play()
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
# whenever "omnitrix_left" button is pressed, plays sound effect, subtracts 1 to the counter and change the image  


def button_press():
     BoomBox("res/sound_transformation.mp3").play()
# whenever the "middle_button" button is pressed play sound effect


def skip_up(omnitrix_button):
    BoomBox("res/sound_switch.mp3").play()
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
# whenever "omnitrix_left_skip" button is pressed, plays sound effect, adds 5 to the counter and change the image  


def skip_down(omnitrix_button):
    BoomBox("res/sound_switch.mp3").play()
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
# whenever "omnitrix_right_skip" button is pressed, plays sound effect, subtracts 5 to the counter and change the image  


def start():
     BoomBox("res/sound_startup.mp3").play()
# when program first starts up, plays sound effect

def image_display(index):
    alien = alien_table(index)
    if(alien == 0):
        global counter
        counter = 0
        return "res/Omnitrix.png"
    else:
        image_location = "res/" + alien + ".png"
        return image_location
# if the next alien does not exists, resets counter, else returns image location 