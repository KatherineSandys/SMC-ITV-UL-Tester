#Library to Generate Set and Get EIP packagees
import tkinter as tk
import pyeip
import time
import tkinter.font as font

#function for ITV's
def signal(value):
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

def connect(num, state):
    if(state):
        if(num == 1):
            label_1 = tk.Label(master=window, text="Pressure (psi): 130.5")
            label_1['font'] = myFont
            label_1.grid(row=1, column=1, sticky="nsew")
            try:
                C1_1 = EIP_1.explicit_conn(hostname1)
            except TimeoutError:
                C1_1 = 1
                label_1 = tk.Label(master=window, text="Pressure (psi): 0")
                label_1['font'] = myFont
                label_1.grid(row=1, column=1, sticky="nsew")
        elif(num == 2):
            label_2 = tk.Label(master=window, text="Pressure (psi): 130.5")
            label_2['font'] = myFont
            label_2.grid(row=2, column=1, sticky="nsew")
            try:
                Cl_2 = EIP_2.explicit_conn(hostname2)
            except TimeoutError:
                Cl_2 = 1
                label_2 = tk.Label(master=window, text="Pressure (psi): 0")
                label_2['font'] = myFont
                label_2.grid(row=2, column=1, sticky="nsew")
        elif(num == 3):
            label_3 = tk.Label(master=window, text="Pressure (psi): 130.5")
            label_3['font'] = myFont
            label_3.grid(row=3, column=1, sticky="nsew")
            try:
                Cl_3 = EIP_3.explicit_conn(hostname3)
            except TimeoutError:
                Cl_3 = 1
                label_3 = tk.Label(master=window, text="Pressure (psi): 0")
                label_3['font'] = myFont
                label_3.grid(row=3, column=1, sticky="nsew")
    else:
        if(num == 1):
            C1_1 = 1
            label_1 = tk.Label(master=window, text="Pressure (psi): 0")
            label_1['font'] = myFont
            label_1.grid(row=1, column=1, sticky="nsew")
        elif(num == 2):
            label_2 = tk.Label(master=window, text="Pressure (psi): 0")
            label_2['font'] = myFont
            label_2.grid(row=2, column=1, sticky="nsew")
        elif(num == 3):
            label_3 = tk.Label(master=window, text="Pressure (psi): 0")
            label_3['font'] = myFont
            label_3.grid(row=3, column=1, sticky="nsew")


#delay 10 seconds
#time.sleep(10)

#variables
hostname1 = "192.168.1.20"
hostname2 = "192.168.1.21"
hostname3 = "192.168.1.22"
EIP_1 = pyeip.EtherNetIP(hostname1)
EIP_2 = pyeip.EtherNetIP(hostname2)
EIP_3 = pyeip.EtherNetIP(hostname3)
C1_1 = 1 #defult value
Cl_2 = 1 #defult value
Cl_3 = 1 #defult value
high = 4095
low = 0
values = {high, low}
Cl_list = {C1_1, Cl_2, Cl_3}

#SET SCREEN
#gui
window = tk.Tk()

# define font
myFont = font.Font(size=30) #size of text
window.geometry("650x500") #window size

#high and low button
btn_high = tk.Button(master=window, text="\nHIGH\n", command=lambda:signal(high), width=10)
btn_high.grid(row=0, column=0, sticky="nsew")
btn_low = tk.Button(master=window, text="\nLOW\n", command=lambda:signal(low), width=10)
btn_low.grid(row=0, column=1, sticky="nsew")

btn_high['font'] = myFont
btn_low['font'] = myFont

#quit button
btn_quit =  tk.Button(master=window, text="quit", command=lambda:quit())
btn_quit.grid(row=4, column=0, sticky="nsew")
btn_quit['font'] = myFont

#3 check box's for the ITV's to show if connected
chkValue1 = tk.BooleanVar()
ITV_1 = tk.Checkbutton(master=window, text="ITV 1", command=lambda:connect(1,chkValue1.get()), background='white', variable=chkValue1)
ITV_1.grid(row=1, column=0, sticky="nsew")
chkValue2 = tk.BooleanVar()
ITV_2 = tk.Checkbutton(master=window, text="ITV 2", command=lambda:connect(2,chkValue2.get()), background='gray', variable=chkValue2)
ITV_2.grid(row=2, column=0, sticky="nsew")
chkValue3 = tk.BooleanVar()
ITV_3 = tk.Checkbutton(master=window, text="ITV 3", command=lambda:connect(3,chkValue3.get()), background='white', variable=chkValue3)
ITV_3.grid(row=3, column=0, sticky="nsew")

ITV_1['font'] = myFont
ITV_2['font'] = myFont
ITV_3['font'] = myFont

#Pressure labels
label_1 = tk.Label(master=window, text="Pressure (psi): 0")
label_1['font'] = myFont
label_1.grid(row=1, column=1, sticky="nsew")
label_2 = tk.Label(master=window, text="Pressure (psi): 0")
label_2['font'] = myFont
label_2.grid(row=2, column=1, sticky="nsew")
label_3 = tk.Label(master=window, text="Pressure (psi): 0")
label_3['font'] = myFont
label_3.grid(row=3, column=1, sticky="nsew")

print("C1's: " + str(C1_1) + " " +str(Cl_2) + " " +str(Cl_3))
print("Setup Complete")

#loop for window to make it responsive
window.mainloop()
