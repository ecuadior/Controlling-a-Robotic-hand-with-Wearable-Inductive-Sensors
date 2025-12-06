//Read LDC Sensor data
//Use methods from RegisterSetup.ino
//readChannel,setupI2C

//store raw LDC value
unsigned long data0, data1, data2, data3; 

void RawData()
{
    // update channel info and store data in vars
    //previous group had 268435455 an arbitrary value appear frequecntly 
    unsigned long d0 = readChannel0();
    unsigned long d1 = readChannel1();
    unsigned long d2 = readChannel2();
    unsigned long d3 = readChannel3();
    if(d0 != 268435455) data0 = d0;
    if(d1 != 268435455) data1 = d1;
    if(d2 != 268435455) data2 = d2;
    if(d3 != 268435455) data3 = d3;

    Serial.print("Channel 0: "); Serial.println(data0);
    Serial.print("Channel 1: "); Serial.println(data1);
    Serial.print("Channel 2: "); Serial.println(data2);
    Serial.print("Channel 3: "); Serial.println(data3);
    Serial.println();
}
//function for ploting raw data
void plotRawData()
{
    unsigned long p0 = readChannel0(); 
    if(p0 != 268435455) data0 = p0; 
    unsigned long p1 = readChannel1(); 
    if(p1 != 268435455) data1 = p1; 
    unsigned long p2 = readChannel2(); 
    if(p2 != 268435455) data2 = p2; 
    unsigned long p3 = readChannel0(); 
    if(p3 != 268435455) data3 = p3; 
    Serial.println(data1); 
}
void MATLABplotData()
{
  unsigned long p0 = readChannel0();
  if (p0 != 268435455) data0 = p0;
  unsigned long p1 = readChannel1();
  if (p1 != 268435455) data1 = p1;
  unsigned long p2 = readChannel2();
  if (p2 != 268435455) data2 = p2;
  // Send all three channels separated by commas
  Serial.print(data0);
  Serial.print(",");
  Serial.print(data1);
  Serial.print(",");
  Serial.println(data2);
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