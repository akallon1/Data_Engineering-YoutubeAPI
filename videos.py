import pandas as pd
from dateutil import parser
import isodate
import Extract
import PlaylistItems
from Extract import *
from PlaylistItems import *

yt = Extract.Youtube()
playlistId="UUnItr-I_IeD9kv2zC2yLcFg"
video_ids = PlaylistItems.video_stats(yt,playlistId)



def get_video_details(yt,video_ids):
    """
    To Extract and parse Json video info
    :param yt:
    :param video_ids:
    :return:
    """

    all_video_info = []

    request = yt.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_ids[::]
    )
    response = request.execute()

    for video in response['items']:
        stats_to_keep = {
            'snippet':['channelTitle','title','description','tags','publishedAt'],
            'statistics':['viewCount','likeCount','favouriteCount','commentCount'],
            'contentDetails':['duration','definition','caption']
        }
        video_info = {}
        video_info['video_id'] = video['id']

        for k in stats_to_keep.keys():
            for v in stats_to_keep[k]:
                try:
                    video_info[v] = video[k][v]
                except:
                    video_info[v] = None

        all_video_info.append(video_info)
    return pd.DataFrame(all_video_info)


video_df = get_video_details(yt,video_ids)


#Transformations of data types
numeric_cols = ['viewCount','likeCount','favouriteCount','commentCount']
video_df[numeric_cols] = video_df[numeric_cols].apply(pd.to_numeric,errors = 'coerce',axis=1)


video_df['durationSecs'] = video_df['duration'].apply(lambda x: isodate.parse_duration(x))
video_df['durationSecs'] = video_df['durationSecs'].astype('timedelta64[s]')

# add tags count
video_df["tagCount"] = video_df['tags'].apply(lambda x: 0 if x is None else len(x))

video_df.to_excel('Video_Details.xlsx', index=False)

