### ECEN1400

##Structure
I used python virtual environment to make this. So that is what pyenv.cfg is. all the necessary packages are installed

## How to use this app
This app assumes you have a local computer running a public server. As of now, it does not upload serial data to a website so it cannot be used with a server like firebase or azure. This is an easy fix, just allow the server of your choice access to usb data. We didn't do this because  in the future we would like to use a webhook based framework like Autobahn.

To start the bot, you need to plug in the arduino to the processor. Make  sure you know which usb it is connected to. For pis, this is /dev/ttyUSB# where # is the number of the usb (this is all down to your computer) you can change this directly in server.py.

To continue, if you haven't already done so, upload transistorcamera.ino to the arduino (you need Arduino IDE to do this). Once the arduino is set up, all you have to do is run server.py. This will set up a local website on port 5000 (/localhost:5000) you need to make this public. I did this using ngrok. Merely run the command
	$ ngrok http 5000
This will list an http and https url. This URL is your home page of the app (index.html). Right now, the website will be running fine. You can turn on or off the camera at will on the temporary site. However, to get sms functionality, you'll notice there is a /sms/ POST request on server.py. This is the url you need to supply  to twilio. Once you changed account sid and account key in server.py, you need to change twilio's default webhook sms url to the https://#######.ngrok.io/sms usrl that ngrok supplied (or another url if you are using a different application). IMPORTANT, add /sms to the end of the url. /sms/ is  the webapp  that processes the information and sends the user back a text.

## Required packages
I installed all of my packages in a virtual python environment, but you don't need to do this. you will need to install flask and twilio. Of course, flask is the python microframework. If you chose to switch to a different language (particularly javascript), you must install you're prefered framework. We could have used any framework like Django or Autobahn, but flask was good for microframeworks like our own.

## Troubleshooting
A common problem comes from serial connection between the arduino and the processor. Make sure your usb is correct in server.py (for linux and mac its /dev/tty#, for windows it's COM#). Also make sure your usb serial communication is right. Sometimes if you somehow send serial data over arduino at the start (this shouldn't  be the case because when the arduino is first initiated, it is passive) it is difficult to start server.py because python attempts to make a serial connection while the serial is in use. For best results, upload your code on Arduino and immediately afterwards run server.py. 

The camera is a very tricky part of the code primarily because it is not a native camera. We would like to switch to a more controlled camera (unfortunately we did not have the funding). Generally the camera will work in our current code transistorcamera.ino. However, in transistorcamera.ino, pins 7 and 8 essentially provide a square wave at the same frequency as the main control loop. To make this better, you could control the camera with an external clock (get a very very low frequency that switches the camera on and off). 


## Problems / future
Right now, there are a lot of small problems. These are mainly  from an experienced software developer's point of view. We would like to make this website completely public. To do this, we would need account information so that everyone isn't running the same camera. We just started changing our code  to an object oriented design, however, the OO nature could be worked with.

## Arduino pins
This project assumes a two line camera, that is only two wires are used for the camera, they are hooked up across the switch so that if one is high and the other is low, the camera is passive, but when they are both low  or high, the camera takes a picture. Of  course in the future, we would use a serial camera such as the OV760, but the arduino would need an external timer to impliment this.
Pin A0 --> Motionsensor output1
Pin A1 --> Motionsensor output2
Pin A2 --> Motionsensor output3
Pin A3 --> Motionsensor output4
Pin A4 --> Motionsensor output5
Pin 7 --> Camera high switch output (unfortunately the only way to find this is by trial and error)
Pin 8 --> Camera low switch output
Pin 9~ --> Servo motor
Pin 5v --> All components
Pin GND --> All Components
Each motion sensor is hooked up to a 880 k Ohm resistor from high potential to low.


## Notes
This was a project for the class ECEN1400 at CU Boulder. If you have any questions, contact Maxwell Pettit, Noah Saidy or Theo Lincke (all contributers to this repository). Please, enjoy playing around with the code as much as we did and we sincerly hope everything works as planned.

