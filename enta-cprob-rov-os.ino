#include "./arduino_sense/sense.h"
#include "./arduino_actuate/actuate.h"

/**
 * @brief Define the board function
 *        S - Sensing Board
 *        A - Actuating Board 
 * 
 *        This is used to determine the board 
 *        function, to upload to the sensing board
 *        make sure to change the BOARD_FUNCTION to 
 *        'S' and to 'A' for the actuating board
 */
char BOARD_FUNCTION = 'A';  

void setup() {
  Serial.begin(19200);
}

void loop() {

  if(BOARD_FUNCTION == 'S'){
    sense();
  }
  else if(BOARD_FUNCTION == 'A'){
    actuate();
  }
  else{
    Serial.println("Error: Invalid Board Function");
  }
}
