#include <Wire.h>
#include "DFRobot_PH.h"
#include "DFRobot_EC10.h"

#define SLAVE_ADDRESS   0x04
#define TEMP_PIN        A0
#define EC_SENSOR_PIN   A1
#define PH_SENSOR_PIN   A2
#define MPU             0x68



#define SONAR_1_TRIGPIN 11
#define SONAR_1_ECHOPIN 10
#define SONAR_2_TRIGPIN 9
#define SONAR_2_ECHOPIN 8

float   waterTemp = 25.0;
float   voltageEC, valueEC;
float   voltagePH, valuePH;
float   sonar1Distance, sonar1Duration; 
float   sonar2Distance, sonar2Duration;
float   gyroX, gyroY, GyroZ;
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;


DFRobot_PH ph;
DFRobot_EC10 ec;

void setup() {
  
  Wire.begin(SLAVE_ADDRESS);  // Initialize I2C as slave
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  pinMode(TEMP_PIN, INPUT);
  pinMode(EC_SENSOR_PIN, INPUT);
  pinMode(PH_SENSOR_PIN, INPUT);
  pinMode(SONAR_1_TRIGPIN, OUTPUT);
  pinMode(SONAR_1_ECHOPIN, INPUT);
  pinMode(SONAR_2_TRIGPIN, OUTPUT);
  pinMode(SONAR_2_ECHOPIN, INPUT);

  Serial.begin(115200);  // Initialize serial communication for debugging
}

void loop() {
  updateWaterTempVal();
  updatePHVal();
  updateECVal();
  updateSonar1Val();
  updateSonar2Val();
  delay(50);
}

float updateWaterTempVal(){
  int analogValue = analogRead(TEMP_PIN);
  float voltage = analogValue * (5.0 / 1023.0);
  float temperatureC = voltage * 100.0;  // LM35: 10mV per degree Celsius

  String tempString = "001:"+String(temperatureC);
  Wire.write(tempString.c_str());

  return temperatureC;
}

void updatePHVal(){
    static unsigned long PHtimepoint = millis();
    if(millis()-PHtimepoint>1000U)  //time interval: 1s
    {
      PHtimepoint = millis();
      waterTemp   = updateWaterTempVal();                   
      voltagePH   = analogRead(PH_SENSOR_PIN)/1024.0*5000;  
      valuePH     = ph.readPH(voltagePH, waterTemp);        
    }
    ph.calibration(voltagePH,waterTemp);  

    String phString = "002:"+String(valuePH);
    Wire.write(phString.c_str());              
}

void updateECVal(){
    static unsigned long ECtimepoint = millis();
    if(millis()-ECtimepoint>1000U)  //time interval: 1s
    {
      ECtimepoint = millis();
      waterTemp   = updateWaterTempVal();                    
      voltageEC   = analogRead(EC_SENSOR_PIN)/1024.0*5000;   
      valueEC     = ec.readEC(voltageEC, waterTemp);        
    }
    ec.calibration(voltageEC,waterTemp);  

    String ecString = "003:"+String(valueEC);
    Wire.write(ecString.c_str());                 
}

void updateSonar1Val(){
    digitalWrite(SONAR_1_TRIGPIN, LOW);
    delayMicroseconds(2);
    digitalWrite(SONAR_1_TRIGPIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(SONAR_1_TRIGPIN, LOW);
    sonar1Duration = pulseIn(SONAR_1_ECHOPIN, HIGH);
    sonar1Distance = (sonar1Duration/2) / 29.1;

    String sonar1String = "004:"+String(sonar1Distance);
    Wire.write(sonar1String.c_str());                 
}

void updateSonar2Val(){
    digitalWrite(SONAR_2_TRIGPIN, LOW);
    delayMicroseconds(2);
    digitalWrite(SONAR_2_TRIGPIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(SONAR_2_TRIGPIN, LOW);
    sonar2Duration = pulseIn(SONAR_2_ECHOPIN, HIGH);
    sonar2Distance = (sonar2Duration/2) / 29.1;

    String sonar2String = "005:"+String(sonar2Distance);
    Wire.write(sonar2String.c_str());                 
}


void sendData() {
  Wire.write("OK");  
}

void receiveData(int byteCount) {
  while (Wire.available()) {
    char c = Wire.read();
    Serial.print(c);
  }
  Serial.println();
}