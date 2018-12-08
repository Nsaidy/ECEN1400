import json
import serial, time, csv, decimal
from server import ser
with open("messages.json") as json_content:
    data = json.load(json_content)


messageDefault = "I'm sorry, please enter a valid command"

#Arduino motion and camera, arduino will take info from camera class
class ArduinoCamera:
    def __init__(self, status):
        self.status = status

#program gets data from arduinomotion and status will be controlled by user innerface (arm = status true)
class ArduinoMotion:
    def __init__(self, status, motionDetect):
        self.status = status
        self.motionDetect = motionDetect


camera = ArduinoCamera(False)

#will have to change later
motion =  ArduinoMotion(True, False)



class Responder:
    def __init__(self):
        self.currentMessage = data['intro']
        ser.write(b'DS')
    

    def findResponse(self, input):
        if(input == "PROCEED"):
            self.currentMessage = data['pictures?']
            ser.write(b'AS')
            
        elif(input == "NOTHING"):
            self.currentMessage = data['exit']

        elif(input == "y" and self.currentMessage == data['pictures?']):
            self.currentMessage = data['policeactivecamera?']
            #activate camera
        elif(input == "y" and self.currentMessage == data['policeactivecamera?']):
            self.currentMessage = data['police']
            #call police function
            #abort
        elif(input == "n" and self.currentMessage == data['policeactivecamera?']):
            self.currentMessage = data['nopolicecamera']
            #call police function
            #abort
        elif(input == "n" and self.currentMessage == data['pictures?']):
            self.currentMessage = data['policenoactivecamera?']
        elif(input == "y" and self.currentMessage == data['policenoactivecamera?']):
            self.currentMessage = data['police']
            #call police
            #abort
        elif(input == "n" and self.currentMessage == data['policenoactivecamera?']):
            self.currentMessage = data['nopolicenocamera']
            #abort

    
        #send text with defaultMessage

