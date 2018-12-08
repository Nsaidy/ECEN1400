

import serial, time, csv, decimal

import json
from flask import Flask, request, redirect, render_template
from twilio.twiml.messaging_response import MessagingResponse

from sendmessages import PhoneAccount, myAccount
from twilio.rest import Client


#Authenticate Information These are blank because they are private

my_twilio = "17207073308"
my_cell = "13034781391"



#open json file for responses
with open("messages.json") as json_content:
    data = json.load(json_content)




#Connect to serial
port = '/dev/ttyUSB0'
ser = serial.Serial(port , baudrate=9600, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=2)



#start an app
app = Flask(__name__)

_status = "Deactivated"
_htmlstatus = False





#Responder deals with what response to send
class Responder:
    def __init__(self):
        self.currentMessage = data['intro']
        htmlstatus = False
        ser.write(b"DSDC")

    def findResponse(self, input):


        #future versions would impliment google dialogflow
        if(input == "PROCEED"):
            self.currentMessage = data['pictures?']
            ser.write(b"ASDC")
            _status = "Active with no Camera"
            htmlstatus = True
            
        elif(input == "NOTHING"):
            self.currentMessage = data['exit']
            ser.write(b"DSDC")
            _status = "Deactivated"
            htmlstatus = False

        elif(input == "y" and self.currentMessage == data['pictures?']):
            self.currentMessage = data['policeactivecamera?']
            ser.write(b"ASAC")
            _status = "Activated with Camera"
            htmlstatus = True

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




    #the commands for setting the system and the camera are not efficient
    #sends a signal over serial and arduino reads this. I have made
    #these methods so that they can easily be changed and still called in 
    #findresponse
    def setSystem():
        ser.write(b"ASDC")
    
    def setCamera():
        ser.write(b"ASAC")

    def deactivate():
        ser.write("DSDC")


    

    


    
        #send text with defaultMessage

#initialize a responder
response = Responder()


@app.route('/')
@app.route('/index')
def index():
    _status = "Deactive"
    return render_template("index.html", status=_status, htmlstatus = False)


@app.route('/turnonsystem/', methods=["POST"])
def turnOnSystem():
    ser.write(b"ASDC")
    _status = "Active with no Camera"
    _htmlstatus = True
    return render_template("index.html", status=_status, htmlstatus = _htmlstatus)


@app.route('/turnoncamera/', methods=["POST"])
def turnOnCamera():
    ser.write(b"ASAC")
    _status = "Activated with Camera"
    _htmlstatus = True
    return render_template("index.html", status = _status, htmlstatus=_htmlstatus)


@app.route('/turnoffsystem/', methods=["POST"])
def turnOffSystem():
    ser.write(b"DSDC")
    _status = "Deactivated"
    return render_template("index.html", status = _status)








#manages post request w/ http
@app.route("/sms", methods=['GET', 'POST'])
#replies to the message
def sms_reply():
    
    resp = MessagingResponse()
    message_body = request.form['Body']
    


    if(message_body == "RESET"):
        resp.message("Resetting")
        response.currentMessage = data['intro']
        ser.write(b'DS')

    else:
        response.findResponse(message_body)
        resp.message(response.currentMessage)

   # messages.append(messageOutIn(message_body, response.currentMessage))
    
    return str(resp)












#Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)


