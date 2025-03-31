from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import random
import csv
from tktimepicker import SpinTimePickerModern
from tktimepicker import constants

root = Tk() # Main window
time = () # helps with time showing
root.geometry("300x400") # window size
root.resizable(width=False, height=False) # makes window not resizable
root.configure(bg="Orange") # bg colour of window
root.title("Meal Planner") # title of app
global ie # makes var usable all over the project
ie = 0 # used for making new line in Listbox() widget

def recomend(): #recommendation button function
    with open("C:\\Users\\Nihal\\OneDrive\\Documentos\\pyfoods.csv", mode="r", encoding="utf8") as input_file: # uses the csv file as input_file ONLY in the code under it
        csv_reader = csv.reader(input_file) # opens file as csv
        questions = list(csv_reader) # makes the csv into a list
        food = random.choice(questions) # chooses random food from list
        messagebox.showinfo("Recommendation", f"Try {food[0]} for {random.choice(["breakfast", "lunch", "dinner"])}") # shows message box with food & time

def updateTime(time): # used to show time in the label
    global timefood # makes var usable all over the project
    timefood = "{}:{} {}".format(*time) # sets the time in a time format
    timeshow.configure(text = f"Set meal time: {timefood}") # shows the time


def get_time(): # retrives time from the time picker
    top = Toplevel(root) # shows this window on top of the other one
    top.geometry("400x100") # change size of window
    time_picker = SpinTimePickerModern(top) # adds time picker

    time_picker.addAll(constants.HOURS12) # shows time in time picker
    time_picker.configureAll(height=1) # changes height of time picker
    time_picker.configure_separator() # seperates

    time_picker.pack(expand=True, fill="both", pady=2) # adds the time picker to the window
    def updtimemid(): # updates time
        updateTime(time_picker.time()) # runs updateTime() function
        top.destroy() # removes the window
    ok_btn = Button(top, text="OK", command=lambda: updtimemid()) # defines a button that when clicked sets time
    ok_btn.pack(pady=2) # adds button

def planmeal(): # planning meal button function
    global ie # global declaration again to prevent error
    ie += 1 # changes by 1
    foodbox.insert(ie, f"Eat {addmealentry.get()} at {timefood}") # adds food to box
    time_btn.delete(0, END)     # ] - clears both text boxes
    addmealentry.delete(0, END) # ] -|


title = Label(root, text = "Welcome to the meal planner!", background="Orange") # title
addmeallabel = Label(root, text = "Add Meal:", background="Orange") # add meal label
addmealentry = Entry(root, background="Orange") # text box
timelabel = Label(root, text = "Time of day you will eat this:", background="Orange") #time of day eat label
time_btn = Button(root, text="Set Time", command=get_time)# opens window to set time
timeshow = Label(root, background="Orange")# shows time
planmealbtn = Button(root, text="Plan Meal", command=lambda: planmeal()) # adds meal to listbox
reccomend = Button(root, text="Get recommendation", command=lambda: recomend()) # gets a reccomendation
plannedmealslabel = Label(root, text = "Planned meals for today:", background="Orange") # planned meals label
foodbox = Listbox(root, width=45) # list of plnned meals

title.pack(pady=5) # lines 66-75: adds to window
addmeallabel.pack(pady=2)
addmealentry.pack(pady=2)
timelabel.pack(pady=2)
time_btn.pack(pady=2)
timeshow.pack(pady=2)
planmealbtn.pack(pady=2)
reccomend.pack(pady=2)
plannedmealslabel.pack(pady=2)
foodbox.pack(pady=2)

root.mainloop() # refresh the screen