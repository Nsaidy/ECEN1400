import os


from twilio.rest import Client


account_sid = "AC05303a6c1508f0ac96a3e547fbf76e67"
auth_token = "37da334b83f43c19617db3fb4346a1e8"
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