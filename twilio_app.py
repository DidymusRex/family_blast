from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    sms_keys=['MessageSid', 'AccountSid', "MessagingServiceSid", "From", "To", "Body", "NumMedia", "FromCity", "FromState", "FromZip", "FromCountry", "ToCity", "ToState", "ToZip", "ToCountry" ]

    known_numbers=["+12693260515"]

    r = request.values
    rk = sorted(request.values.keys())
    f = r["From"]
    b =  r["Body"]

    print("Processing sms")
    print("Received text \"{}\" from {}".format(b, f))

    for k in rk:
        if r[k] != None:
            print("key: {} -> value: {}".format(k, r[k])) 

    m = "Foo"
    if f in known_numbers:
        m = "Hello, friend!"
    else:
        m = "Stranger danger! in {}, {}".format(r["FromCity"], r["FromState"])

    # Add a message
    print("Sending reply \"{}\" to {}".format(m, f))

    # Start our response
    resp = MessagingResponse()
    resp.message(m)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
