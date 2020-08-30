from secrets import user_auth_token
from spotify_api_oauth import SpotifyAPI
import json


spotify = SpotifyAPI(user_auth_token)
# print(spotify.search({"track": "Time"}))
json_output = spotify.get_playlists()
print(json.dumps(json_output, indent=4))
# for key in json_output:
#     # print(json.dumps(json_output[key], indent=4))
#     if (key == "items"):
#         # print(json.dumps(json_output[key], indent=4))
#         for item in json_output[key]:
#             # print(json.dumps(item, indent=4))
#             for item_key in item:
#                 if (item_key == "name"):
#                     print(item[item_key])
