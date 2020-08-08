from PyQt5 import QtCore, QtGui, QtWidgets
from control_ITV_UI import Ui_ITV_control
import pyeip
import sys

hostname1 = "192.168.1.20"  #IP address of ITV 1
hostname2 = "192.168.1.21"  #IP address of ITV 2
hostname3 = "192.168.1.22"  #IP address of ITV 3
EIP_1 = pyeip.EtherNetIP(hostname1)
EIP_2 = pyeip.EtherNetIP(hostname2)
EIP_3 = pyeip.EtherNetIP(hostname3)
C_A = 1 #default network status is disconnected
C_B = 1 #default network status is disconnected
C_C = 1 #default network status is disconnected
high = 4095 #max count value
low = 0 #min count value
value = low     # initial value state

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ITV_control()
        self.ui.setupUi(self) #set up ui
        self.ui.quit.clicked.connect(button_quit) #quit button
        self.show() #dont want to show the screen on load
        #button to triggers give input to ITVs that are connected
        self.ui.on.clicked.connect(lambda: button_response("on"))
        self.ui.off.clicked.connect(lambda: button_response("off"))
        #turns ITV's to recieve input
        self.ui.ITV_A.stateChanged.connect(lambda: check_connection(self.ui.ITV_A, 1))
        self.ui.ITV_B.stateChanged.connect(lambda: check_connection(self.ui.ITV_B, 2))
        self.ui.ITV_C.stateChanged.connect(lambda: check_connection(self.ui.ITV_C, 3))
        # timer that makes the screen responsive updates for pressure
        self.my_timer = QtCore.QTimer()
        self.my_timer.timeout.connect(lambda: update_status(self))   #call the update_status function every one second
        self.my_timer.start(1000) #sets update interval

#quit function
def button_quit():
    #print("quit")
    sys.exit(app.exec_())

#button responses for high and low button
def button_response(name):
    if name == "on":      #sets value to button being pushed
        value = 4095
        print(str(value))
    if name == "off":
        value = 0
        print(str(value))
    if C_A != 1: #writes new count value to the connected ITV
        #print("Attempting to write")
        x = value.to_bytes(2, "little") #change to bytes
        data = pyeip.struct.pack("BB", x[0], x[1]) #format the vale to send out
        if C_A != 1: #if connected
            #print("Write to ITV 1")
            r = C_A.setAttrSingle(0x64, 0x64, 0x03, data) #write data to ITV
            #if r[0] != 0:
                #print("Failed to write")
    if C_B != 1: #writes new count value to the connected ITV
        #print("Attempting to write")
        x = value.to_bytes(2, "little") #change to bytes
        data = pyeip.struct.pack("BB", x[0], x[1])
        if C_B != 1:
            #print("Write to ITV 2")
            r = C_B.setAttrSingle(0x64, 0x64, 0x03, data) #write data to ITV
            #if r[0] != 0:
                #print("Failed to write")
    if C_C != 1: #writes new count value to the connected ITV
        #print("Attempting to write")
        x = value.to_bytes(2, "little") #change to bytes
        data = pyeip.struct.pack("BB", x[0], x[1])
        if C_C != 1:
            #print("Write to ITV 3")
            r = C_C.setAttrSingle(0x64, 0x64, 0x03, data) #write data to ITV
            #if r[0] != 0:
                #print("Failed to write")

# Connection is only attempted and data is sent when a checkbox is active. If previous attempt fails,
# need to uncheck and recheck box to attempt another connection
def check_connection(c, ITV):
    if c.isChecked() == True:       #executes at checkbox state change, only executes if checked
        if ITV == 1:                #ITV variable selects which ITV should be connected
            print("Attempting to connect...")
            try:    #attempt to connect ITV1
                global EIP_1, C_A
                EIP_1= pyeip.EtherNetIP(hostname1)
                C_A = EIP_1.explicit_conn(hostname1)
            except Exception:   #general catch-all error handler, triggers if no connection detected
                C_A = 1  #set C_A back to disconnected state

        elif ITV == 2:  # checks whatever ITV is specified by variable ITV (passed in from checkbox)
            print("Attempting to connect...")
            try:
                global EIP_2, C_B
                EIP_2= pyeip.EtherNetIP(hostname2)
                C_B = EIP_2.explicit_conn(hostname2)
            except Exception:
                #self.label_ITV_B.setText("ITV 2 (psi): " + str(pressure))
                C_B = 1
        elif ITV == 3:
            print("Attempting to connect...")
            try:
                global EIP_3, C_C
                EIP_3= pyeip.EtherNetIP(hostname3)
                C_C = EIP_3.explicit_conn(hostname3)
            except Exception:
                C_C = 1
    else:       # no connection found, set C_# to non-connected state
        #print("Not Connected")
        if ITV == 1:
            C_A = 1
        elif ITV == 2:
            C_B = 1
        elif ITV == 3:
            C_C = 1

# attempts to read count values from all connected ITVs and converts into PSI, Outputs to specific label
def update_status(self):
    if C_A != 1: #if connection exists read and display values
        r = C_A.getAttrSingle(0x96, 0x96, 0x03)
        print(r[1])
        if 0 == r[0]:
            print(int.from_bytes(r[1],"little"))
            if(r[1][-2:] == b'\x00\x00'):
                pressure = int.from_bytes(r[1],"little") #in counts
                pressure = pressure / 31.37 #convert to psi
                pressure = round(pressure, 1) #rounding to 10th place
                print(pressure)
                self.ui.ITV_A.setText("ITV 1 (psi): " + str(pressure))
        else:
            self.ui.ITV_A.setText("ITV 1 (psi): Error Detected")
    #else:
        #print("C_A Disconnected")
    if C_B != 1:
        r = C_B.getAttrSingle(0x96, 0x96, 0x03)
        print(r[1])
        if 0 == r[0]:
            print(int.from_bytes(r[1],"little"))
            if(r[1][-2:] == b'\x00\x00'):
                pressure = int.from_bytes(r[1],"little") #in counts
                pressure = pressure / 31.37 #convert to psi
                pressure = round(pressure, 1) #rounding to 10th place
                print(pressure)
                self.ui.ITV_B.setText("ITV 2 (psi): " + str(pressure))
        else:
            self.ui.ITV_B.setText("ITV 2 (psi): Error Detected")
    #else:
        #print("C_B Disconnected")
    if C_C != 1:
        r = C_C.getAttrSingle(0x96, 0x96, 0x03)
        print(r[1])
        if 0 == r[0]:
            print(int.from_bytes(r[1],"little"))
            if(r[1][-2:] == b'\x00\x00'):
                pressure = int.from_bytes(r[1],"little") #in counts
                pressure = pressure / 31.37 #convert to psi
                pressure = round(pressure, 1) #rounding to 10th place
                print(pressure)
                self.ui.ITV_C.setText("ITV 3 (psi): " + str(pressure))
        else:   #Connected, error with the ITV
            self.ui.ITV_C.setText("ITV 3 (psi): Error Detected")
    #else:
        #print("C_C Disconnected")

def main():
    global app
    app = QtWidgets.QApplication(sys.argv)

    a = window()

    a.show()
    sys.exit(app.exec_())
    spi.close()

main()
