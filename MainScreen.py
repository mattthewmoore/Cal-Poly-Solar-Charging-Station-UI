from tkinter import*
import Charging

class Locker():
    def __init__(self, number, occupied
                 , temp_pass, master_pass ):
        self.number = number
        self.password = ""
        self.occupied = occupied
        self.tempPass = temp_pass
        self.masterPass = master_pass
        self.start_time = 0
        self.current_list = []
# locker class to create a locker object

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()
# Function to clear window


def main_screen():
    clear_frame()

    message = Label(root,  background='#22CC00',
                    font=('Consolas', 49), text="Solar Charging Station",
                    bd=10, )
    message.grid(row=0, column=0)
    message.configure(foreground='#4D4A4F')
    # Top border

    unlock_button = Button(root, background='#4D4A4F'
                           , border=0, command=unlock_selection
                           , image=unlock_image
                           ,activebackground='#4D4A4F')
    unlock_button.place(x=245, y=150)

    charge_button = Button(root, background='#4D4A4F'
                            , border=0, command=locker_selection
                            , image=charge_image
                            , activebackground='#4D4A4F')
    charge_button.place(x=225,y=190)
    # Charge and Unlock buttons

def locker_selection():
    clear_frame()

    def locker_filled():
            message = Label(root, font=('Consolas', 18)
                            , background='#4D4A4F'
                            , foreground='red'
                            , text="Locker Filled Choose Another"
                            , bd=0)
            message.place(x=225, y=135)
    # Message for filled locker

    def locker_one():
        if locker1.occupied == False:
            enter_password(locker1)
        else:
            locker_filled()

    def locker_two():
        if locker2.occupied == False:
            enter_password(locker2)
        else:
            locker_filled()

    def locker_three():
        if locker3.occupied == False:
            enter_password(locker3)
        else:
            locker_filled()

    def locker_four():
        if locker4.occupied == False:
            enter_password(locker4)
            # Proceed to next page if empty
        else:
            locker_filled()
            # Display message if filled

    top = Label(root, background='#22CC00',
                    font=('Consolas', 49)
                    , text="Solar Charging Station", bd=10)
    top.configure(foreground='#4D4A4F')
    top.grid(column=0, row=0)
    # Top banner solar charging station

    message = Label(root, font=('Consolas', 20)
                    , background='#4D4A4F'
                    , foreground='#22CC00'
                    , text="Choose a locker", bd=0)
    message.place(x=285, y=135)
    # Ask to choose a locker

    back_button = Button(root, background='#4D4A4F'
                           , command=main_screen
                           , border=0, image=back_image
                           , activebackground='#4D4A4F')
    back_button.place(x=80,y=125)
    # Back button to main screen

    btn1 = Button(root, background = '#4D4A4F'
                    , command=locker_one
                    , border=0, image=num1_image
                    , activebackground='#4D4A4F' )
    btn1.place(x=260, y=185)

    btn2 = Button(root, background='#4D4A4F'
                  , command=locker_two
                  , border=0, image=num2_image
                  , activebackground='#4D4A4F')
    btn2.place(x=403, y=186)

    btn3 = Button(root, background='#4D4A4F'
                  , command=locker_three
                  , border=0, image=num3_image
                  , activebackground='#4D4A4F')
    btn3.place(x=260, y=325)

    btn4 = Button(root, background='#4D4A4F'
                  , command=locker_four
                  , border=0, image=num4_image
                  , activebackground='#4D4A4F')
    btn4.place(x=405,y=325)
    # Buttons in square formation
# Select out of lockers 1-4

