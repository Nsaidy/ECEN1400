import json

with open("messages.json") as json_content:
    data = json.load(json_content)

messageDefault = "I'm sorry, please enter a valid command"

class Responder:
    def __init__(self):
        self.currentMessage = data['intro']
    
    

    def findResponse(self, input):
        if(input == "PROCEED"):
            self.currentMessage = data['pictures?']

            #function turn on arduino
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

response = Responder()
