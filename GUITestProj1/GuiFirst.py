import tkinter # load the GUI in python with all widgets
from tkinter import Label, Frame, Button, messagebox

class FirstGUIApp:
    # create main widget window
    def __init__(self):
        self.main_window = tkinter.Tk() # this will allow us to call the main window/interface for the application
            # main_window here will work as an object of the tkinter class
        # to put customized title
        self.main_window.title('First GUI App')

        # to organize the widgets in a frame container
        self.top_frame = tkinter.Frame(self.main_window, width=400, height=600,
                                       background="blue")
        self.bottm_frame = Frame(self.main_window)
        self.midFrame = Frame(self.main_window)
        # fourth frame, checbox frame
        self.checkBoxFrame = Frame(self.main_window)

        # to put some text on the interface, we need to use label
        self.label1 = Label(self.top_frame, text='Enter distance in kilometers',
                            relief='solid', borderwidth=2)
        #self.label2 = Label(self.top_frame, text= '2nd Line Text', relief='solid', borderwidth=2)
        self.label1.pack(side = 'top', ipadx=20, ipady=30, padx=15) # this method will place the widget on our GUI interface, without defining the
        #self.label2.pack(side='left', ipadx=20, ipady = 30)
        self.kilo_Meters = tkinter.Entry(self.label1, width=20)
        self.kilo_Meters.pack(side='right')

        self.topFrameButton = Button(self.top_frame, text='Convert', command=self.topButtonFnc)
        self.topFrameButton.pack(side='left')
        self.quitButton = tkinter.Button(self.top_frame, text='Quit',
                                         command=self.main_window.destroy)
        self.quitButton.pack(side='bottom')

        ## MiD Frame ##
        self.valueDisplayLabel = Label(self.midFrame, text='Converted Results: ')
        self.valueDisplay = tkinter.StringVar()
        # need to create another hidden label which is going to hold the valueDisplay object
        self.hidden_label = Label(self.midFrame, textvariable=self.valueDisplay)
        self.valueDisplayLabel.pack(side='left')
        self.hidden_label.pack(side='left')

        ## RadioButtons Activity
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create radioButton widgets
        self.radioButton1 = tkinter.Radiobutton(self.midFrame, text='Option 1',
                                                variable=self.radio_var, value=1,
                                                command=self.radioButton1Activity)
        self.radioButton2 = tkinter.Radiobutton(self.midFrame, text='Option 2',
                                                variable=self.radio_var, value=2,
                                                command=self.radioButton2Activity)
        self.choiceButton = Button(self.midFrame, text='Selection',
                                   command=self.selectionChoice)
        self.radioButton1.pack()
        self.radioButton2.pack()
        self.choiceButton.pack()

        ## CheckBoxes for third frame
        self.ckBox1_var = tkinter.StringVar()
        self.ckBox2_var = tkinter.StringVar()

        self.ckBox1_var.set(0)
        self.ckBox2_var.set(0)

        # create the checkboxes
        self.checkBox1 = tkinter.Checkbutton(self.checkBoxFrame, text='Check Box 1',
                                             variable=self.ckBox1_var)
        self.checkBox2 = tkinter.Checkbutton(self.checkBoxFrame, text='Check Box 2',
                                             variable=self.ckBox2_var)
        self.ckBxButton = Button(self.checkBoxFrame, text = 'Selection Option',
                                 command=self.selectChoiceCkBx)

        self.checkBox1.pack()
        self.checkBox2.pack()
        self.ckBxButton.pack()

        self.label3 = Label(self.bottm_frame, text='New Bottom Label One', relief='solid', borderwidth=1)
        self.label4 = Label(self.bottm_frame, text='New Bottom Label Two', relief='solid', borderwidth=1)
        self.label3.pack()
        self.label4.pack()
        self.bottomButton = tkinter.Button(self.bottm_frame, text='Bottom Frame Buttn', command=self.bottomButtonFnc)
        self.bottomButton.pack()

        self.top_frame.pack(side='top', expand = False)

        self.midFrame.pack()
        self.checkBoxFrame.pack()
        self.bottm_frame.pack(side='bottom')
        # area, it will put the widgets at default area, which is center


        # to hold window we need the tkinter to run in a loop
        tkinter.mainloop()

    def topButtonFnc(self):
        milestoConvert = float(self.kilo_Meters.get()) # this will allow us to take the input from the
        # text box
        # everytime, this method will return the value in string format. So, we need to convert
        # the value from string to float.
        miles = milestoConvert / 1.61
        #messagebox.showinfo('Converted Miles',
         #                   f'The distance in miles is {miles}')
        self.valueDisplay.set(miles)

    def bottomButtonFnc(self):
        messagebox.showerror('Bottom Button', 'You pressed on lower frame button')

    def selectionChoice(self):
        tkinter.messagebox.showinfo('Selected option ', self.radio_var.get())

    def radioButton1Activity(self):
        num = float(self.kilo_Meters.get())
        tkinter.messagebox.showinfo('Sqaure', f'The square of the given '
                                              f'value {num**2}')

    def radioButton2Activity(self):
        num = float(self.kilo_Meters.get())
        tkinter.messagebox.showinfo('Exponentioal', f'The exponential of the given '
                                          f'value {num ** num}')

    def selectChoiceCkBx(self):
        message = ' '
        # print(self.ckBox1_var.get())
        if int(self.ckBox1_var.get()) == 1:
            message = 'option 1'
        elif int(self.ckBox2_var.get()) ==1:
            message = 'option 2'
        tkinter.messagebox.showinfo('Warning', f'Selected value ' + message)


if __name__ == "__main__":
    window = FirstGUIApp()
