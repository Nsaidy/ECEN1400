import os


from twilio.rest import Client


#my key and sid
my_twilio = "17207073308"
my_cell = "13034781391"



class PhoneAccount:
    

    def __init__(self, account, token, number):
        self.account_sid = account
        self.auth_token = token
        self.number = number
        self.client = Client(account_sid, auth_token)

    def sendMessage(self, _message, recipient):
        message = self.client.messages \
                    .create(
                        body = _message,
                        from_ = self.number,
                        to = recipient
                    )
        print('Message sent from' , self.number , ' to ' , recipient , '. Content: ' , _message)


myAccount = PhoneAccount(account_sid, auth_token, my_twilio)
