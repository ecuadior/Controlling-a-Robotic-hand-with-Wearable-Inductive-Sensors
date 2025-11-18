//Read LDC Sensor data
//Use methods from RegisterSetup.ino

//store raw LDC value
unsigned long data0, data1, data2, data3; 

void RawData()
{
    // update channel info and store data in vars
    //previous group had 268435455 an arbitrary value appear frequecntly so tenery operator use
    data0 = readChannel0() != 268435455 ? readChannel0() : data0;
    data1 = readChannel1() != 268435455 ? readChannel1() : data1;
    data2 = readChannel2() != 268435455 ? readChannel2() : data2;
    data3 = readChannel3() != 268435455 ? readChannel3() : data3;
    Serial.println("Channel 0: " , data0);
    Serial.println("Channel 1: " , data1);
    Serial.println("Channel 2: " , data2);
    Serial.println("Channel 3: " , data3);
}
//function for ploting raw data
void plotRawData()
{

}

void setup()
{
    Serial.begin(115200);
    setupI2C(); //set up the register of LDC module

}

void loop()
{
    RawData();
    delay(10);
}