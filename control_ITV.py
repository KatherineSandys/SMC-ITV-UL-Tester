#Library to Generate Set and Get EIP packagees
import tkinter as tk
import pyeip
import time

#variables
hostname1 = "192.168.1.20"
hostname2 = "192.168.1.21"
hostname3 = "192.168.1.22"
EIP_1 = pyeip.EtherNetIP(hostname1)
EIP_2 = pyeip.EtherNetIP(hostname2)
EIP_3 = pyeip.EtherNetIP(hostname3)

try:
    C1_1 = EIP_1.explicit_conn(hostname1)
except TimeoutError:
    C1_1 = 1
try:
    Cl_2 = EIP_2.explicit_conn(hostname2)
except TimeoutError:
    Cl_2 = 1
try:
    Cl_3 = EIP_3.explicit_conn(hostname3)
except TimeoutError:
    Cl_3 = 1

high = 4095
low = 0
values = {high, low}
Cl_list = {C1_1, Cl_2, Cl_3}

#set defult
SetPoint = low
x = SetPoint.to_bytes(2, "little")
data = pyeip.struct.pack("BB", x[0], x[1])
for i in Cl_list:
    if i != 1:
        r = i.setAttrSingle(0x64, 0x64, 0x03, data)
        if 0 == r[0]:
            print("Wrote!")
        else:
            print("Failed to write")

        r = i.getAttrSingle(0x96, 0x96, 0x03)
        if 0 == r[0]:
            print(int.from_bytes(r[1],"little"))
        else:
            print("Failed to read")

print("Setup Complete")

#gui
window = tk.Tk()

#function to set ITV
def signal(value):
    refresh()
    SetPoint = value
    x = SetPoint.to_bytes(2, "little") #change to bytes
    data = pyeip.struct.pack("BB", x[0], x[1])
    for i in Cl_list:
        if i != 1:
            r = i.setAttrSingle(0x64, 0x64, 0x03, data)
            if 0 == r[0]:
                print("Wrote!")
            else:
                print("Failed to write")

            r = i.getAttrSingle(0x96, 0x96, 0x03)
            if 0 == r[0]:
                print(int.from_bytes(r[1],"little"))
            else:
                print("Failed to read")

def refresh():
    try:
        C1_1 = EIP_1.explicit_conn(hostname1)
    except TimeoutError:
        C1_1 = 1
    try:
        Cl_2 = EIP_2.explicit_conn(hostname2)
    except TimeoutError:
        Cl_2 = 1
    try:
        Cl_3 = EIP_3.explicit_conn(hostname3)
    except TimeoutError:
        Cl_3 = 1
    Cl_list = {C1_1, Cl_2, Cl_3}
    count = 0
    for j in Cl_list:
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=2, column=count)
        color = "red"
        if j != 1: #"green" means connected, "red" means not connected
            color = "green"
        label = tk.Label(master=frame, text=f"ITV {count + 1}", background=color, width=15, height=3)
        count += 1
        label.pack()
    print("Cl's: " + str(C1_1) + " " +str(Cl_2) + " " +str(Cl_3))

#high and low buttons
btn_high = tk.Button(master=window, text="HIGH", command= lambda: signal(high))
btn_high.grid(row=0, column=0, sticky="nsew")
btn_low = tk.Button(master=window, text="LOW", command= lambda: signal(low))
btn_low.grid(row=0, column=1, sticky="nsew")
btn_refresh = tk.Button(master=window, text="refresh", command=lambda: refresh())
btn_refresh.grid(row=0, column=2, sticky="nsew")
    
#3 box's for the ITV's to show if connected
count = 0
for j in Cl_list:
    frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    frame.grid(row=2, column=count)
    color = "red"
    if j != 1: #"green" means connected, "red" means not connected
        color = "green"
    label = tk.Label(master=frame, text=f"ITV {count + 1}", background=color, width=15, height=3)
    count += 1
    label.pack()

print("C1's: " + str(C1_1) + " " +str(Cl_2) + " " +str(Cl_3))

#messages to the screen - need to test
label1 = tk.Label(master=frame, text="Setup Complete")
label1.pack()

#loop for window to make it responsive
window.mainloop()
