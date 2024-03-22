import Extract
from Extract import *



channel_ids = ['UCDWnJMuJXwnMG9Pm7ERoVYA',"UCnItr-I_IeD9kv2zC2yLcFg"]

yt = Extract.Youtube()



request = yt.channels().list(
    part="snippet,contentDetails,statistics",
    id=','.join(channel_ids)
)
response = request.execute()


# Loop through items
def channel_stats(youtube,channel_ids):
    all_data = []
    for item in response['items']:
        data = {
            'channelname': item['snippet']['title'],
            'channelStartDate': item['snippet']['publishedAt'],
            'Country': item['snippet']['country'],
            'subscribers': item['statistics']['subscriberCount'],
            'views': item['statistics']['viewCount'],
            'TotalVidoes': item['statistics']['videoCount'],
            'PlayListID': item['contentDetails']['relatedPlaylists']['uploads']
        }
        all_data.append(data)
    return pd.DataFrame(all_data)

channel_stats_df = channel_stats(yt,channel_ids)
channel_stats_df.to_excel('Channel_Details.xlsx', index=False)
