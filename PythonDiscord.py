import requests
data = {"content":"{message}"}
header= {"authorization":"{token}"}
r = requests.post("https://discord.com/api/v8/channels/{channelid}/messages",headers=header,data=data)


'''
message = Message to send
token = Your discord token
channelid = Channel id of the channel to send message
'''
