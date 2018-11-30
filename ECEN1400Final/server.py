import json
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

#open json file for responses
with open("messages.json") as json_content:
    responses = json.load(json_content)


#start an app
app = Flask(__name__)

# this is the starting message, it is set to default if messages is wrong
messageDefault = "I'm sorry, please enter a valid command"

# because findresponse relies on both the message being sent and the recieved message
# if will have a default which is the first message to be sent
currentResponse = data['intro']

#manages post request w/ http
@app.route("/sms", methods=['GET', 'POST'])



#replies to the message
def sms_reply():
    resp = MessagingResponse()
    message_body = request.form['Body']
    print(message_body)


    resp.message("Hi there, this is my response")
    return str(resp)


#finds the correct response and course of action
def findResponse(input):
    if(input == "PROCEED"):
        currentMessage = data['pictures?']
        #function turn on arduino
    else if(input == "NOTHING"):
        #abort
    else if(input == "y" and currentMessage == data['pictures?']):
        currentMessage = data['policeactivecamera?']
        #activate camera
    else if(input == "y" and currentMessage == data['policeactivecamera?'])
        currentMessage = data['police']
        #call police function
        #abort
    else if(input == "n" and currentMessage == data['policeactivecamera?'])
        currentMessage = data['nopolicecamera']
        #call police function
        #abort
    else if(input == "n" and currentMessage == data['pictures?']):
        currentMessage = data['policenoactivecamera?']
    else if(input == "y" and currentMessage == data['policenoactivecamera?'])
        currentMessage = data['police']
        #call police
        #abort
    else if(input == "n" and currentMessage == data['policenoactivecamera?']):
        currentMessage = data['nopolicenocamera']
        #abort
    else
        #send text with defaultMessage





if __name__ == "__main__":
    app.run(debug=True)


