#include "./arduino_sense/sense.h"
#include "./arduino_actuate/actuate.h"
#include "./arduino_cfg/config.h"

void setup() {
  Serial.begin(BAUD_RATE);
}

void loop() {

  if(BOARD_FUNCTION == 'S'){
    sense();
  }
  else if(BOARD_FUNCTION == 'A'){
    actuate();
  }
  else{
    Serial.println("ERROR: BOARD_FUNCTION not defined");
  }
}
