import requests
import json
data = {"content":"Bu mesaj pythondan lol"}
header= {"authorization":"MzQyNTk0MzU3NzkyMjEwOTQ1.X8iEOQ.2iZHs162YXmC9aryrI3TnsJQ7l8"}
r = requests.post("https://discord.com/api/v8/channels/765972823595417660/messages",headers=header,data=data)
print(r.content)

