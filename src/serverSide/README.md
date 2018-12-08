# ServerSide



### Debugmessage.py
This program can be run in your terminal. It prints out all of the possible sequences of server.py class findRespons method.


### sendmessages.py
Not  utilized as much in our code, but for the future, this contains a class that sends a text message to a client


### messages.json
Contains all of the messages used in the text dialog. For the future, we would like to use dialogflow, the google API, to make a better user experience.


### server.py
The bulk of the program. Sets up a local server on port 5000 (debug mode is on so you can make changes and directly refresh the page). It also sends serial commands to the arduino to switch the mode




### templates
Contains (only 1 for now) templates for the webapp. This way, we can use jinja2 to embed data onto the html template
