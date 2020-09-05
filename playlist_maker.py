from secrets import user_auth_token
from spotify_api_oauth import SpotifyAPI
import json

def checkRecentAdded(spotify, playlistId):
    json_output = spotify.get_playlist_tracks("37i9dQZEVXcJqwWvsXBOAM")
    print(json.dumps(json_output, indent=4))

def getPlaylistIdFromName(spotify, name):
    print("")
    


spotify = SpotifyAPI(user_auth_token)
# print(spotify.search({"track": "Time"}))
# json_output = spotify.get_playlists()
# print(json.dumps(json_output, indent=4))
# for key in json_output:
#     # print(json.dumps(json_output[key], indent=4))
#     if (key == "items"):
#         # print(json.dumps(json_output[key], indent=4))
#         for item in json_output[key]:
#             # print(json.dumps(item, indent=4))
#             for item_key in item:
#                 if (item_key == "name"):
#                     print(item[item_key])

checkRecentAdded(spotify, "37i9dQZEVXcJqwWvsXBOAM")
# json_output = spotify.get_playlist_tracks("37i9dQZEVXcJqwWvsXBOAM")
# print(json.dumps(json_output, indent=4))
