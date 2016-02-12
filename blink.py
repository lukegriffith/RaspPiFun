import RPi.GPIO as GPIO;
import time;


pinRed = 6;
pinYellow = 12;

GPIO.setmode(GPIO.BCM);
GPIO.setup(pinRed,GPIO.OUT);
GPIO.setup(pinYellow,GPIO.OUT);

run = 0;

while True:
  GPIO.output(pinRed,GPIO.HIGH);
  GPIO.output(pinYellow,GPIO.LOW);
  time.sleep(0.5);
  GPIO.output(pinRed,GPIO.LOW);
  GPIO.output(pinYellow,GPIO.HIGH);
  time.sleep(0.5);
  print(run);
  run += 1;
  
