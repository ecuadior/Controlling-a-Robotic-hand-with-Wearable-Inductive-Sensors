# Read LDC Sensor data
# Use methods from LDCRegisterSetup.py
# readChannel, setupI2C
import time
from LDCRegisterSetup import (
    readChannel0,
    readChannel1,
    readChannel2,
    readChannel3,
    setupI2C
)


# store raw LDC Value
data0 =0
data1 = 0
data2 = 0
data3 = 0

def RawData():
    global data0, data1, data2 ,data3

    # update channel info and store data in vars
    # previous group had 268435455 an arbitrary value appear frequecntly
    d0 = readChannel0()
    d1 = readChannel1()
    d2 = readChannel2()
    d3 = readChannel3()

    if d0 != 268435455:
        data0 = d0
    if d1 != 268435455:
        data1 = d1
    if d2 != 268435455:
        data2 = d2
    if d3 != 268435455:
        data3 = d3
    print("Channel 0:", data0)
    print("Channel 1:", data1)
    print("Channel 2:", data2)
    print("Channel 3:", data3)
    print()

# function for plotting raw data
def plotRawData():
    global data0, data1, data2, data3
    p0 = readChannel0()
    if p0 != 268435455:
        data0 = p0

    p1 = readChannel1()
    if p1 != 268435455:
        data1 = p1

    p2 = readChannel2()
    if p2 != 268435455:
        data2 = p2

    p3 = readChannel3()   
    if p3 != 268435455:
        data3 = p3

    print(data1)

def MATLABplotData():
    global data0, data1, data2

    p0 = readChannel0()
    if p0 != 268435455:
        data0 = p0

    p1 = readChannel1()
    if p1 != 268435455:
        data1 = p1

    p2 = readChannel2()
    if p2 != 268435455:
        data2 = p2

    # Send all three channels separated by commas
    print(f"{data0},{data1},{data2}")


#LPF setting
fs =100.0 # sampling frequency 100 Hz
cutoff = 8.0 # cutoff freuncy 8Hz
alpha = (2*3.1416*cutoff)/ (fs +2_3.1416*cutoff)

#filter values
lpf0=0
lpf1=0
lpf2=0
lpf3=0 

def LPFData():
    global lpf0,lpf1,lpf2,lpf3
    #read raw val
    x0 = readChannel0()
    x1 = readChannel1()
    x2 = readChannel2()
    x3 = readChannel3()

    # ignore invalid readings
    if x0 == 268435455 or x1 == 268435455 or x2 == 268435455 or x3 == 268435455:
        return None
     # Single-pole low-pass filter
    #   -Measure how far off you are
    #   -Move partway toward the new value
    #   -Store it for next time
    lpf0 = lpf0 + alpha *(x0-lpf0)
    lpf1 = lpf1 + alpha *(x1-lpf1)
    lpf2 = lpf2 + alpha *(x2-lpf2)
    lpf3 = lpf3 + alpha *(x3-lpf3)

    #output filter data
    print(f"{int(lpf0)}, {int(lpf1)},{int(lpf2)},{int(lpf3)}")


def setup():
    setupI2C()  # set up the register of LDC module


def loop():
    MATLABplotData()
    time.sleep_ms(100)


# ---- main execution ----
setup()
while True:
    loop()






