from tkinter import *
from tkinter import messagebox
import math

#function to calculate total price
def calculateRunTime():
    global hourEntry
    global minuteEntry
    global secEntry
    global frameEntry
    global fpsEntry
    global clicked

    hours = int(hourEntry.get())
    minutes = int(minuteEntry.get())
    secs = int(secEntry.get())

    totalSeconds = (hours * 3600) + (minutes * 60) + secs
    fps = int(fpsEntry.get())
    totalFrames = (fps * totalSeconds)

    if (clicked.get() == "16 mm"):
        totalFeet = totalFrames / 39

    if (clicked.get() == "Regular 8"):
        totalFeet = totalFrames / 79

    if (clicked.get() == "Super 8"):
        totalFeet = totalFrames / 71

    if (clicked.get() == "9.5 approx."):
        totalFeet = totalFrames / 40

    if (clicked.get() == "35 mm"):
        totalFeet = totalFrames / 16

    tenLabelOut.configure(text = (totalFeet * 0.10))
    twelveLabelOut.configure(text = (totalFeet * 0.12))
    fifteenLabelOut.configure(text = (totalFeet * 0.15))
    twentyLabelOut.configure(text = (totalFeet * 0.20))
    thirtyLabelOut.configure(text = (totalFeet * 0.30))
    fortyLabelOut.configure(text = (totalFeet * 0.40))
    fifteyLabelOut.configure(text = (totalFeet * 0.50))
    footageLabelOut.configure(text = totalFeet)
    frameLabelOut.configure(text = totalFrames)


    print(totalFeet)
    print(totalFrames)

#initializes the frame and sets the size
root = Tk()
root.geometry("400x525")

#initializes and places the label in the correct spot
rootTitle = Label(root, text = "AV Geeks Calculator")
rootTitle.place(relx = 0.5, rely = 0, anchor = CENTER, y = 25)

fpsLabel = Label(root, text = "Frames Per Second: ")
fpsLabel.place(x = 10, y = 75)

formatLabel = Label(root, text = "Format: ")
formatLabel.place(x = 10, y = 125)

timeLabel = Label(root, text = "Running Time (h:m:s): ")
timeLabel.place(x = 10, y = 175)

footageLabel = Label(root, text = "Footage (feet): ")
footageLabel.place(x = 10, y = 225)

framesLabel = Label(root, text = "Total Number of Frames: ")
framesLabel.place(x = 10, y = 275)

tenLabel = Label(root, text = "0.10: ")
tenLabel.place(x = 10, y = 325)

twelveLabel = Label(root, text = "0.12: ")
twelveLabel.place(x = 10, y = 350)

fifteenLabel = Label(root, text = "0.15: ")
fifteenLabel.place(x = 10, y = 375)

twentyLabel = Label(root, text = "0.20: ")
twentyLabel.place(x = 10, y = 400)

thirtyLabel = Label(root, text = "0.30: ")
thirtyLabel.place(x = 10, y = 425)

fortyLabel = Label(root, text = "0.40: ")
fortyLabel.place(x = 10, y = 450)

fifteyLabel = Label(root, text = "0.50: ")
fifteyLabel.place(x = 10, y = 475)

#Creates an input box for the user to input data
fpsEntry = Entry(root, width= 5)
fpsEntry.focus_set()
fpsEntry.place(x = 125, y = 75)

options = [
    "Regular 8",
    "Super 8",
    "9.5 approx.",
    "16 mm",
    "35 mm"
]
clicked = StringVar()
clicked.set( "16 mm" )
drop = OptionMenu(root, clicked, *options)
drop.focus_set()
drop.place(x = 75, y = 125)

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

frameEntry = Entry(root, width= 5)
frameEntry.focus_set()
frameEntry.place(x = 150, y = 275)

frameLabelOut = Label(root)
frameLabelOut.focus_set()
frameLabelOut.place(x = 200, y = 275)

tenLabelOut = Label(root)
tenLabelOut.focus_set()
tenLabelOut.place(x = 50, y = 325)

twelveLabelOut = Label(root)
twelveLabelOut.focus_set()
twelveLabelOut.place(x = 50, y = 350)

fifteenLabelOut = Label(root)
fifteenLabelOut.focus_set()
fifteenLabelOut.place(x = 50, y = 375)

twentyLabelOut = Label(root)
twentyLabelOut.focus_set()
twentyLabelOut.place(x = 50, y = 400)

thirtyLabelOut = Label(root)
thirtyLabelOut.focus_set()
thirtyLabelOut.place(x = 50, y = 425)

fortyLabelOut = Label(root)
fortyLabelOut.focus_set()
fortyLabelOut.place(x = 50, y = 450)

fifteyLabelOut = Label(root)
fifteyLabelOut.focus_set()
fifteyLabelOut.place(x = 50, y = 475)

calcRunTimeButton = Button(text = "Calculate", command = calculateRunTime)
calcRunTimeButton.place(x = 225, y = 370)

#calcFootageButton = Button(text = "Calculate Footage", command = calculateFootage)
#calcFootageButton.place(x = 225, y = 420)

#displays the frame
root.mainloop()