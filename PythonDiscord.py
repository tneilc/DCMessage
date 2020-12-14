import requests
data = {"content":"Message you want to send"}
header= {"authorization":"Your Token Here"}
r = requests.post("https://discord.com/api/v8/channels/id of the channel to send/messages",headers=header,data=data)