def enter_password(locker):
    clear_frame()

    def Btn1():
        updateInput(1)
    def Btn2():
        updateInput(2)
    def Btn3():
        updateInput(3)
    def Btn4():
        updateInput(4)
    def Btn5():
        updateInput(5)
    def Btn6():
        updateInput(6)
    def Btn7():
        updateInput(7)
    def Btn8():
        updateInput(8)
    def Btn9():
        updateInput(9)
    def Btn0():
        updateInput(0)
    # Functions to send correct number to
    # updateInput based upon the button pressed

    def enter_btn():
        if len(locker.tempPass) == 4:
            confirmation_screen(locker)
    # Next screen if enter pressed and tempPass is 4 digits

    def back_btn():
        locker.tempPass = ""
        locker_selection()
    # Reset pass word and return to last screen

    def updateInput(number):
        if len(locker.tempPass) < 4:
            locker.tempPass = locker.tempPass + str(number)
            """ Password while typing held in tempPass here
                it is adding the new user input to tempPass """

            inputframe = Label(root, background='white'
                               , font=('Lato', 25)
                               , text=locker.tempPass, padx=0)
            inputframe.place(x=377, y=164)
            # Update the input on frame
        if len(locker.tempPass) == 4:
            enter = Button(root, command=enter_btn
                           , bg='#22CC00'
                           , text="Enter", bd=2
                           , width=8, height=3)
            enter.place(x=451, y=390)
            # Change enter btn background to green when 4 digits
    # Update the number on the display

    def deleteInput():
        length = len(locker.tempPass)
        temp = locker.tempPass[0:length-1]
        locker.tempPass = temp
        # Removes number from object

        whiteframe = Label(root, background='white',padx=63
                           , height=2)
        whiteframe.place(x=377,y=169)
        # Frame to block out old number

        inputframe = Label(root, background='white'
                           , font=('Lato', 25)
                           , text=locker.tempPass, padx=0)
        inputframe.place(x=377, y=164)
        # Put the updated input on the display

        enter = Button(root, command=enter_btn
                       , bg='white'
                       , text="Enter", bd=2
                       , width=8, height=3)
        enter.place(x=451, y=390)
    # Delete on display

    top = Label(root, background='#22CC00',
                    font=('Consolas', 49)
                    , text="Solar Charging Station", bd=10)
    top.configure(foreground='#4D4A4F')
    top.grid(column=0, row=0)
    # Top banner

    message = Label(root, font=('Consolas', 20)
                    , background='#4D4A4F'
                    , foreground='#22CC00'
                    , text="Enter a 4-Digit Pin", bd=0)
    message.place(x=285, y=120)
    # Initial message to enter a 4 digit pin

    back = Button(root, background='#4D4A4F'
                      , command=back_btn
                      , border=0, image=back_image
                      , activebackground='#4D4A4F')
    back.place(x=80, y=125)
    # Back button to locker selection

    inputframe = Label(root, background='white'
                       , font=('Lato', 25),  padx=98)
    inputframe.place(x=315, y=164)
    # Blank white input frame

    btn1 = Button(root, command=Btn1, text="1"
                  , bd=2, width=8, height=3)
    btn1.place(x=315,y=216)

    btn2 = Button(root, command=Btn2, text="2"
                  , bd=2, width=8, height=3)
    btn2.place(x=383,y=216)

    btn3 = Button(root, command=Btn3, text="3", bd=2
                  , width=8, height=3)
    btn3.place(x=451, y=216)
    # First Row

    btn4 = Button(root, command=Btn4, text="4", bd=2
                  , width=8, height=3)
    btn4.place(x=315, y=274)

    btn5 = Button(root, command=Btn5, text="5", bd=2
                  , width=8, height=3)
    btn5.place(x=383, y=274)

    btn6 = Button(root, command=Btn6, text="6", bd=2
                  , width=8, height=3)
    btn6.place(x=451, y=274)
    # Second row

    btn7 = Button(root, command=Btn7, text="7", bd=2
                  , width=8, height=3)
    btn7.place(x=315, y=332)

    btn8 = Button(root, command=Btn8, text="8", bd=2
                  , width=8, height=3)
    btn8.place(x=383, y=332)

    btn9 = Button(root, command=Btn9, text="9", bd=2
                  , width=8, height=3)
    btn9.place(x=451, y=332)
    # Third row

    delete = Button(root, command=deleteInput
                    ,text="Delete", bd=2
                    ,activebackground='red'
                    , width=8, height=3)
    delete.place(x=315, y=390)

    btn0 = Button(root, command=Btn0, text="0", bd=2
                  , width=8, height=3)
    btn0.place(x=383, y=390)

    enter = Button(root, command=enter_btn
                   , text="Enter", bd=2
                   , width=8, height=3)
    enter.place(x=451, y=390)
    # Fourth and final row
# Keypad to enter password

