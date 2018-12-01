#include <Servo.h>


//an array of all voltage values to be sent at the cooresponding indexed pin in pirpins
int pos[] = {40, 60, 108, 150, 180};

//an array of all the pirPins
int pirPins[] = {0, 1, 2, 3, 4};

//true is right and false is  left, doing this so that sensors don't  backtrack unless they have to reducing jerkiness
//direction will only change if directionChanger == 2
boolean direction = true;
int directionChanger = 0;
int voltage;

Servo myservo;  // create servo object to control a servo


//all pirpins inputs (digital) servo pin output
void setup() {
  // attaches the servo on pin 9 to the servo object
  myservo.attach(9);  

  // sets all pir pins to inputs (will be digital)
  pinMode(pirPins[0], INPUT);
  pinMode(pirPins[1], INPUT);
  pinMode(pirPins[2], INPUT);
  pinMode(pirPins[3], INPUT);
  pinMode(pirPins[4], INPUT);

 

  
}

void loop() {
  //value is the final value to be sent to the motor
  int value = 0;

  //for calculating the average of all the sensors that are on
  int count = 0;

  //version 1, sums all the voltages of pir sensors that are on and finds median
  for(int i = 0; i < sizeof(pirPins); i++){
    if(digitalRead(pirPins[i]) == 1){
      value = value + pos[i];
      count++;
    }
  }

  value = value / count;

  if ((value < voltage && direction) || (value > voltage && !direction)){
    directionChanger++;
  }else{
    myservo.write(value);
  }
  
  if(directionChanger == 2){
    direction = !direction;
  }
  voltage = value;
  
}
