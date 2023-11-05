#include "sense.h"
#include "actuate.h"

char BOARD_FUNCTION = 'S';  //S - Sensing Board, A - Actuating Board

void setup() {
  //Initialize the board
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


