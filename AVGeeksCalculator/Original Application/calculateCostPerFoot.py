from tkinter import *
from tkinter import messagebox
import math

Font_tuple = ("Arial", 15, "bold")


#function to calculate total price
def calculateFootage():
    global hourEntry
    global minuteEntry
    global secEntry
    global frameEntry
    global fpsEntry
    global clicked

    if(len(hourEntry.get()) != 0 and len(minuteEntry.get()) != 0 and len(secEntry.get()) != 0):
        hours = int(hourEntry.get())
        minutes = int(minuteEntry.get())
        secs = int(secEntry.get())
        errorMessageLabel.configure(text = "")
    else:
        errorMessageLabel.configure(text="Please input running time numbers. (input 0 if none)")

    totalSeconds = (hours * 3600) + (minutes * 60) + secs

    if(len(fpsEntry.get()) != 0):
        fps = int(fpsEntry.get())
        errorMessageLabel.configure(text="")
    else:
        errorMessageLabel.configure(text="Please input a number for fps. (input 0 if none)")

    totalFrames = (fps * totalSeconds)

    if (clicked.get() == "16 mm"):
        totalFeet = totalFrames / 40

    if (clicked.get() == "Regular 8"):
        totalFeet = totalFrames / 79

    if (clicked.get() == "Super 8"):
        totalFeet = totalFrames / 72

    if (clicked.get() == "9.5 approx."):
        totalFeet = totalFrames / 40

    if (clicked.get() == "35 mm"):
        totalFeet = totalFrames / 16


    tenLabelOut.configure(text = round((totalFeet * 0.10),2))
    twelveLabelOut.configure(text = round((totalFeet * 0.12),2))
    fifteenLabelOut.configure(text = round((totalFeet * 0.15),2))
    twentyLabelOut.configure(text = round((totalFeet * 0.20),2))
    thirtyLabelOut.configure(text = round((totalFeet * 0.30),2))
    fortyLabelOut.configure(text = round((totalFeet * 0.40),2))
    fifteyLabelOut.configure(text = round((totalFeet * 0.50),2))
    footageLabelOut.configure(text = totalFeet)
    frameLabelOut.configure(text = totalFrames)

def calculateRunTime():
    global frameEntry
    global fpsEntry
    global footageEntry
    global clicked

    if(len(fpsEntry.get()) != 0):
        fps = int(fpsEntry.get())
    else:
        errorMessageLabel.configure(text="Please input a number for fps. (input 0 if none)")

    if(len(footageEntry.get()) != 0):
        totalFeet = int(footageEntry.get())

    elif(len(footageEntry.get()) == 0 and len(frameEntry.get()) != 0):

        totalFrames = int(frameEntry.get())

        if (clicked.get() == "16 mm"):
            totalFeet = totalFrames / 40

        if (clicked.get() == "Regular 8"):
            totalFeet = totalFrames / 79

        if (clicked.get() == "Super 8"):
            totalFeet = totalFrames / 72

        if (clicked.get() == "9.5 approx."):
            totalFeet = totalFrames / 40

        if (clicked.get() == "35 mm"):
            totalFeet = totalFrames / 16

        footageLabelOut.configure(text = totalFeet)
    else:
        errorMessageLabel.configure(text="Please input a number for feet or frames. (input 0 if none)")

    if (clicked.get() == "16 mm"):
        totalFrames = totalFeet * 40

    if (clicked.get() == "Regular 8"):
        totalFrames = totalFeet * 79

    if (clicked.get() == "Super 8"):
        totalFrames = totalFeet * 72

    if (clicked.get() == "9.5 approx."):
        totalFrames = totalFeet * 40

    if (clicked.get() == "35 mm"):
        totalFrames = totalFeet * 16

    totalSeconds = (totalFrames / fps)

    totalHours = int((totalSeconds / 3600))
    secsRemain = int((totalSeconds - (totalHours * 3600)))
    totalMinutes = int((secsRemain / 60))
    secsRemain = int(secsRemain - (totalMinutes * 60))
    totalSecs = int(secsRemain)

    tenLabelOut.configure(text = round((totalFeet * 0.10),2))
    twelveLabelOut.configure(text = round((totalFeet * 0.12),2))
    fifteenLabelOut.configure(text = round((totalFeet * 0.15),2))
    twentyLabelOut.configure(text = round((totalFeet * 0.20),2))
    thirtyLabelOut.configure(text = round((totalFeet * 0.30),2))
    fortyLabelOut.configure(text = round((totalFeet * 0.40),2))
    fifteyLabelOut.configure(text = round((totalFeet * 0.50),2))
    hourLabelOut.configure(text = totalHours)
    minuteLabelOut.configure(text = totalMinutes)
    secLabelOut.configure(text = totalSecs)
    frameLabelOut.configure(text = totalFrames)

