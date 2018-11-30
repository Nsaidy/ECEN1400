### ECEN1400

## Progress
Current code - send and recieve works with python, the automated convo is not perfect yet, trying to make it object oriented


## How to use this app
This app can be used on a public website, however, we used ngrok to tunnel to our own local host ports

For the future, this would be running on a public website

If you just download the code, it will not work. This is because the app runs using my own twilio 
token and sid. I have stored these as variables in my computer for sake of privacy, so you will need
to configure credentials.py

Also, the server being run on my twilio account is different than the default. If you have a twilio account
you must replace the URI under webhook recieving sms with the URL that ngrok provides (https://kasjdfne.io)
and then add your /sms because server.py initiates a post request, so the URL is
https://oandfkjs.io/sms
(where kasjdfs and ojweofibek are the strings provided by ngrok)
server.py defaults to port 5000, so /localhost:5000 => ngrok url

# install packages and other stuff:
install latest version of pip and make sure pip is part of environmental variables path

    $ pip i twilio
    $ pip i flask
    
    (if you chose to use the javascript code, you'll have to install:
    
    $ node i twilio
    $ node i express

install ngrok here: https://ngrok.com/download
extract the ngrok zip file and make sure it is in some place accessible to your path in environmental variables
ngrok is used to make a local host webpage (only visible to your machine) be publicly accessible

# setup your server 
(normally, this would already be published, but we don't own a domain name so we will use ngrok)
server.py sets up your webhook, allowing http requests to be made from your device and go through a server
and back to the client

server.js uses the modules http, express and twilio
it then sets up the server to be run on port 1337

Run the code

    $[location of server.py]python server.py
    [in a seperate terminal]
    $ngrok http 5000
    
    $[location to server.js] node server.js
    [in a seperate terminal]
    $ngrok http 1337
    
your webhook is now set up and you should be able to send and recieve text messages
