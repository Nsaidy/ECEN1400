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
#for debugging - a set series of responses to the text messages

sequence1 = ["PROCEED", "y", "y"]
sequence2 = ["PROCEED", "y", "n"]
sequence3 = ["PROCEED", "n", "y"]
sequence4 = ["PROCEED", "n", "n"]
sequence5 = ["NOTHING"]

def test(sequence):
    response = Responder()
    print(response.currentMessage)
    for command in sequence:
        print(command)
        print("")
        response.findResponse(command)
        print(response.currentMessage)
    response = Responder()

print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("")
print("**************************************************")
print("")
test(sequence1)
print("")
print("**************************************************")
print("")
test(sequence2)
print("")
print("**************************************************")
print("")
test(sequence3)
print("")
print("**************************************************")
print("")
test(sequence4)
print("")
print("**************************************************")
print("")
test(sequence5)
print("")
print("**************************************************")
print("")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")