def resetAll():
    fpsEntry.delete(0,END)
    hourEntry.delete(0,END)
    minuteEntry.delete(0,END)
    secEntry.delete(0,END)
    footageEntry.delete(0,END)
    frameEntry.delete(0,END)
    hourLabelOut.configure(text = "")
    minuteLabelOut.configure(text = "")
    secLabelOut.configure(text = "")
    footageLabelOut.configure(text = "")
    frameLabelOut.configure(text = "")
    tenLabelOut.configure(text = "")
    twelveLabelOut.configure(text = "")
    fifteenLabelOut.configure(text = "")
    twentyLabelOut.configure(text = "")
    thirtyLabelOut.configure(text = "")
    fortyLabelOut.configure(text = "")
    fifteyLabelOut.configure(text="")

#initializes the frame and sets the size and color
root = Tk()
root.geometry("400x525")
root.configure(bg='#fafd32')

#initializes and places the label in the correct spot
rootTitle = Label(root, text = "AV Geeks Calculator", )
rootTitle.place(relx = 0.5, rely = 0, anchor = CENTER, y = 25)
rootTitle.configure(font = Font_tuple)
rootTitle.configure(bg='#fafd32')

fpsLabel = Label(root, text = "Frames Per Second: ")
fpsLabel.place(x = 10, y = 75)
fpsLabel.configure(bg='#fafd32')


formatLabel = Label(root, text = "Format: ")
formatLabel.place(x = 10, y = 125)
formatLabel.configure(bg='#fafd32')

timeLabel = Label(root, text = "Running Time (h:m:s): ")
timeLabel.place(x = 10, y = 175)
timeLabel.configure(bg='#fafd32')

footageLabel = Label(root, text = "Footage (feet): ")
footageLabel.place(x = 10, y = 225)
footageLabel.configure(bg='#fafd32')

framesLabel = Label(root, text = "Total Number of Frames: ")
framesLabel.place(x = 10, y = 275)
framesLabel.configure(bg='#fafd32')

tenLabel = Label(root, text = "0.10: ")
tenLabel.place(x = 10, y = 325)
tenLabel.configure(bg='#fafd32')

twelveLabel = Label(root, text = "0.12: ")
twelveLabel.place(x = 10, y = 350)
twelveLabel.configure(bg='#fafd32')

fifteenLabel = Label(root, text = "0.15: ")
fifteenLabel.place(x = 10, y = 375)
fifteenLabel.configure(bg='#fafd32')

twentyLabel = Label(root, text = "0.20: ")
twentyLabel.place(x = 10, y = 400)
twentyLabel.configure(bg='#fafd32')

thirtyLabel = Label(root, text = "0.30: ")
thirtyLabel.place(x = 10, y = 425)
thirtyLabel.configure(bg='#fafd32')

fortyLabel = Label(root, text = "0.40: ")
fortyLabel.place(x = 10, y = 450)
fortyLabel.configure(bg='#fafd32')

fifteyLabel = Label(root, text = "0.50: ")
fifteyLabel.place(x = 10, y = 475)
fifteyLabel.configure(bg='#fafd32')

#Creates an input box for the user to input data
v = IntVar()
fpsEntry = Entry(root, width= 5, text = v)
fpsEntry.focus_set()
fpsEntry.place(x = 125, y = 75)
v.set(24)



