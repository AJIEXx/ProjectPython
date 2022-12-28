# Now let’s see how to create a digital clock GUI application with Python. I will first start with importing the libraries:
#
# 1
# from tkinter import Label, Tk
# 2
# import time
# Now let’s define the title and size of our application. Note that in the code below I will set both the height and width of the resizable function as True(1,1) if you want a fixed window and don’t want to maximize or minimize the output you can set it to False(0,0):
#
# 1
# app_window = Tk()
# 2
# app_window.title("Digital Clock")
# 3
# app_window.geometry("420x150")
# 4
# app_window.resizable(1,1)
# Now here I will define the font of the time and its colour, its border width and the background colour of the digital clock:
#
# 1
# text_font= ("Boulder", 68, 'bold')
# 2
# background = "#f2e750"
# 3
# foreground= "#363529"
# 4
# border_width = 25
# Now here I will combine all the elements to define the label of the clock application:
#
# 1
# label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
# 2
# label.grid(row=0, column=1)
# Now let’s define the main function of our digital clock. Here I will set the text of the label as the realtime:
#
# 1
# def digital_clock():
# 2
#    time_live = time.strftime("%H:%M:%S")
# 3
#    label.config(text=time_live)
# 4
#    label.after(200, digital_clock)
# Now let’s run and see our output:
#
# 1
# digital_clock()
# 2
# app_window.mainloop()


from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()