from secrets import user_auth_token
from spotify_api_oauth import SpotifyAPI
import json
import datetime
import time

def check_recent_added(spotify, playlist_id):
    next_request = " "
    offset = 0
    most_recent_time = 0
    json_output = spotify.get_playlist_tracks(playlist_id, offset, 100)
    if json_output == None:
        raise Exception("No tracks in playlist.")
    while next_request != None:
        for items in json_output["items"]:
            print(items["added_at"])
            print(items["track"]["id"])
            item_time = time.mktime(datetime.datetime.strptime(items["added_at"], "%Y-%m-%dT%H:%M:%SZ").timetuple())
            print(item_time)
            if item_time > most_recent_time:
                most_recent_time = item_time
        next_request = json_output["next"]
        offset += 100
        json_output = spotify.get_playlist_tracks(playlist_id, offset, 100)

    return most_recent_time

def get_track_uris(spotify, playlist_id):
    next_request = " "
    offset = 0
    track_uris = []
    
    while next_request != None:
        json_output = spotify.get_playlist_tracks(playlist_id, offset, 100)
        if json_output == None:
            raise Exception("No tracks in playlist.")
        for items in json_output["items"]:
            # print(items["added_at"])
            # print(items["track"]["id"])
            track_uris.append(items["track"]["uri"])
        next_request = json_output["next"]
        offset += 100

    return track_uris

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
delivering_pl_ids = get_track_uris(spotify, get_playlist_id_from_name(spotify, "Discover Weekly"))
receiving_pl_ids = get_track_uris(spotify, get_playlist_id_from_name(spotify, "test"))
print("test: "+ get_playlist_id_from_name(spotify, "test"))
# test: 1pDx8Gx3cPlgpPsebyBnDP
#"uri": "spotify:track:6sVQNUvcVFTXvlk3ec0ngd"
json_body = '{"uri": "spotify:track:6sVQNUvcVFTXvlk3ec0ngd"}'

spotify.post_playlist_tracks(get_playlist_id_from_name(spotify, "test"), json.loads(json_body))

# for id in delivering_pl_ids:
#     if id not in receiving_pl_ids:
#         # add track
#         print(id)
