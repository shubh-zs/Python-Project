from __future__ import print_function
from telesign.messaging import MessagingClient

customer_id = "0FB1307C-B088-4490-B45D-B62ED8AAD289"
api_key = "6gBmrjj24hSeX6pkQ4D03VwYn0eqqrIrr9riS7P3ib7oFvPFYOmwx+qe5Bjyi2MiDr5kTATGJA/0jRdK7zOWJA=="

p1 = "+919582566693"
message = "Hello"
message_type = "ARN"

messaging = MessagingClient(customer_id, api_key)
response = messaging.message(p1, message, message_type)
print("done")