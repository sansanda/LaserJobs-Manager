"""

Creating a  window class GUI for entering the data of a new laser job

David SAnchez Sanchez


"""
import tkinter
from tkinter import *
from tkinter import ttk
from datetime import date

class NewJobWindow():



    def __init__(self, w, h, guiController):

        # pixels of the window
        self.width = w
        self.height = h

        self.guiController = guiController
        self.root = tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.root.title('Laser-Jobs Manager. New Job Window.')
        self.root.iconbitmap('../Gui/icons/laserJobsManager_Icon5.ico')

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth() / 2 - self.width / 2)
        positionDown = int(self.root.winfo_screenheight() / 2 - self.height / 2)

        self.root.geometry(str(self.width) + 'x' + str(self.height) + "+" +str(positionRight) + "+" + str(positionDown))
        self.root.resizable(0, 0)
        self.create_menu_bar()
        self.createLabelsAndEntries()
        self.createOKAndCancelButtons()

    def create_menu_bar(self):

        self.menubar = Menu(self.root)
        self.fileMenu = Menu(self.root, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.close)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.root.config(menu=self.menubar)

    def createLabelsAndEntries(self):

        newJobData_frame = Frame(self.root)
        newJobData_frame.config(height=self.height-25, width=self.width)
        newJobData_frame.grid(row=0, columnspan=12, rowspan=10, padx=5, pady=5, sticky=W + E + N + S)

        Label(newJobData_frame, text='Username:',anchor=W, width=20).grid(row=0, column=0)
        Label(newJobData_frame, text='Date:',anchor=W, width=20).grid(row=1, column=0)
        Label(newJobData_frame, text='Material:',anchor=W, width=20).grid(row=2, column=0)
        Label(newJobData_frame, text='Cut/Raster:',anchor=W, width=20).grid(row=3, column=0)
        Label(newJobData_frame, text='Speed(%):', anchor=W, width=20).grid(row=4, column=0)
        Label(newJobData_frame, text='Power(%):', anchor=W, width=20).grid(row=5, column=0)
        Label(newJobData_frame, text='DPI:', anchor=W, width=20).grid(row=6, column=0)
        Label(newJobData_frame, text='Freq(Hz):', anchor=W, width=20).grid(row=7, column=0)
        Label(newJobData_frame, text='#Passes (Cut/Raster):', anchor=W, width=20).grid(row=8, column=0)
        Label(newJobData_frame, text='RasterDepth(mm):', anchor=W, width=20).grid(row=9, column=0)
        Label(newJobData_frame, text='Others:', anchor=W, width=20).grid(row=10, column=0)

        #Username entry
        self.username = StringVar(newJobData_frame)
        self.username_entry = Entry(newJobData_frame,textvariable=self.username)
        self.username_entry.config(width=15)
        self.username_entry.grid(row=0, column=1, sticky=W)

        #Date entry
        self.date = StringVar(newJobData_frame)
        self.date_entry = Entry(newJobData_frame,textvariable=self.date)
        self.date_entry.config(width=15)
        self.date_entry.insert(0,date.today())
        self.date_entry.config(state='disabled')
        self.date_entry.grid(row=1,column=1,sticky=W)

        #Material Entry
        self.material = StringVar(newJobData_frame)
        self.material_entry = Entry(newJobData_frame, textvariable=self.material)
        self.material_entry.config(width=15)
        self.material_entry.grid(row=2, column=1, sticky=W)

        #Dropdown list for job type
        self.jobType = StringVar(newJobData_frame)
        choices = ('Cut', 'Raster', 'Cut/Raster')
        self.jobType.set(choices[0])  # default value
        JobTypeMenu = OptionMenu(newJobData_frame, self.jobType, *choices)
        JobTypeMenu.config(width=8, anchor=W)
        JobTypeMenu.grid(row=3, column=1, sticky=W)

        # Speed Entry
        self.speed = IntVar(newJobData_frame, 90)
        self.speed_entry = Entry(newJobData_frame, textvariable=self.speed)
        self.speed_entry.config(width=15)
        self.speed_entry.grid(row=4, column=1, sticky=W)

        #Power Entry
        self.power = IntVar(newJobData_frame,90)
        self.power_entry = Entry(newJobData_frame, textvariable=self.power)
        self.power_entry.config(width=15)
        self.power_entry.grid(row=5, column=1, sticky=W)

        #dpi entry (dots per icnh)
        self.dpi = IntVar(newJobData_frame, 900)
        self.dpi_entry = Entry(newJobData_frame, textvariable=self.dpi)
        self.dpi_entry.config(width=15)
        self.dpi_entry.grid(row=6, column=1, sticky=W)

        # Frequency entry (in Hz)
        self.freq = IntVar(newJobData_frame, 5000)
        self.freq_entry = Entry(newJobData_frame, textvariable=self.freq)
        self.freq_entry.config(width=15)
        self.freq_entry.grid(row=7, column=1, sticky=W)

        # Number of passes entry
        self.nPasses = StringVar(newJobData_frame, '1/0')
        self.nPasses_entry = Entry(newJobData_frame, textvariable=self.nPasses)
        self.nPasses_entry.config(width=15)
        self.nPasses_entry.grid(row=8, column=1, sticky=W)

        # Raster depth entry (in mm)
        self.rasterDepth = IntVar(newJobData_frame, 1)
        self.rasterDepth_entry = Entry(newJobData_frame, textvariable=self.rasterDepth)
        self.rasterDepth_entry.config(width=15)
        self.rasterDepth_entry.grid(row=9, column=1, sticky=W)

        # Observations entry
        self.others = StringVar(newJobData_frame, 'Enter here useful comments for the future')
        self.others_entry = Entry(newJobData_frame, textvariable=self.others)
        self.others_entry.bind('<FocusIn>', lambda event: self.others_entry.delete(0, END))
        self.others_entry.config(width=60)
        self.others_entry.grid(row=10, column=1, sticky=W)

    def createOKAndCancelButtons(self):
        okAndCancelButtons_frame = Frame(self.root)
        okAndCancelButtons_frame.config(width= self.width)
        okAndCancelButtons_frame.grid(row=10, column=0, columnspan=2, sticky=W + E + N + S)
        self.okButton = Button(okAndCancelButtons_frame, command=self.newJob, text='Add New Job', width=10)
        self.okButton.grid(row=0, column=0, padx=5, pady=2, sticky=E)
        self.cancelButton = Button(okAndCancelButtons_frame, command= lambda: self.guiController.closeWindow(self), text='Cancel', width=10)
        self.cancelButton.grid(row=0, column=1, padx=5, pady=2, sticky=E)

    def enable(self, enable):
        self.root.attributes('-disabled', not enable)

    def close(self):
        print('Exiting...')
        self.guiController.closeWindow(self)

    def newJob(self):
        print('Adding job...')
        newJobdata = {}
        newJobdata['Username'] = self.username_entry.get()
        newJobdata['Date'] = self.date_entry.get()
        newJobdata['Material'] = self.material_entry.get()
        newJobdata['Cut_Raster'] = self.jobType.get()
        newJobdata['Speed'] = self.speed_entry.get()
        newJobdata['Power'] = self.power_entry.get()
        newJobdata['DPI'] = self.dpi_entry.get()
        newJobdata['Freq'] = self.freq_entry.get()
        newJobdata['Passes'] = self.nPasses_entry.get()
        newJobdata['RasterDepth'] = self.rasterDepth_entry.get()
        newJobdata['Others'] = self.others_entry.get()

        self.guiController.newJob(newJobdata)

    def show(self):
        self.enable(True)
        self.root.mainloop()