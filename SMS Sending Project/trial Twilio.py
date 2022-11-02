import twilio
from twilio.rest import Client

account_sid = 'ACd67b000c9520816c5486e1054e483a25'
auth_token = '7f814686097375cb794d9d696012d2b6'
client = Client(account_sid, auth_token)

numbers_to_message = ['+919810721539']
for number in numbers_to_message:
    message = client.messages.create(
        body = 'Namaste Shubh here, \n You can send any type of msgs like for our grocery company if we buy this subscription from the Api ',
        from_ = "+19285890408",
        to = number
    )

print(message.sid)

