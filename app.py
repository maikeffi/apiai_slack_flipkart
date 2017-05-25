import os
import json
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):

    if req.get("result").get("action") != "getFlipkartCat":
        return {            "text": "Work in progress."        }

    res = makeWebhookResult()
    return res

def makeWebhookResult():

    print("Response:")

    speech = "Flipkart Categories"
    slack_message = {
        "text": "Which Category are you looking for?",
        "response_type": "in_channel",
        "attachments": [
            {
                "text": "Choose a Category",
                "fallback": "If you could read this message, you'd be choosing something fun to do right now.",
                "color": "#3AA3E3",
                "attachment_type": "default",
                "callback_id": "category_selection",
                "actions": [
                    {
                        "name": "category_list",
                        "text": "Pick a Category...",
                        "type": "select",
                        "options": [
                            {
                                "text": "Laptops",
                                "value": "laptops"
                            },
                            {
                                "text": "Tablets",
                                "value": "tablets"
                            },
                            {
                                "text": "Desktops",
                                "value": "desktops"
                            },
                            {
                                "text": "Computer Storage",
                                "value": "computer_storage"
                            },
                            {
                                "text": "Computer Components",
                                "value": "computer_components"
                            },
                            {
                                "text": "Laptop Accessories",
                                "value": "laptop_accessories"
                            },
                            {
                                "text": "Computer Peripherals",
                                "value": "computer_peripherals"
                            }
                        ]
                    }
                ]
            }
        ]
    }

    print(json.dumps(slack_message))

    return {
        "speech": speech,
        "displayText": speech,
        "data": {"slack": slack_message},
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print( "Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')

