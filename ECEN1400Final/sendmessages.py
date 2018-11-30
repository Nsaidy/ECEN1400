import os

from credentials import account_sid, auth_token, my_twilio, my_cell
from twilio.rest import Client


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
myAccount.sendMessage('hi there!', my_cell)
