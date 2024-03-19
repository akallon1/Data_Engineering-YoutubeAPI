import Extract
from Extract import *
yt = Extract.Youtube()
playlistId="UUDWnJMuJXwnMG9Pm7ERoVYA"


def video_stats(yt,playlistId):
    video_id = []
    request = yt.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlistId,
        maxResults = 50
    )
    response = request.execute()

    for item in response['items']:
        video_id.append(item['contentDetails']['videoId'])

    next_page_token = response.get('nextPageToken')
    while next_page_token is not None:
        request = yt.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlistId,
            maxResults=50
        )
        response = request.execute()


    return video_id