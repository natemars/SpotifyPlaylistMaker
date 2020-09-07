from secrets import user_auth_token
from spotify_api_oauth import SpotifyAPI
import json

def check_recent_added(spotify, playlistId):
    next_request = " "
    offset = 0
    while next_request != None:
        json_output = spotify.get_playlist_tracks(playlist_id, offset, 100)
        for items in json_output["items"]:
            print(items["added_at"])
        next_request = json_output["next"]
        offset += 100

def get_playlist_id_from_name(spotify, name):
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
# playlist_id = getPlaylistIdFromName(spotify, "Discover Weekly")
playlist_id = get_playlist_id_from_name(spotify, "DW LOG")
check_recent_added(spotify, playlist_id)
