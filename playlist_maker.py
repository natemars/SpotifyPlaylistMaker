from secrets import user_auth_token
from spotify_api_oauth import SpotifyAPI
import json

def checkRecentAdded(spotify, playlistId):
    json_output = spotify.get_playlist_tracks("37i9dQZEVXcJqwWvsXBOAM")
    print(json.dumps(json_output, indent=4))

def getPlaylistIdFromName(spotify, name):
    json_output = spotify.get_playlists()
    playlist_id = None
    for item in json_output["items"]:
        if(item["name"] == name):
            href = item["tracks"]["href"]
            playlist_id = href.split("/")[5]
            return playlist_id

    if playlist_id == None:
        raise Exception("Playlist ID was not found.")
                    
        


spotify = SpotifyAPI(user_auth_token)
getPlaylistIdFromName(spotify, "DW LOG")
# checkRecentAdded(spotify, "37i9dQZEVXcJqwWvsXBOAM")
