from secrets import user_auth_token
from spotify_api_oauth import SpotifyAPI
import json
import datetime
import time

def check_recent_added(spotify, playlistId):
    next_request = " "
    offset = 0
    most_recent_time = 0
    json_output = spotify.get_playlist_tracks(playlist_id, offset, 100)
    if json_output == None:
        raise Exception("No tracks in playlist.")
    while next_request != None:
        for items in json_output["items"]:
            # print(items["added_at"])
            # print(items["track"]["id"])
            item_time = time.mktime(datetime.datetime.strptime(items["added_at"], "%Y-%m-%dT%H:%M:%SZ").timetuple())
            print(item_time)
            if item_time > most_recent_time:
                most_recent_time = item_time
        next_request = json_output["next"]
        offset += 100
        json_output = spotify.get_playlist_tracks(playlist_id, offset, 100)

    return most_recent_time

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
print(datetime.datetime.now().timetuple())
