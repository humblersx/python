
from twilio.rest import Client



account_sid = "ACf54e34e90fd4a4f6a492b6ef474a4f2b"
auth_token = "048afe528e9a4743debe8ab6b24b6494"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello",
    from_="whatsapp:+14155238886",
    to="whatsapp:+16145585761"
)
print(message.status)