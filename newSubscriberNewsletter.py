"""
Create a new subscriber contact:
"""
from mailjet_rest import Client
import os
import pprint

api_key = '62ab7bb78295b072593fbf3c793118ca'
api_secret = '6a18f10c1dd466f55e8bf221b87e706f'

mailjet = Client(auth=(api_key, api_secret))

data_basic = {
    "Email" : email
}

data_newsletter_list = {
    "ContactAlt" : email,
    "ListID" : "26947"
}

# create a contact and all to "all contacts"
result = mailjet.contact.create(data=data_basic)

# create a contact and add to the Newsletter Contacts List
result = mailjet.listrecipient.create(data=data_newsletter_list)

print(result.status_code)
pprint.pprint(result.json())