# import mailjet wrapper
from mailjet_rest import Client
import os
import time

# Get you environment mailet keys
api_key = '62ab7bb78295b072593fbf3c793118ca'
api_secret = '6a18f10c1dd466f55e8bf221b87e706f'

# Initialize Mailjet client
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

data = {
    'Globals' : {
        "From": {
			    "Email": "thomasbinaghi@gmail.com",
			    "Name": "wsAlpha - Your Portfolio's Newsletter"
		}
    },
    'Messages': [
	    {
		    "To": [
				{
					"Email": "thomasbinaghi@gmail.com",
					"Name": "Thomas"
				}
			],
            "Variables" : {
                "Name" : "Thomas"
            },
			"Subject": "Your email flight plan!",
			"TextPart": "  ",
			"HTMLPart": "<h3>Dear Thomas, welcome to <a href=\"https://ignaciobinaghi.github.io/wsAlpha/index.html\">wsAlpha</a>!</h3><br />Custom Stuff Here"
		},
		{
		    "To": [
				{
					"Email": "binaghiignacio@gmail.com",
					"Name": "Nacho"
				}
			],
            "Variables" : {
                "Name" : "Nacho"
            },
            # "Template ID" : 1
            # "Template Language" : True
            # Subject
			"Subject": "Hello!",
			"TextPart": "  ",
			"HTMLPart": "<h3>Dear Nacho, welcome to <a href=\"https://ignaciobinaghi.github.io/wsAlpha/index.html\">wsAlpha</a>!<br />Custom Stuff Here"
		}
	]
}

result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())

while True:
	result = mailjet.send.create(data=data)
	time.sleep(86400)