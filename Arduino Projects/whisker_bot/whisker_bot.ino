
#include <Servo.h>

Servo servoRight;
Servo servoLeft;

int piezo = 4;
int left= 5;
int right=7; 

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  pinMode (piezo, OUTPUT);
  pinMode (left, INPUT);
  pinMode (right, INPUT);
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds (1500);
  servoRight.writeMicroseconds (1500);
  
}

void backwards () {
  Serial.println ("I GOT HIT");
  servoLeft.writeMicroseconds (1300);
  servoRight.writeMicroseconds (1700);
   
   
}

void forward () {
  Serial.println ("LET'S GO");
  servoLeft.writeMicroseconds (1700);
  servoRight.writeMicroseconds (1300);
}


void loop() {
  // put your main code here, to run repeatedly:

  if (digitalRead (left) == 0) {
    backwards();
    servoRight.writeMicroseconds (1300);
    delay (1000);
    } 
  else if (digitalRead (right) == 0) {
    backwards ();
    servoLeft.writeMicroseconds (1700);
    delay (1000);
    }
   else if ((digitalRead (right)== 0) and (digitalRead (left)==0)) {
    backwards ();
    delay (1000);
   }
   else { 
    forward();
  }
}
 



