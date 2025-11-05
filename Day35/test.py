
from twilio.rest import Client



#account_sid = "<ACCOUNT_SID>"
#auth_token = "<AUTH_TOKEN>"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello",
    from_="whatsapp:+14155238886",
    to="whatsapp:+16145585761"
)
print(message.status)