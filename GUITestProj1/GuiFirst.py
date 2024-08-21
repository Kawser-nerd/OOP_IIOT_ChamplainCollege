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
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottm_frame = Frame(self.main_window)

        # to put some text on the interface, we need to use label
        self.label1 = Label(self.top_frame, text='This is a programming class', relief='solid', borderwidth=2)
        self.label2 = Label(self.top_frame, text= '2nd Line Text', relief='solid', borderwidth=2)
        self.label1.pack(side = 'left', ipadx=20, ipady=30, padx=15) # this method will place the widget on our GUI interface, without defining the
        self.label2.pack(side='left', ipadx=20, ipady = 30)
        self.topFrameButton = Button(self.top_frame, text='Top Frame Button', command=self.topButtonFnc)
        self.topFrameButton.pack(side='right')

        self.label3 = Label(self.bottm_frame, text='New Bottom Label One', relief='solid', borderwidth=1)
        self.label4 = Label(self.bottm_frame, text='New Bottom Label Two', relief='solid', borderwidth=1)
        self.label3.pack()
        self.label4.pack()
        self.bottomButton = tkinter.Button(self.bottm_frame, text='Bottom Frame Buttn', command=self.bottomButtonFnc)
        self.bottomButton.pack()
        self.top_frame.pack(side='top')
        self.bottm_frame.pack(side='bottom')
        # area, it will put the widgets at default area, which is center


        # to hold window we need the tkinter to run in a loop
        tkinter.mainloop()

    def topButtonFnc(self):
        messagebox.showinfo('Response Message', 'Thanks for clicking on the topFrame Button')

    def bottomButtonFnc(self):
        messagebox.showerror('Bottom Button', 'You pressed on lower frame button')


if __name__ == "__main__":
    window = FirstGUIApp()
