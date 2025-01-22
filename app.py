from customtkinter import *

set_appearance_mode('dark')
set_default_color_theme('blue')

root = CTk()
root.title("Amman's Monthly spending calculator")
root.iconbitmap('icon.ico')
root.geometry('800x600+450+100')
root.resizable(False, False)


# Functions #
def file_read():
    file = open('Text files/Total spending of Amman.txt', 'r')
    file2 = float(file.read())
    file.close()
    return file2


def file_write(sums):
    file = open('Text files/Total spending of Amman.txt', 'w')
    file2 = file.write(str(sums))
    file.close()


def add():
    window = CTkToplevel(root)

    def adding():
        sums = file_read()
        money = float(entry1.get())
        entry1.delete(0, END)
        new = sums + money
        file_write(new)

    def saving():
        window.destroy()

    window.geometry('500x300+650+300')
    window.title("Add Money")
    window.iconbitmap('icon.ico')
    window.resizable(False, False)
    label = CTkLabel(window, text='Adding Money', font=('Arial', 15, 'bold'))
    label.place(x=195, y=20)
    entry1 = CTkEntry(window, height=40, width=150, placeholder_text='Enter amount', font=('Arial', 14))
    entry1.pack(pady=70)
    add_button = CTkButton(window, text='Add', height=30, width=80, font=('Arial', 18, 'bold'), command=adding)
    add_button.place(x=210, y=150)
    close_button = CTkButton(window, text='Close', fg_color='#ba132c', height=30, width=80,
                             font=('Arial', 18, 'bold'), command=saving)
    close_button.place(x=210, y=200)


def subtract():
    window = CTkToplevel(root)

    def subtracting():
        sums = file_read()
        money = float(entry1.get())
        entry1.delete(0, END)
        new = sums - money
        file_write(new)

    def saving():
        window.destroy()

    window.geometry('500x300+650+300')
    window.title("Subtract Money")
    window.iconbitmap('icon.ico')
    window.resizable(False, False)
    label = CTkLabel(window, text='Subtracting Money', font=('Arial', 15, 'bold'))
    label.place(x=177, y=20)
    entry1 = CTkEntry(window, height=40, width=150, placeholder_text='Enter amount', font=('Arial', 14))
    entry1.pack(pady=70)
    add_button = CTkButton(window, text='Subtract', height=30, width=80, font=('Arial', 15, 'bold'),
                           command=subtracting)
    add_button.place(x=210, y=150)
    close_button = CTkButton(window, text='Close', fg_color='#ba132c', height=30, width=80,
                             font=('Arial', 18, 'bold'), command=saving)
    close_button.place(x=210, y=200)


def clear_data():
    window = CTkToplevel(root)

    def clearing():
        window.destroy()
        file_write('0')
        new_window = CTkToplevel(root)
        new_window.title('Clear Data')
        new_window.iconbitmap('icon.ico')
        new_window.geometry('350x100+730+390')
        new_window.resizable(False, False)
        new_label = CTkLabel(new_window, text='The data has been cleared', font=('Arial', 15, 'bold'))
        new_label.pack(pady=10)
        ok_button = CTkButton(new_window, text='Ok', height=160, width=70, font=('Arial', 15, 'bold'),
                              command=new_window.destroy)
        ok_button.pack(pady=10)

    window.geometry('450x150+660+360')
    window.title("Cleat Data")
    window.iconbitmap('icon.ico')
    window.resizable(False, False)
    label = CTkLabel(window, text='Are you sure you want to clear all the data?', font=('Arial', 15, 'bold'))
    label.pack(pady=30)
    yes_button = CTkButton(window, text='Yes', height=30, width=80, font=('Arial', 18, 'bold'), command=clearing)

    yes_button.place(x=130, y=75)
    no_button = CTkButton(window, text='No', height=30, width=80, font=('Arial', 18, 'bold'), command=window.destroy)
    no_button.place(x=240, y=75)


def show_total_spending():
    money = format(file_read(), '.2f')
    count_money = f'You have spent  {money}  Euros this month.'
    window = CTkToplevel(root)
    window.geometry('450x150+660+360')
    window.title("Cleat Data")
    window.iconbitmap('icon.ico')
    window.resizable(False, False)
    label = CTkLabel(window, text=count_money, font=('Arial', 17, 'bold'))
    label.pack(pady=30)
    ok_button = CTkButton(window, text='Ok', height=30, width=80, font=('Arial', 15, 'bold'), command=window.destroy)
    ok_button.pack()


# Adding Labels
label1 = CTkLabel(root, text='Menu', font=('Arial', 40, 'bold'))
label1.pack(pady=50)

# Adding Buttons
button1 = CTkButton(root, text='Add Money', height=50, width=400, font=('Arial', 20, 'bold'), command=add)
button1.pack(pady=6)

button2 = CTkButton(root, text='Subtract Money', height=50, width=400, font=('Arial', 20, 'bold'), command=subtract)
button2.pack(pady=6)

button3 = CTkButton(root, text='Clear Data', height=50, width=400, font=('Arial', 20, 'bold'), command=clear_data)
button3.pack(pady=6)

button4 = CTkButton(root, text='Show Total Spending', height=50, width=400, font=('Arial', 20, 'bold'),
                    command=show_total_spending)
button4.pack(pady=6)

button5 = CTkButton(root, text='Exit', fg_color='#ba132c', height=40, width=150, font=('Arial', 20, 'bold'),
                    command=root.destroy)
button5.pack(pady=75)

root.mainloop()