def confirmation_screen(locker):
    clear_frame()

    def cancel():
        locker.tempPass = ""
        main_screen()
    # Reset temp pass and return to beginning

    def confirm():
        locker.password = locker.tempPass
        # Set password to input
        locker.occupied = True
        # Object holds that locker is in use
        Charging.begin_charging(locker)
        # Charging started in Charging file
        charging_screen(locker.number)
        # Proceed to next screen

    # Confirm button pressed

    def back_btn():
        enter_password(locker.number)
        locker.tempPass = ""
    # Back button pressed

    top = Label(root, background='#22CC00',
                font=('Consolas', 49)
                , text="Solar Charging Station", bd=10)
    top.configure(foreground='#4D4A4F')
    top.grid(column=0, row=0)
    # Top banner

    message = Label(root, background='#4D4A4F'
                    , font=('Lato', 25)
                    , text="Password: " + locker.tempPass
                    +"\nLocker Number: " + str(locker.number)
                    , padx=0, foreground="#22CC00")
    message.place(x=300,y=150)
    # Display password and locker number for confirmation

    back = Button(root, background='#4D4A4F'
                  , command=back_btn
                  , border=0, image=back_image
                  , activebackground='#4D4A4F')
    back.place(x=80, y=125)
    # Back button to password entry

    confirm = Button(root, background='#4D4A4F'
                     , command=confirm
                     , border=0, image=confirm_image
                     , text='confirm'
                     , activebackground='#4D4A4F')
    confirm.place(x=305,y=250)
    # Confirm button

    cancel_btn = Button(root, command=cancel
                  , background='#4D4A4F'
                  , border=0, image=cancel_image
                  , text='cancel'
                  , activebackground='#4D4A4F')
    cancel_btn.place(x=435, y=250)
    # Cancel button
# Choose to confirm charging and password or exit

def charging_screen(locker_num):
    clear_frame()

    top = Label(root, background='#22CC00'
                , font=('Consolas', 49)
                , text="Solar Charging Station", bd=10)
    top.configure(foreground='#4D4A4F')
    top.grid(column=0, row=0)
    # Top banner

    return_btn = Button(root, background='white'
                        , command=main_screen
                        , text='Return')
    return_btn.place(x=300,y=250)
    # Button to return to start
# Screen to display charging info

def unlock_selection():
    clear_frame()

    def locker_unfilled():
        message = Label(root, font=('Consolas', 20)
                        , background='#4D4A4F'
                        , foreground='#22CC00'
                        , text="Locker Empty", bd=0
                        ,padx=100)
        message.place(x=210, y=135)
    # Message for unfilled locker

    def locker_one():
        if locker1.occupied == True:
            check_password(locker1)
        else:
            locker_unfilled()

    def locker_two():
        if locker2.occupied == True:
            check_password(locker2)
        else:
            locker_unfilled()

    def locker_three():
        if locker3.occupied == True:
            check_password(locker3)
        else:
            locker_unfilled()

    def locker_four():
        if locker4.occupied == True:
            check_password(locker4)
        else:
            locker_unfilled()
    # Checks if lockers are occupied proceeds to next
    # if filled and displays unfilled message otherwise

    top = Label(root, background='#22CC00',
                font=('Consolas', 49)
                , text="Solar Charging Station", bd=10)
    top.configure(foreground='#4D4A4F')
    top.grid(column=0, row=0)
    # Top banner solar charging station

    message = Label(root, font=('Consolas', 20)
                    , background='#4D4A4F'
                    , foreground='#22CC00'
                    , text="Choose a Locker to Unlock", bd=0)
    message.place(x=210, y=135)
    # Ask to choose a locker

    back_button = Button(root, background='#4D4A4F'
                         , command=main_screen
                         , border=0, image=back_image
                         , activebackground='#4D4A4F')
    back_button.place(x=80, y=125)
    # Back button to main screen

    btn1 = Button(root, background='#4D4A4F'
                  , command=locker_one
                  , border=0, image=num1_image
                  , activebackground='#4D4A4F')
    btn1.place(x=260, y=185)

    btn2 = Button(root, background='#4D4A4F'
                  , command=locker_two
                  , border=0, image=num2_image
                  , activebackground='#4D4A4F')
    btn2.place(x=403, y=186)

    btn3 = Button(root, background='#4D4A4F'
                  , command=locker_three
                  , border=0, image=num3_image
                  , activebackground='#4D4A4F')
    btn3.place(x=260, y=325)

    btn4 = Button(root, background='#4D4A4F'
                  , command=locker_four
                  , border=0, image=num4_image
                  , activebackground='#4D4A4F')
    btn4.place(x=405, y=325)
    # Buttons for lockers in square formation
# Select locker to unlock

