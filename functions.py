from aliens import *
from PIL import ImageTk, Image
from boombox import BoomBox
counter = 0
# determans which image is shown


def alien_select(index, omnitrix_button):
    BoomBox("res/sound_switch.mp3").play()
    global counter
    counter += index
    path = image_display(abs(counter))
    img = ImageTk.PhotoImage(Image.open(path))
    omnitrix_button.configure(image=img)
    omnitrix_button.image = img  # keep a reference
# controls how much up or down the list you go


def button_press():
    BoomBox("res/sound_transformation.mp3").play()
# whenever the "middle_button" button is pressed play sound effect


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
