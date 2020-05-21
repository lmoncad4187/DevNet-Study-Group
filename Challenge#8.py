
import requests
import json


url = 'https://webexapis.com/v1/rooms'


headers = {
    'Authorization': 'Bearer ZDUzNDM3M2UtNTU2Mi00NjQ1LWEwZDUtMjQ4MTBlNTY0ZDU4YTMwODk5OWItZWY5_PF84_consumer',
    'Content-Type': 'application/json'
}


group_name = {
    'title': 'Lucas-DEVNET-TEST'
}

add_user = 'https://webexapis.com/v1/memberships'

#Create/name new room
requests.request('POST', url, data=json.dumps(group_name), headers=headers)

get_id = requests.request('GET', url, headers=headers)
format_json = get_id.json()
room_id = format_json['items'][0]['id']

#json format for group info
group_info = {
    'roomId': room_id,
    'personEmail': 'lucasmoncada@yahoo.com'
}

#Adding user to group
requests.request('POST', add_user, data=json.dumps(group_info), headers=headers)


message = 'Welcome to the search of the One Piece!'

#json format for group info
new_chat = {
    'roomId': room_id,
    'markdown': message
}

##Greatings for new user
requests.request('POST', 'https://webexapis.com/v1/messages', data=json.dumps(new_chat), headers=headers)

#print(welcome_message.status_code)
