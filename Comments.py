import pandas as pd
import PlaylistItems
from PlaylistItems import *
import Extract
from Extract import *

yt = Extract.Youtube()
video_ids = PlaylistItems.video_stats(yt,playlistId)

def get_comments(yt,video_ids):
    all_comments = []

    for video_id in video_ids:
        request = yt.commentThreads().list(
            part="snippet,replies",
            videoId=video_id
        )
        response = request.execute()

        comments_in_video = [comment['snippet']['topLevelComment']['snippet']['textOriginal'] for comment in response['items']]
        comments_in_video_info = {'video_id':video_id,'comments':comments_in_video}

        all_comments.append(comments_in_video_info)
    return pd.DataFrame(all_comments)

comments_df = get_comments(yt,video_ids)
comments_df.to_excel('Comments_Details.xlsx', index=False)