//2 servos will be used

//SG90 servos pulse len: min =105~110, max =550~555
//6kg servo pulse len: min = 565~570, min = 100~95
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(); //Address of board 0x40

#define SG90MIN 110 // pulse len for ~ 0 degrees
#define SG90MAX 550 // pulse len for ~ 180 degrees
#define KGMIN 95 // pulse len for ~ 0 degrees
#define KGMAX 565 // pulse len for ~ 180 degrees

#define SERVO_FREQ 50 // servo frequency 

//First 3 channels of ServConrtoller for the grippers movement
uint8_t SGChannel1 = 0;
uint8_t SGChannel2 = 1;
uint8_t SGChannel3 = 2;

//2 Channels for the S1 and S2 joint
uint8_t KGChannel1 = 4;
uint8_t KGChannel2 = 5;

void setup() {
  Serial.begin(115200);
  pwm.begin(); // Starting I2C connection
  pwm.setPWMFreq(SERVO_FREQ);

  delay(10);

}
void loop()
{
    
}