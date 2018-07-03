"""
use SendCloud API to send emails
"""
import requests
import json

# set your attachment path
file_path = "/Users/dangchong/Documents/Github/CodingTask/Code/event.csv"

url = "http://api.sendcloud.net/apiv2/mail/sendtemplate"
API_USER = 'junengpin_test_ZI48jr'
API_KEY = 'LNpJSbhsMGt6dgrv'


def send_email(name, email):
    x_smtpapi = {
        "to": [email],
        "sub": {
            "%name%": [name],
        }
    }

    params = {
        "apiUser": API_USER,
        "apiKey": API_KEY,
        "from": "rickydangc@yahoo.com",
        "fromName": "ChongDang",
        "subject": "Interview: CodingTask | Maplecroft |",
        "replyTo": "rickydangc@yahoo.com",
        "templateInvokeName": "test_template_send",
        "xsmtpapi": json.dumps(x_smtpapi),
        "useAddressList": "false",
        "respEmailId": "true",
        "embeddedCid": "event.csv",

    }

    # file path
    filename1 = file_path
    display_filename_1 = "event.csv"

    files = [
        ("embeddedImage", (display_filename_1, open(filename1, 'rb'), 'application/octet-stream'))
    ]

    try:
        r = requests.post(url, files=files, data=params)
    except requests.exceptions.HTTPError:
        raise

    return r.status_code == 200


# call send function, input your name and email address: send_email('name','email_address')
send_email('Sir', 'rickydangc@yahoo.com')
