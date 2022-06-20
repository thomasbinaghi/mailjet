"""
Create a new subscriber contact:
"""
from mailjet_rest import Client
import os
import pprint

api_key = '62ab7bb78295b072593fbf3c793118ca'
api_secret = '6a18f10c1dd466f55e8bf221b87e706f'

mailjet = Client(auth=(api_key, api_secret))

email = "thomasbinaghi@gmail.com"
listID = '26947'

data_basic = {
    "Email" : email
}

data_newsletter_list = {
    "ContactAlt" : email,
    "ListID" : listID
}

# create a contact and all to "all contacts"
resultAll = mailjet.contact.create(data=data_basic)
# print(resultAll.status_code)
# print(resultAll.json())

# create a contact and add to the Newsletter Contacts List
resultSub = mailjet.listrecipient.create(data=data_newsletter_list)
# print(resultSub.status_code)
# print(resultSub.json())

## force subcribe if in list already but not subcribed
if resultSub.json()['ErrorMessage'] == 'A duplicate ListRecipient already exists.':
    data = {
        'Action': "addforce",
        'Contacts': [
          {
            "Email": email,
          }
        ]
    }
    result = mailjet.contactslist_managemanycontacts.create(id=listID, data=data)