# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from http://twilio.com/user/account
account_sid = "Dont worry"
auth_token = "Nothing to see here"
client = TwilioRestClient(account_sid, auth_token)
room_number = 0

states = ['+14846854944', '+14159686840']


def setUpCall(from_state, numbers, room):
    if len(numbers) < 2 or not 0 <= from_state < 2:
        print "error: not enough numbers for conference"
        return -1
    global client

    for num in numbers:
        #num = cleanUpNum(num)
        call = client.calls.create(to="+1" + num,
                                   from_=states[from_state],
                                   url="http://twimlets.com/conference?Name=" +
                                   room + "&Message=%20")

    return call.sid


def killCall(call_id):
    call = client.calls.update(call_id, status="completed")
    print call.start_time


def cleanUpNum(num):
    num = num.translate(None, '()-')
    return num


#nums = ["+19085287844", "+16107616189", "+17326681916", "+17324850325"]
# resources = client.calls.list()
