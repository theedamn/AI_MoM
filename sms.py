from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from main import *
from twilio.rest import Client
import os
app = Flask(__name__)

#Use ngrok to port this to the twilio website to receive sms

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    body=request.form['Body']
    From=request.form['From']
    print(body)
    # Start our TwiML response
    resp = MessagingResponse()    
    
    responsebot=on_message(body)

    # This will send reply message
    resp.message(str(responsebot))
    print(resp)
    account_sid = os.environ['acc_ssid']
    auth_token = os.environ['auth_token']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_=os.environ['my_num'],
    to='your number',
    body=str(resp)
    )
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

