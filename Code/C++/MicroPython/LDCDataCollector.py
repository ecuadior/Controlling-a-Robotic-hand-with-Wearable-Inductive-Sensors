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
fs = 100.0          # Hz
cutoff = 8.0        # Hz

dt = 1.0 / fs
RC = 1.0 / (2 * 3.1416 * cutoff)
alpha = dt / (RC + dt)

#filter values
lpf0=None
lpf1=None
lpf2=None
lpf3=None 

INVALID = 268435455 

def LPFData():
    global lpf0,lpf1,lpf2,lpf3
    #read raw val
    x0 = readChannel0()
    x1 = readChannel1()
    x2 = readChannel2()
    x3 = readChannel3()

    # ignore invalid readings
    # Ignore invalid readings, but DO NOT return silently forever
    if x0 != INVALID:
        if lpf0 is None:
            lpf0 = x0
        else:
            lpf0 += alpha * (x0 - lpf0)

    if x1 != INVALID:
        if lpf1 is None:
            lpf1 = x1
        else:
            lpf1 += alpha * (x1 - lpf1)

    if x2 != INVALID:
        if lpf2 is None:
            lpf2 = x2
        else:
            lpf2 += alpha * (x2 - lpf2)

    if x3 != INVALID:
        if lpf3 is None:
            lpf3 = x3
        else:
            lpf3 += alpha * (x3 - lpf3)

   # Only print when at least one channel is valid
    if lpf0 is not None:
        print(f"{int(lpf0)},{int(lpf1 or 0)},{int(lpf2 or 0)},{int(lpf3 or 0)}")
     # Single-pole low-pass filter
    #   -Measure how far off you are
    #   -Move partway toward the new value
    #   -Store it for next time

def setup():
    setupI2C()  # set up the register of LDC module


def loop():
    LPFData()
    time.sleep_ms(10)


# ---- main execution ----
setup()
while True:
    loop()






