#include <Wire.h>

//Registers Address 
const int LDC = 0x2A; // When addr is sent to low 
//Channels Addr
const int CH0MSB = 0x00, CH0LSB = 0x01;
const int  CH1MSB = 0x02, CH1LSB = 0x03;
const int CH2MSB = 0x04, CH2LSB = 0x05;
const int CH3MSB = 0x06, CH3LSB = 0x07; 

unsigned long readChannel0()
{
    unsigned long val= 0;
    // storing regiter val
    word c = 0;
    word d = 0; 
    //MSB need to read first then LSB
    c = readValue(LDC,CH0MSB);
    d = readValue(LDC,CH0LSB);
    val = c; //MSB need to be read first
    val <<= 16; // moving MSB vale 16 bits - need to be place at top
    val += d; // LSB need to be at the bottom
    return val;
}
unsigned long readChannel1()
{
    unsigned long val= 0;
    word c = 0;
    word d = 0; 
    c = readValue(LDC,CH1MSB);
    d = readValue(LDC,CH1LSB);
    val = c; 
    val <<= 16; 
    val += d; 
    return val;
}
unsigned long readChannel2()
{
    unsigned long val= 0;
    word c = 0;
    word d = 0; 
    c = readValue(LDC,CH2MSB);
    d = readValue(LDC,CH2LSB);
    val = c;
    val <<= 16; 
    val += d; 
    return val;
}

//Channel3 subject to chnage when multiplexer is added
unsigned long readChannel3()
{
    unsigned long val= 0;
    word c = 0;
    word d = 0; 
    c = readValue(LDC,CH3MSB);
    d = readValue(LDC,CH3LSB);
    val = c;
    val <<= 16; 
    val += d; 
    return val;
}

uint16_t readValue(uint8_t addr, uint8_t reg)
{
    //I2C sequence of register address -> LDC
    Wire.beginTransmission(addr);
    Wire.write(reg); // tells chip what register is wanted
    Wire.endTransmission(); // stop transmsion

    //Requesting 2 bytes(MSB,LSB) 
    Wire.requestFrom(addr, 2);

//     Code from previous group supposeldy dosent work becasue only reads bytes once becasue only 2 bytes are aviable
//     while (Wire.available()) { 
//     a = Wire.read(); 
//     b = Wire.read(); 
//   } 
    uint8_t msb = Wire.read();
    uint8_t lsb = Wire.read();
    
    return (msb << 8) | lsb; //combine into 1 16 bit number by shifting
}

//Creates 16-bit configuration value --> LDC congiguration register
void writeConfig(int LDC, int reg, int MSB, int LSB) { 

  Wire.beginTransmission(LDC); //LDC addr
  Wire.write(reg); //register to configure
  Wire.write(MSB); //upper byte of data
  Wire.write(LSB); //lower byte of data
  Wire.endTransmission(); // commanf finalized --> LDC update register

}

//Base on Table 48 of LDC1614 Datasheet in Typical Application
void Configuration()
{
    //Ch0
    writeConfig(LDC,0x14,0x10,0x02); //Clock_divider
    writeConfig(LDC,0x1E,0x90,0x00); // Drive_Cuurent
    writeConfig(LDC,0x10,0x00,0x0A); //Settlecount
    writeConfig(LDC,0x08,0x04,0xD6); //Rcount
    //Ch1
    writeConfig(LDC,0x15,0x10,0x02); //Clock_divider
    writeConfig(LDC,0x1F,0x90,0x00); // Drive_Cuurent
    writeConfig(LDC,0x11,0x00,0x0A); //Settlecount
    writeConfig(LDC,0x09,0x04,0xD6); //Rcount
    //Ch2
    writeConfig(LDC,0x16,0x10,0x02); //Clock_divider
    writeConfig(LDC,0x20,0x90,0x00); // Drive_Cuurent
    writeConfig(LDC,0x12,0x00,0x0A); //Settlecount
    writeConfig(LDC,0x0A,0x04,0xD6); //Rcount
    //Ch3
    writeConfig(LDC,0x17,0x10,0x02); //Clock_divider
    writeConfig(LDC,0x21,0x90,0x00); // Drive_Cuurent
    writeConfig(LDC,0x13,0x00,0x0A); //Settlecount
    writeConfig(LDC,0x0B,0x04,0xD6); //Rcount

    writeConfig(LDC,0x19,0x00,0x00); //ErrorConfig
    //MUXconfig only one that changed from Table48
    //chnage becasue now Ch0,CH1,CH2,Ch3 are enabled
    writeConfig(LDC,0x1B,0xC2,0x0C); 
}

//SetupI2C and configure the registers
void setupI2C()
{
    Wire.begin();
    Configuration();
}