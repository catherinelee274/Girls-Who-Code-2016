#include <Servo.h>

int leftwhisker_pin = 5;
int rightwhisker_pin = 7;

Servo servoRight;
Servo servoLeft;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(leftwhisker_pin, INPUT);
  pinMode(rightwhisker_pin, INPUT);
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);

}

void Backward() {
  Serial.println("I hit something.");
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
}
void Forward() {
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (digitalRead(leftwhisker_pin) == 0) {
    Backward();
    servoRight.writeMicroseconds(500);


  }
  else {
    Forward();
  }
  if (digitalRead(rightwhisker_pin) == 0) {
  Backward();
  servoLeft.writeMicroseconds(500);
  }
  else{
  Forward();
  }
}






