from twilio import rest

#Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC4193cd66ec52de5d2789ea288a3c2348"
auth_token = "c3ee75b4b284e13dd2ba42df321792c9"
client = rest.TwilioRestClient (account_sid, auth_token)

message = client.sms.messages.create(
        body="Hello from Twilio",
        to="+19162912374",
        from_="+14152869043")

print message.sid

