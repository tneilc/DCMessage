import requests
data = {"content":"Message you want to send"}
header= {"authorization":"Your Token Here"}
r = requests.post("https://discord.com/api/v8/channels/765972823595417660/messages",headers=header,data=data)


