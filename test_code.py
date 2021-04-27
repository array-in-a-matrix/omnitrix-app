# # # Import module
# # from tkinter import *

# # # Create object
# # root = Tk()

# # # Adjust size
# # root.geometry("400x400")

# # # Add image file
# # bg = PhotoImage(file = "green.png")

# # # Create Canvas
# # canvas1 = Canvas( root, width = 400,
# # 				height = 400)

# # canvas1.pack(fill = "both", expand = True)

# # # Display image
# # canvas1.create_image( 0, 0, image = bg,
# # 					anchor = "nw")

# # # Add Text
# # canvas1.create_text( 200, 250, text = "Welcome")

# # # Create Buttons
# # button1 = Button( root, text = "Exit")
# # button3 = Button( root, text = "Start")
# # button2 = Button( root, text = "Reset")

# # # Display Buttons
# # button1_canvas = canvas1.create_window( 100, 10,
# # 									anchor = "nw",
# # 									window = button1)

# # button2_canvas = canvas1.create_window( 100, 40,
# # 									anchor = "nw",
# # 									window = button2)

# # button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",
# # 									window = button3)

# # # Execute tkinter
# # root.mainloop()


# # importing only those functions
# # which are needed
# from tkinter import *
# from tkinter.ttk import *

# # creating tkinter window
# root = Tk()

# # Adding widgets to the root window
# Label(root, text = 'GeeksforGeeks', font =(
# 'Verdana', 15)).pack(side = TOP, pady = 10)

# # Creating a photoimage object to use image
# photo = PhotoImage(file = r"/home/nasa/Documents/Projects/pythonGUI/omnitrix.png")

# # here, image option is used to
# # set image on button
# Button(root, text = 'Click Me !', image = photo).pack(side = TOP)

# mainloop()
# import tkinter module 
from tkinter import *   
  
# create a tkinter window
master = Tk()  
  
# Open window having dimension 200x100
master.geometry('200x100')  
    
# Create a Button
button = Button(master, 
                text = 'Submit', 
                bg='white', 
                activebackground='blue').pack()  
    
master.mainloop()