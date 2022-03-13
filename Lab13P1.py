# Nakarin Philangam
# 11/17/2021
# This lab create a GUI that takes the total purchase and tax rate from the user
# then it calculates the sales tax and the amount due
import tkinter


class TaxCalculatorGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # add a title for the GUI
        self.main_window.title('Tax Calculator')

        # Set the size of the main window
        self.main_window.geometry('250x125')

        # Create 5 frames to group widgets
        self.total_purchase_frame = tkinter.Frame()
        self.tax_rate_frame = tkinter.Frame()
        self.sales_tax_frame = tkinter.Frame()
        self.amount_due_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        # Create the widgets for the total_purchase_frame
        self.total_purchase_label = tkinter.Label(self.total_purchase_frame,
                                                  text='Total Purchase: ')
        self.total_purchase_entry = tkinter.Entry(self.total_purchase_frame,
                                                  width=10)

        # Pack the total_purchase_frame's widgets
        self.total_purchase_label.pack(side='left')
        self.total_purchase_entry.pack(side='left')

        # Create the widgets for the tax_rate_frame
        self.tax_rate_label = tkinter.Label(self.tax_rate_frame,
                                            text='Tax Rate: ')
        self.tax_rate_entry = tkinter.Entry(self.tax_rate_frame,
                                            width=10)

        # Pack the widgets for the tax_rate_frame
        self.tax_rate_label.pack(side='left')
        self.tax_rate_entry.pack(side='left')

        # Create the widgets for the sale_tax_frame
        self.sale_tax_label = tkinter.Label(self.sales_tax_frame,
                                            text='Sale Tax: $')

        # Use the object's set method to store a string of blank characters
        self.sale_tax_value = tkinter.StringVar()

        # Create a label and associate it with the String object.
        self.sale_tax_value_label = tkinter.Label(self.sales_tax_frame,
                                                  textvariable=self.sale_tax_value)

        # Pack the widgets for sale_tax_frame
        self.sale_tax_label.pack(side='left')
        self.sale_tax_value_label.pack(side='left')
        self.sale_tax_value_label.pack(side='left')

        # Create the widgets for amount_due_frame
        self.amount_due_label = tkinter.Label(self.amount_due_frame,
                                              text='Amount Due: $')

        # Use the object's set method to store a string of blank characters
        self.amount_due_value = tkinter.StringVar()

        # Create a label and associate it with the String object.
        self.amount_due_value_label = tkinter.Label(self.amount_due_frame,
                                                    textvariable=self.amount_due_value)

        # Pack the widgets for amount_due_frame
        self.amount_due_label.pack(side='left')
        self.amount_due_value_label.pack(side='left')
        self.amount_due_value_label.pack(side='left')

        # create the widgets for button_frame
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
        self.total_purchase_frame.pack()
        self.tax_rate_frame.pack()
        self.sales_tax_frame.pack()
        self.amount_due_frame.pack()
        self.button_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    def calculate(self):
        # Get the value entered by the user into the total_purchase_entry
        total_purchase = float(self.total_purchase_entry.get())

        # Get the value entered by the user into the tax_rate_entry
        tax_rate = int(self.tax_rate_entry.get())

        # Calculate the sale tax
        sale_tax = round((tax_rate / 100) * total_purchase, 2)

        # Calculate the amount due
        amount_due = round(total_purchase + sale_tax, 2)

        # Convert sale_tax to a string and store it in the StringVar object.
        self.sale_tax_value.set(sale_tax)

        # Convert amount_due to a string and store it in the StringVar object.
        self.amount_due_value.set(amount_due)


# Create an instance of the TaxCalculatorGUI class
tax_calculator = TaxCalculatorGUI()
