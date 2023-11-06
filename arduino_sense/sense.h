/**
 * @brief Variables to store sensor values
 * 
 * @param waterTemp Water temperature
 * @param voltageEC Voltage of EC sensor
 * @param valueEC EC value
 * @param voltagePH Voltage of PH sensor
 * @param valuePH PH value
 * 
 */
float waterTemp = 25.0;
float voltageEC, valueEC;
float voltagePH, valuePH;


/**
 * @brief Send sensor values to Serial Port
 * 
 */
void sendSensorValues(){
  String ecString = String(valueEC) + "," + String(waterTemp) + "," + String(voltageEC);
  Serial.print("SENSE_EC:");
  Serial.println(ecString);
  String phString = String(valuePH) + "," + String(waterTemp) + "," + String(voltagePH);
  Serial.print("SENSE_PH:");
  Serial.println(phString);
}

/**
 * @brief Update water temperature value
 * 
 */
int updateWaterTempVal(){
    return 25;
}

/**
 * @brief Update ec value
 * 
 */
//TODO: Melhorar entrada em modo de clibração (Ver demo github DF_PH Library)
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
}

/**
 * @brief Update ph value
 * 
 */
//TODO: Melhorar entrada em modo de clibração (Ver demo github DF_PH Library)
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
}

/**
 * @brief Read all sensors and update values into variables
 * 
 */
void read_sensors(){
  updateECVal();
  updatePHVal();
  sendSensorValues();
}



    





