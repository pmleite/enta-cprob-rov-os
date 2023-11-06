#include <DFRobot_PH.h>
#include <DFRobot_EC10.h>
#include <EEPROM.h>

#include "./arduino_cfg/config.h"
#include "./arduino_sense/sense.h"
#include "./arduino_actuate/actuate.h"

void setup() {
  Serial.begin(BAUD_RATE);
  BOARD_FUNCTION == 'S' ? sensor_setup() : actuator_setup();
}

void loop() {
  BOARD_FUNCTION == 'S' ? read_sensors() : actuate_devices();
}
