// GENERIC CONFIGURATIONS
#define BAUD_RATE                  19200
#define BOARD_FUNCTION             'S' // 'S' (sensing board) or 'A' (actuator board) 

// SENSOR PINS
#define INTERNAL_TEMP_SENSOR_PIN    A0
#define EXTERNAL_TEMP_SENSOR_PIN    A1
#define HUMIDITY_SENSOR_PIN         A2
#define PH_SENSOR_PIN               A3
#define EC_SENSOR_PIN               A4
#define ULTRA_SONIC_SENSOR_PIN      A5

// ACTUATOR PINS
#define LIGHT_PIN                   4
#define FAN_PIN                     5
#define PROP_LEFT_MOTOR             6
#define PROP_RIGTH_RIGTH            7
#define VER_FRONT_LEFT_MOTOR        8
#define VER_FRONT_RIGHT_MOTOR       9
#define VER_BACK_LEFT_MOTOR         10
#define VER_BACK_RIGHT_MOTOR        11

void sensor_setup(){
    pinMode(INTERNAL_TEMP_SENSOR_PIN, INPUT);
    pinMode(EXTERNAL_TEMP_SENSOR_PIN, INPUT);
    pinMode(HUMIDITY_SENSOR_PIN, INPUT);
    pinMode(PH_SENSOR_PIN, INPUT);
    pinMode(EC_SENSOR_PIN, INPUT);
    pinMode(ULTRA_SONIC_SENSOR_PIN, INPUT);
}

void actuator_setup(){
    pinMode(LIGHT_PIN, OUTPUT);
    pinMode(FAN_PIN, OUTPUT);
    pinMode(PROP_LEFT_MOTOR, OUTPUT);
    pinMode(PROP_RIGTH_RIGTH, OUTPUT);
    pinMode(VER_FRONT_LEFT_MOTOR, OUTPUT);
    pinMode(VER_FRONT_RIGHT_MOTOR, OUTPUT);
    pinMode(VER_BACK_LEFT_MOTOR, OUTPUT);
    pinMode(VER_BACK_RIGHT_MOTOR, OUTPUT);
}