def check_password(locker):
    clear_frame()


    locker.tempPass = ""
    # Reset temporary password

    def Btn1():
        updateInput(1)
    def Btn2():
        updateInput(2)
    def Btn3():
        updateInput(3)
    def Btn4():
        updateInput(4)
    def Btn5():
        updateInput(5)
    def Btn6():
        updateInput(6)
    def Btn7():
        updateInput(7)
    def Btn8():
        updateInput(8)
    def Btn9():
        updateInput(9)
    def Btn0():
        updateInput(0)
    # Functions to send correct number to
    # updateInput based upon the button pressed

    def enter_btn():
        if len(locker.tempPass) == 4:
            if locker.tempPass == locker.password or locker.tempPass == locker.masterPass:
                locker.occupied = False
                Charging.stop_charging(locker)
                locker_unlocked(locker)
            else:
                incorrect = Label(root, font=('Consolas', 20)
                                  , background='#4D4A4F'
                                  , foreground='Red', padx=60
                                  , text="Incorrect Pin", bd=0)
                incorrect.place(x=255, y=120)
    # Checks length then checks password

    def back_btn():
        locker.tempPass = ""
        unlock_selection()
    # Resets input stored and returns to last screen

    def updateInput(number):
        if len(locker.tempPass) < 4:
            locker.tempPass = locker.tempPass + str(number)
            # Password while typing held in tempPass here
            # adding new input to tempPass
            inputframe = Label(root, background='white'
                               , font=('Lato', 25)
                               , text=locker.tempPass, padx=0)
            inputframe.place(x=377, y=164)

            if len(locker.tempPass) == 4:
                enter = Button(root, command=enter_btn
                               , bg='#22CC00'
                               , text="Enter", bd=2
                               , width=8, height=3)
                enter.place(x=451, y=390)

        # When length of password reaches 4
    # Function to update the number on the display

    def deleteInput():
        length = len(locker.tempPass)
        temp = locker.tempPass[0:length - 1]
        locker.tempPass = temp
        # Removes number from object

        whiteframe = Label(root, background='white', padx=63
                           , height=2)
        whiteframe.place(x=377, y=169)
        # Frame to block out old number

        inputframe = Label(root, background='white'
                           , font=('Lato', 25)
                           , text=locker.tempPass, padx=0)
        inputframe.place(x=377, y=164)
        # Put the updated input on the display

        enter = Button(root, command=enter_btn
                       , bg='white'
                       , text="Enter", bd=2
                       , width=8, height=3)
        enter.place(x=451, y=390)
    # Function to delete on display

    top = Label(root, background='#22CC00',
                font=('Consolas', 49)
                , text="Solar Charging Station", bd=10)
    top.configure(foreground='#4D4A4F')
    top.grid(column=0, row=0)
    # Top banner

    message = Label(root, font=('Consolas', 20)
                    , background='#4D4A4F'
                    , foreground='#22CC00'
                    , text="Enter 4-Digit Pin", bd=0)
    message.place(x=285, y=120)
    # Initial message asking for pin

    back = Button(root, background='#4D4A4F'
                  , command=back_btn
                  , border=0, image=back_image
                  , activebackground='#4D4A4F')
    back.place(x=80, y=125)
    # Back button to locker selection

    inputframe = Label(root, background='white'
                       , font=('Lato', 25), padx=98)
    inputframe.place(x=315, y=164)
    # White input frame


    btn1 = Button(root, command=Btn1, text="1"
                  , bd=2, width=8, height=3)
    btn1.place(x=315, y=216)

    btn2 = Button(root, command=Btn2, text="2"
                  , bd=2, width=8, height=3)
    btn2.place(x=383, y=216)

    btn3 = Button(root, command=Btn3, text="3", bd=2
                  , width=8, height=3)
    btn3.place(x=451, y=216)
    # First row keypad


    btn4 = Button(root, command=Btn4, text="4", bd=2
                  , width=8, height=3)
    btn4.place(x=315, y=274)

    btn5 = Button(root, command=Btn5, text="5", bd=2
                  , width=8, height=3)
    btn5.place(x=383, y=274)

    btn6 = Button(root, command=Btn6, text="6", bd=2
                  , width=8, height=3)
    btn6.place(x=451, y=274)
    # Second row keypad


    btn7 = Button(root, command=Btn7, text="7", bd=2
                  , width=8, height=3)
    btn7.place(x=315, y=332)

    btn8 = Button(root, command=Btn8, text="8", bd=2
                  , width=8, height=3)
    btn8.place(x=383, y=332)

    btn9 = Button(root, command=Btn9, text="9", bd=2
                  , width=8, height=3)
    btn9.place(x=451, y=332)
    # Third row keypad


    delete = Button(root, command=deleteInput
                    , text="Delete", bd=2
                    , activebackground='red'
                    , width=8, height=3)
    delete.place(x=315, y=390)

    btn0 = Button(root, command=Btn0, text="0", bd=2
                  , width=8, height=3)
    btn0.place(x=383, y=390)

    enter = Button(root, command=enter_btn
                   , text="Enter", bd=2
                   , width=8, height=3)
    enter.place(x=451, y=390)
    # Fourth and final row of keypad
