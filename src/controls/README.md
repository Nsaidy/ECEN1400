# Controls

## transistorcamera.ino

Runs on the arduino (must open using arduino IDE). This code runs through checking the status of the serial every  time it goes through the loop.

### Serial = DSDC
Deactivate system deactivate camera

### Serial = ASDC
Activate system deactivate camera


### Serial = ASAC
Activate system activate camera


### commandmotionsensor
Runs through checking each sensor. If the sensor is active, it  adds the value that cooresponds to the servo's position at that sensor to value. At the end it averages value and writes it to servo