options = [
    "Regular 8",
    "Super 8",
    "9.5 approx.",
    "16 mm",
    "35 mm"
]
clicked = StringVar()
clicked.set( "16 mm" )
drop = OptionMenu(root, clicked, *options,)
drop.focus_set()
drop.place(x = 75, y = 125)
drop.configure(bg='#c1c2d2')

hourEntry = Entry(root, width= 5)
hourEntry.focus_set()
hourEntry.place(x = 140, y = 175)

minuteEntry = Entry(root, width= 5)
minuteEntry.focus_set()
minuteEntry.place(x = 180, y = 175)

secEntry = Entry(root, width= 5)
secEntry.focus_set()
secEntry.place(x = 220, y = 175)

footageEntry = Entry(root, width= 5)
footageEntry.focus_set()
footageEntry.place(x = 100, y = 225)

footageLabelOut = Label(root)
footageLabelOut.focus_set()
footageLabelOut.place(x = 150, y = 225)
footageLabelOut.configure(bg='#fafd32')

frameEntry = Entry(root, width= 5)
frameEntry.focus_set()
frameEntry.place(x = 150, y = 275)

frameLabelOut = Label(root)
frameLabelOut.focus_set()
frameLabelOut.place(x = 200, y = 275)
frameLabelOut.configure(bg='#fafd32')

tenLabelOut = Label(root)
tenLabelOut.focus_set()
tenLabelOut.place(x = 50, y = 325)
tenLabelOut.configure(bg='#fafd32')

twelveLabelOut = Label(root)
twelveLabelOut.focus_set()
twelveLabelOut.place(x = 50, y = 350)
twelveLabelOut.configure(bg='#fafd32')

fifteenLabelOut = Label(root)
fifteenLabelOut.focus_set()
fifteenLabelOut.place(x = 50, y = 375)
fifteenLabelOut.configure(bg='#fafd32')

twentyLabelOut = Label(root)
twentyLabelOut.focus_set()
twentyLabelOut.place(x = 50, y = 400)
twentyLabelOut.configure(bg='#fafd32')

thirtyLabelOut = Label(root)
thirtyLabelOut.focus_set()
thirtyLabelOut.place(x = 50, y = 425)
thirtyLabelOut.configure(bg='#fafd32')

fortyLabelOut = Label(root)
fortyLabelOut.focus_set()
fortyLabelOut.place(x = 50, y = 450)
fortyLabelOut.configure(bg='#fafd32')

fifteyLabelOut = Label(root)
fifteyLabelOut.focus_set()
fifteyLabelOut.place(x = 50, y = 475)
fifteyLabelOut.configure(bg='#fafd32')

hourLabelOut = Label(root)
hourLabelOut.focus_set()
hourLabelOut.place(x = 140, y = 200)
hourLabelOut.configure(bg='#fafd32')

minuteLabelOut = Label(root)
minuteLabelOut.focus_set()
minuteLabelOut.place(x = 180, y = 200)
minuteLabelOut.configure(bg='#fafd32')

secLabelOut = Label(root)
secLabelOut.focus_set()
secLabelOut.place(x = 220, y = 200)
secLabelOut.configure(bg='#fafd32')

calcFootageButton = Button(text = "Calculate Footage", command = calculateFootage)
calcFootageButton.place(x = 225, y = 370)
calcFootageButton.configure(bg='#c1c2d2')

calcRunTimeButton = Button(text = "Calculate RunTime", command = calculateRunTime)
calcRunTimeButton.place(x = 225, y = 415)
calcRunTimeButton.configure(bg='#c1c2d2')

resetButton = Button(text = "Reset All", command = resetAll)
resetButton.place(x = 335, y = 490)
resetButton.configure(bg='#ed4245')

errorMessageLabel = Label(root)
errorMessageLabel.focus_set()
errorMessageLabel.place(x = 25, y = 500)
errorMessageLabel.configure(bg='#fafd32', fg = "red")

#displays the frame
root.mainloop()