# Enter and check locker password

def locker_unlocked(locker):
    clear_frame()

    elapsed_sec = Charging.get_charge_time(locker)
    elapsed_min = 0
    elapsed_hour = 0
    if elapsed_sec > 3599:
        elapsed_hour = int(elapsed_sec / 3600)
        elapsed_sec = elapsed_sec - (3600 * elapsed_hour)
    if elapsed_sec > 59:
        elapsed_min = int(elapsed_sec / 60)
        elapsed_sec = elapsed_sec - (60 * elapsed_min)
    elapsed_hms = [elapsed_hour, elapsed_min, elapsed_sec]
    # Turning elapsed time in secs into hours mins secs
    def exit_btn():
        main_screen()

    top = Label(root, background='#22CC00',
                font=('Consolas', 49)
                , text="Solar Charging Station", bd=10)
    top.configure(foreground='#4D4A4F')
    top.grid(column=0, row=0)
    # Top banner

    message = Label(root, font=('Consolas', 20)
                    , background='#4D4A4F'
                    , foreground='#22CC00'
                    , text="Locker " + str(locker.number) + " Unlocked", bd=0)
    message.place(x=275, y=120)
    # Unlock Message

    charge_time = Label(root, font=('Consolas', 20)
                    , background='#4D4A4F'
                    , foreground='#22CC00'
                    , text="Charge time: " + str(elapsed_hms[0])
                        + ":" + str(elapsed_hms[1]) + ":"
                        + str(elapsed_hms[2])
                    , bd=0)
    charge_time.place(x=265, y=165)
    # Display charge time

    exit = Button(root, background='#4D4A4F'
                  , command=exit_btn
                  , border=0, image=exit_image
                  , activebackground='#4D4A4F')
    exit.place(x=300, y=200)
# Screen after locker is unlocked


locker1 = Locker(1, False, "", "1387")
locker2 = Locker(2, False, "", "8465")
locker3 = Locker(3, False, "", "4375")
locker4 = Locker(4, False, "", "8102")
# Creating locker objects for all lockers
# so that locker info is stored globally

root = Tk()
root.geometry("800x480")
root.configure(background='#4D4A4F')
# Configure window

battery = PhotoImage(file = r'C:\Users\mm7x7\Downloads\Ui_photos\battery_btn.png')
charge_image = battery.subsample(1, 1)

unlock_png = PhotoImage(file = r'C:\Users\mm7x7\Downloads\Ui_photos\unlock_btn.png')
unlock_image = unlock_png.subsample(2,2)

back_png = PhotoImage(file = r'C:\Users\mm7x7\Downloads\Ui_photos\back_btn.png')
back_image = back_png.subsample(6, 6)

num1_png = PhotoImage(file = r'C:\Users\mm7x7\Downloads\Ui_photos\num1.png')
num1_image = num1_png.subsample(1, 1)

num2_png = PhotoImage(file = r'C:\Users\mm7x7\Downloads\Ui_photos\num2.png')
num2_image = num2_png.subsample(1, 1)

num3_png = PhotoImage(file = r'C:\Users\mm7x7\Downloads\Ui_photos\num3.png')
num3_image = num3_png.subsample(1, 1)

num4_png = PhotoImage(file = r'C:\Users\mm7x7\Downloads\Ui_photos\num4.png')
num4_image = num4_png.subsample(1, 1)

confirm_png = PhotoImage(file = r'C:\Users\mm7x7\Downloads\Ui_photos\confirm_btn.png')
confirm_image = confirm_png.subsample(5, 5)

cancel_png = PhotoImage(file = r'C:\Users\mm7x7\Downloads\Ui_photos\cancel_btn.png')
cancel_image = cancel_png.subsample(13, 13)

exit_btn = PhotoImage(file = r'C:\Users\mm7x7\Downloads\Ui_photos\Exit.png')
exit_image = exit_btn.subsample(5, 5)
# Turning various photos into objects for buttons

main_screen()
# Running first frame

root.mainloop()
# Initializing root
