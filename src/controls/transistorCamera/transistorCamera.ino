
#include <Servo.h>
boolean trigger = false;
float pos = 0;


int valSlot0 = 0; 
int valSlot1 = 0;
int valSlot2 = 0;
int valSlot3 = 0;
int valSlot4 = 0;
int val = 0;
int count = 0;

Servo myservo;  // create servo object to control a servo

void setup() {
  
  //The system runs at 9600 but most  rates should work all data is sent over serial
  Serial.begin(9600);
  
  pinMode(A0, INPUT);
  
  pinMode(A1, INPUT);
  
  pinMode(A2, INPUT);
  
  pinMode(A3, INPUT);
  
  pinMode(A4, INPUT);
  
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  
//7 and 8 are camera in and outs
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);

}


//a is the status of the camera, DSDC ASAC ASDC
String a;

void loop() {
  digitalWrite(7, LOW);
  digitalWrite(8, HIGH);


  
  if(Serial.available()){
    a = Serial.readString();
  }
  

  //Active system deactive camera
  if(a == "ASDC"){
    commandMotionSensors();
  }
  
  //Active system active camera
  else if(a == "ASAC"){
    commandMotionSensors();
    digitalWrite(8, LOW);
    Serial.print("akdjfndf");
  }


  Serial.println(a);
  
  //turn the camera off no matter what
  //put it here to leave a slight gap just in case

  myservo.write(98);
}



//loops through the sensors and finds which ones are on to add their specified value to val
void commandMotionSensors(){
  if(valSlot0 == 1 || valSlot1 == 1 || valSlot2 == 1 || valSlot3 == 1 || valSlot4 == 1){
  trigger = true;
}
  
  val = 0;
  count = 0;

//if all equal zero val gets halfway
  if(digitalRead(A0) == 0 && digitalRead(A1) == 0 && digitalRead(A2) == 0 && digitalRead(A3) == 0 && digitalRead(A5) == 0){
    val+= 98;
    count++;
    
  }
  if(digitalRead(A0) == 1){
    val+= 40;
    count++;
    
  }
  if(digitalRead(A1) == 1){
    val+= 60;
    count++;
    
  }
  if(digitalRead(A2) == 1){
    val+= 108;
    count++;
    
  }
  if(digitalRead(A3) == 1){
    val+= 180;
    count++;
    
  }
  if(digitalRead(A4) == 1){
    val+= 220;
    count++;
    
  }

  val = val / count;
  myservo.write(val);
  
}
