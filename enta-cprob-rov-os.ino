#define BOARD_FUNCTION SENSE  //SENSE or ACTUATE


void setup(){
    Serial.begin(9600);
}

void loop(){
    Serial.println("Hello World");
    delay(1000);
}