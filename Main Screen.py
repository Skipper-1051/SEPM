import tkinter as tk


def call():
    calling = tk.Toplevel(window)
    calling.title("Calling")
    calling.geometry("100x150")
    l7 = tk.Label(calling, text="Calling...")
    l7.pack()


def message():
    messaging = tk.Toplevel(window)
    messaging.title("Messaging")
    messaging.geometry("300x150")
    l8 = tk.Label(messaging, text="Current Location has been sent to the authorities.")
    l8.pack()
    l9 = tk.Label(messaging, text="Please stay where you are")
    l9.pack()


def add():
    contact = tk.Toplevel(window)
    contact.title("ADD EMERGENCY CONTACT")
    contact.geometry("300x150")
    tk.Label(contact, text="Enter Contact Details:", font=("arial", 10)).pack()
    tk.Label(contact, text="Enter Name", font=("arial", 10)).pack()
    tk.Entry(contact, font=("arial", 10)).pack()
    tk.Label(contact, text="Enter Mobile Number", font=("arial", 10)).pack()
    tk.Entry(contact, font=("arial", 10)).pack()
    tk.Button(contact, text="Save", font=("arial", 10), command=save).pack()


def save():
    s = tk.Toplevel(window)
    s.geometry("150x150")
    tk.Label(s, text="Data Saved").pack()


window = tk.Tk()
l1 = tk.Label(window, text="Signal Strength:OK                                                         GPS:ON", anchor='w', font=("arial", 10), bg="MediumOrchid2")
l1.pack(fill='both')
l1 = tk.Label(window, text="Country:INDIA", anchor='w', font=("arial", 10), bg="MediumOrchid2")
l1.pack(fill='both')
l2 = tk.Label(window, text="USER 1", font=("arial", 17), bg="MediumOrchid2")
l2.pack()
l3 = tk.Label(window, text="Available Signals:3", font=("arial", 13), bg="MediumOrchid2")
l3.pack()
l3 = tk.Label(window, text=" ", bg="MediumOrchid2")
l3.pack()
l3 = tk.Label(window, text="Emergency Services:", font=("arial", 12), anchor='w', bg="MediumOrchid2")
l3.pack(fill='both')
l4 = tk.Label(window, text="     Police", font=("arial", 11), anchor='w', bg="MediumOrchid2")
l4.pack(fill='both')
b1 = tk.Button(window, text="CALL", font=('arial', 13), command=call)
b1.place(x=150, y=175)
b2 = tk.Button(window, text="MESSAGE", font=('arial', 13), command=message)
b2.place(x=250, y=175)
l5 = tk.Label(window, text="     Ambulance", font=("arial", 11), anchor='w', bg="MediumOrchid2")
l5.place(x=0, y=230)
b3 = tk.Button(window, text="CALL", font=('arial', 13), command=call)
b3.place(x=150, y=260)
b4 = tk.Button(window, text="MESSAGE", font=('arial', 13), command=message)
b4.place(x=250, y=260)
l6 = tk.Label(window, text="     Fire Brigade", font=("arial", 11), anchor='w', bg="MediumOrchid2")
l6.place(x=0, y=320)
b5 = tk.Button(window, text="CALL", font=('arial', 13), command=call)
b5.place(x=150, y=350)
b6 = tk.Button(window, text="MESSAGE", font=('arial', 13), command=message)
b6.place(x=250, y=350)
b7 = tk.Button(window, text="Add Emergency Contact", font=("arial", 11), anchor='w', command=add)
b7.place(x=100, y=425)
window.geometry('400x600')
window.configure(bg="MediumOrchid2")
window.mainloop()
