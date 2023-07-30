from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from main import *
app = Flask(__name__)

#Use ngrok to port this to the twilio website to receive sms

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()    
    
    responsebot=on_message(['hi mom'])

    # This will send reply message
    resp.message(str(responsebot))
    
    print(resp)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

