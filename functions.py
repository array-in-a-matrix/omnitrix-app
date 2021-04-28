from aliens import *

counter= 0

def count_up():
    global counter
    counter+= 1
    # print(counter)

def count_down():
    global counter
    counter-= 1
    # print(counter)

def transform():
    if counter < 0:
        print(alien_table(counter * -1))
    elif counter == 0:
        print(alien_table(counter))
    elif counter > 0:
        print(alien_table(counter))
#     change_image(counter)

# def change_image(counter):
#     omnitrix_screen = PhotoImage(file= image_display(counter))
