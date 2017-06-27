
#include <Stepper.h>

const int stepsPerRevolution = 48;  // according to the specification of the stepper motor used

Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

int steps = 0;         // number of steps the motor has taken

void setup() 
{
  pinMode(8,1);
  pinMode(9,1);
  pinMode(10,1);
  pinMode(11,1);
  Serial.begin(9600);
}

void StepCount()
{
  if (steps<48)
  steps++;
  else if (steps==48)
  steps=0;
}

void StepperStep()
{
  if (Serial.available())
  {
    if (steps<48)
    {
      char data=Serial.read();
      if (data=='1') // The arduino is controlled using Pyserial Command from Python GUI Window using Keypress 1
      {
        myStepper.step(1);
        delay(50);
        Serial.print('.');
        StepCount();
      }  
    }
  }  
}


void loop() 
{
  StepperStep();
}

