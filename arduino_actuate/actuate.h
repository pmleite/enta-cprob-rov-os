/**
 * @brief Receive data from the raspberyPi and actuate devices 
 */
void actuate_devices(){
  //Read data from the serial port
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print("RCV:");
    Serial.println(data);
  }
}
