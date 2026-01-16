from machine import I2C, Pin

#I2C
LDC = 0x2A

#Channrl Address
CH0MSB, CH0LSB = 0x00, 0x01
CH1MSB, CH1LSB = 0x02, 0x03
CH2MSB, CH2LSB = 0x04, 0x05
CH3MSB, CH3LSB = 0x06, 0x07

#I2C setup - Pins subject to change
i2c = I2C(
    0,
    scl = Pin(22),
    sda =Pin(21),
    freq = 400000
)

#read value
def readValue(addr, reg):
    i2c.writeto(addr, bytes([reg])) # write register address
    #read 2 bytes
    data = i2c.readfrom(addr,2)
    msb = data[0]
    lsb = data[1]
    return (msb<<8) | lsb #combine into 1 16 bit number by shifting

#read channels 
def readChannel0():
    c = readValue(LDC, CH0MSB)
    d = readValue(LDC,CH0LSB)

    val = c
    val <<=16
    val+=d
    return val
def readChannel1():
    c = readValue(LDC, CH1MSB)
    d = readValue(LDC,CH1LSB)

    val = c
    val <<=16
    val+=d
    return val
def readChannel2():
    c = readValue(LDC, CH2MSB)
    d = readValue(LDC,CH2LSB)

    val = c
    val <<=16
    val+=d
    return val
def readChannel3():
    c = readValue(LDC, CH3MSB)
    d = readValue(LDC,CH3LSB)

    val = c
    val <<=16
    val+=d
    return val

#Creates 16-bit configuration value --> LDC congiguration register
def writeConfig(addr,reg,msb,lsb):
    i2c.writeto(addr, bytes([reg,msb,lsb]))

#Base on Table 48 of LDC1614 Datasheet in Typical Application
def Configuration():
    #CH0
    writeConfig(LDC,0x14,0x10,0x02)#Clock_divider
    writeConfig(LDC,0x1E,0x90,0x00)# Drive_Cuurent
    writeConfig(LDC,0x10,0x00,0x0A)#Settlecount
    writeConfig(LDC,0x08,0x04,0xD6)#Rcount
    #Ch1
    writeConfig(LDC,0x15,0x10,0x02)#Clock_divider
    writeConfig(LDC,0x1F,0x90,0x00)# Drive_Cuurent
    writeConfig(LDC,0x11,0x00,0x0A)#Settlecount
    writeConfig(LDC,0x09,0x04,0xD6)#Rcount
    #Ch2
    writeConfig(LDC,0x16,0x10,0x02)#Clock_divider
    writeConfig(LDC,0x20,0x90,0x00)#Drive_Cuurent
    writeConfig(LDC,0x12,0x00,0x0A)#Settlecount
    writeConfig(LDC,0x0A,0x04,0xD6)#Rcount
    #Ch3
    writeConfig(LDC,0x17,0x10,0x02) #Clock_divider
    writeConfig(LDC,0x21,0x90,0x00) # Drive_Cuurent
    writeConfig(LDC,0x13,0x00,0x0A) #Settlecount
    writeConfig(LDC,0x0B,0x04,0xD6) #Rcount

    writeConfig(LDC,0x19,0x00,0x00) #ErrorConfig
    #MUXconfig only one that changed from Table48
    #chnage becasue now Ch0,CH1,CH2,Ch3 are enabled
    writeConfig(LDC,0x1B,0xC2,0x0C) 

#configure the registers
def setupI2C():
    Configuration()