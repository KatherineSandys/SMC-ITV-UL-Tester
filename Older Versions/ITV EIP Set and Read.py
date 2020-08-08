#Library to Generate Set and Get EIP packagees
import pyeip

#variables
hostname = "192.168.1.20"
EIP = pyeip.EtherNetIP(hostname)
C1 = EIP.explicit_conn(hostname)
high = 4095
low = 0

#Get Setpoint
SetPoint = int(input("Enter Setpoint: "))
x = SetPoint.to_bytes(2, "little")
#path = C1.mkReqPath(0x1, 1, None)
data = pyeip.struct.pack("BB", x[0], x[1])

r = C1.setAttrSingle(0x64, 0x64,0x03, data)
if 0 == r[0]:
    #print(int.from_bytes(r[1],"little"))
    print("Wrote!")
else:
    print("Failed to write")

r = C1.getAttrSingle(0x96, 0x96,0x03)
if 0 == r[0]:
    print(int.from_bytes(r[1],"little"))
else:
    print("Failed to read")
