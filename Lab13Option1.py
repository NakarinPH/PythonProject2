# Nakarin Philangam
# 11/19/2021
# This program creates the GUI of the Cash Register
# that calculate the total with or without 20% discount
import tkinter


class CashRegisterGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # add a title for the GUI
        self.main_window.title('Cash Register')

        # Set the size of the main window
        self.main_window.geometry('250x150')

        # Create 6 frames to group widgets
        self.hardbacks_frame = tkinter.Frame()
        self.paperbacks_frame = tkinter.Frame()
        self.magazines_frame = tkinter.Frame()
        self.discount_frame = tkinter.Frame()
        self.total_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        # Create the widgets for the hardbacks_frame
        self.hardbacks_label = tkinter.Label(self.hardbacks_frame,
                                             text='Hardbacks:')
        self.hardbacks_entry = tkinter.Entry(self.hardbacks_frame,
                                             width=10)

        # Pack the hardbacks_frame's widgets
        self.hardbacks_label.pack(side='left')
        self.hardbacks_entry.pack(side='left')

        # Create the widgets for the paperbacks_frame
        self.paperbacks_label = tkinter.Label(self.paperbacks_frame,
                                              text='Paperbacks:')
        self.paperbacks_entry = tkinter.Entry(self.paperbacks_frame,
                                              width=10)

        # Pack the widgets for the paperbacks_frame
        self.paperbacks_label.pack(side='left')
        self.paperbacks_entry.pack(side='left')

        # Create the widgets for the magazines_frame
        self.magazines_label = tkinter.Label(self.magazines_frame,
                                             text='Magazine:')
        self.magazines_entry = tkinter.Entry(self.magazines_frame,
                                            width=10)

        # Pack the widgets for the magazines_frame
        self.magazines_label.pack(side='left')
        self.magazines_entry.pack(side='left')

        # Create the widget for the total_frame
        self.total_label = tkinter.Label(self.total_frame,
                                         text='Total: $')

        # Use the object's set method to store a string of blank characters
        self.total_value = tkinter.StringVar()

        # Create a label and associate it with the String object.
        self.total_value_label = tkinter.Label(self.total_frame,
                                               textvariable=self.total_value)

        # Pack the widgets for sale_tax_frame
        self.total_label.pack(side='left')
        self.total_value_label.pack(side='left')

        # Create the IntVar objects to use with the Checkbutton
        self.cb_var1 = tkinter.IntVar()

        # Set the intVar object to 0
        self.cb_var1.set(0)

        # Create the checkbutton widgets in the discount_frame
        self.cb1 = tkinter.Checkbutton(self.discount_frame,
                                       text='20% Discount',
                                       variable=self.cb_var1)

        # Pack the checkbutton
        self.cb1.pack()

        # Create the widgets for button_frame
        self.calculate_button = tkinter.Button(self.button_frame,
                                               text='Calculate',
                                               command=self.calculate)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the buttons.
        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.hardbacks_frame.pack()
        self.paperbacks_frame.pack()
        self.magazines_frame.pack()
        self.discount_frame.pack()
        self.total_frame.pack()
        self.button_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    def calculate(self):
        # Get the value entered by the user into the hardbacks_entry
        hardbacks = int(self.hardbacks_entry.get())
        hardbacks_total = round(hardbacks * 7, 2)

        # Get the value entered by the user into the paperbacks_entry
        paperbacks = int(self.paperbacks_entry.get())
        paperbacks_total = round(paperbacks * 2.50, 2)

        # Get the value entered by the user into the magazines_entry
        magazines = int(self.magazines_entry.get())
        magazines_total = round(magazines * 3.95, 2)

        # Calculate the total without discount
        total_without_discount = round(hardbacks_total + paperbacks_total + magazines_total, 2)

        # Calculate the discount
        discount = round(total_without_discount * 0.2, 2)

        # Determine if the user selects the discount checkbox
        if self.cb_var1.get() == 1:

            total = round((hardbacks_total + paperbacks_total + magazines_total) - discount, 2)
            self.total_value.set(total)

        else:

            self.total_value.set(total_without_discount)


# Create an instance of the TaxCalculatorGUI class
cash_register = CashRegisterGUI()
