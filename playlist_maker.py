from secrets import client_id, client_secret, user_auth_token
from spotify_api import SpotifyAPI

spotify = SpotifyAPI(client_id, client_secret)
# print(spotify.search({"track": "Time"}))
output = spotify.get_playlists(user_auth_token)
print(output)
