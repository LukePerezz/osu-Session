from ossapi import Ossapi

client_id = XXXXX
client_secret = XXXXXX
#Create New oauth Application in settings, name it something, give http://localhost:####/ as callback in the big box. Number anything over 1024
#Eventually for users create sign in page where they get the client id and client secret and enter it as a username and password? Still thinking of how we run this as a software
#For now just put the client id and client secret in the code and run it

# create a new client at https://osu.ppy.sh/home/account/edit#oauth
api = Ossapi(client_id, client_secret)


print(api.user("xractiv").rank_history)