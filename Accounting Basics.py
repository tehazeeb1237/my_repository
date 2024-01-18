import tkinter as tk
import pygame
from datetime import datetime

pygame.mixer.init()

parent = tk.Tk()
parent.geometry('800x600')
bg = tk.PhotoImage(file='bank.png')
label = tk.Label(parent, image=bg)
label.place(x=0, y=0)
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
tk.Label(parent, text=' WELCOME TO WISESAVER BANK ', font=("Helvetica 30"), height=3, bg='#87CEEB', fg='white').pack()
tk.Label(parent, bg='#87CEEB', height=10)

button_frame = tk.Frame(parent, bg='#87CEEB')
button_frame.place(x=520, y=560)

def New_Window():
    pygame.mixer.music.load("click.mp3")
    pygame.mixer.music.play(loops=0)
    root = tk.Toplevel()
    root.title("Checkbook Transactions")
    root.geometry('800x600')
    root.configure(bg='#87CEEB')

    def clear():
        entry1.delete(first=0, last=20)
        inputs.delete("1.0", "end")

    def tra_fun():
        pb = 'PREVIOUS BALANCE'
        nb = 'NEW BALANCE'
        balance = 0
        num_checks_cleared = 0
        prev_month = None
        service_charge = 0
        first_record = entry1.get()
        balance = float(first_record[:-8])
        start_date_input = first_record[-6:]
        start_date = datetime.strptime(start_date_input, '%m%d%y').date()
        prev_bal = balance
        previous = balance
        tran_list = inputs.get(1.0, "end-1c").split()
        l = len(tran_list)
        for i in range(0, l):
            record = tran_list[i]
            if i < l - 1:
                rec = tran_list[i + 1]
            else:
                rec = tran_list[i]
            amount = float(record[:-8])
            code = record[-8:-6]
            date_str = record[-6:]
            date = datetime.strptime(date_str, '%m%d%y').date()
            date_str1 = rec[-6:]
            date1 = datetime.strptime(date_str1, '%m%d%y').date()
            if code == 'DB':
                previous = balance
                balance -= amount
            if previous < 500:
                num_checks_cleared += 1
            if code == 'CR':
                balance += amount
            if previous < 500 and prev_month != date1.month:
                service_charge = 0.12 * num_checks_cleared
                prev_month = date.month
            if service_charge != 0 or service_charge == 0:
                a = 'CR' if prev_bal >= 0 else 'DB'
                b = 'CR' if balance >= 0 else 'DB'
                c = 'CR' if balance > previous else 'DB'
                transaction = f'{pb} {abs(prev_bal):.2f}{a} {amount:.2f}{c} {nb} {abs(balance):.2f}{b}'
                transactions.append(transaction)
                history_label.config(text='\n'.join(transactions))
                prev_bal = balance
            if prev_month != date1.month and service_charge != 0 and previous < 500:
                balance -= service_charge
                num_checks_cleared = 0
                c = 'CR' if prev_bal >= 0 else 'DB'
                d = 'CR' if balance >= 0 else 'DB'
                sc = 'SC'
                transaction = f'{pb} {abs(prev_bal):.2f}{c} {service_charge:.2f}{sc} {nb} {abs(balance):.2f}{d}'
                transactions.append(transaction)
                service_charge = 0
                history_label.config(text='\n'.join(transactions))
                prev_bal = balance
            if balance < 500 and prev_month is not None:
                if num_checks_cleared != 0:
                    service_charge = 0.12 * num_checks_cleared
                    balance -= service_charge
                    e = 'CR' if prev_bal >= 0 else 'DB'
                    f = 'CR' if balance >= 0 else 'DB'
                    sc = 'SC'
                    transaction = f'{pb} {prev_bal:.2f}{e} {service_charge:.2f}{sc} {nb} {balance:.2f}{f}'
                    transactions.append(transaction)
                    history_label.config(text='\n'.join(transactions))

    x = tk.Label(root, text='INITIAL TRANSACTION:\n(xx.xxmmddyy)', font="Georgia 16", bg="#87CEEB", fg='white')
    x.place(x=50, y=100)

    y = tk.Label(root, text='LIST OF TRANSACTIONS:\n(xx.xx(CR/DB)mmddyy)', font="Georgia 15", bg="#87CEEB", fg='#fff')
    y.place(x=50, y=200)

    z = tk.Label(root, text='TRANSACTIONS \nHISTORY:', font="Georgia 16", bg="#87CEEB", fg='#fff')
    z.place(x=50, y=320)

    entry1 = tk.Entry(root, width=70, bd=2, font=20)
    entry1.place(x=300, y=100)

    inputs = tk.Text(root, width=70, bd=4, height=4, font=20)
    inputs.place(x=300, y=200)

    history_label = tk.Label(root, width=70, bd=2, font=20, height=10)
    history_label.place(x=300, y=320)

    submit = tk.Button(root, text="Submit", bg='MediumSpringGreen', fg='black', font="Bold 15", width=15, height=2, command=tra_fun)
    submit.place(x=300, y=590)

    pygame.mixer.music.load('SUBMIT.mp3')
    pygame.mixer.music.play()

    tk.Button(root, text="Clear", bg='green yellow', fg='black', font="Bold 15", width=15, height=2, command=clear).place(x=700, y=590)
    tk.Button(root, text="Exit", bg='tomato', fg='black', width=15, font="Bold 15", height=2, command=lambda: root.destroy()).place(x=500, y=590)
    transactions = []

enter_button = tk.Button(button_frame, text="Enter", fg='white', font="Bold 15", bg='black', width=15, height=2, command=New_Window)
enter_button.grid(row=6, column=0, padx=30, pady=20)

t = tk.Label(parent, bg='#87CEEB', height=2)
t.pack()
t.place(x=50, y=800)

exit_button = tk.Button(button_frame, text="Exit", fg='white', font="Bold 15", bg='black', width=15, height=2, command=parent.destroy)
exit_button.grid(row=6, column=3, padx=30, pady=20)

parent.mainloop()
