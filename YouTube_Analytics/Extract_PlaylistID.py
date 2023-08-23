# Extract Playlist Id's
from googleapiclient.discovery import build

def get_channel_stats(youtube, channel_ids):

    Data_all_Channels = []

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id= ','.join(channel_ids))
    response = request.execute()

    for i in range(len(response['items'])):         #Loop the Items
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                    Subscribers = response['items'][i]['statistics']['subscriberCount'],
                    Views = response['items'][i]['statistics']['viewCount'],
                    Total_Videos = response['items'][i]['statistics']['videoCount'],
                    Playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        Data_all_Channels.append(data)

    return Data_all_Channels


# Taking More Videos

def get_video_Ids(youtube, id):
    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId = id,
        maxResults = 50  ) # For taking More Data
        # id= ','.join(channel_ids)
    response = request.execute()

    video_ids = []

    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
    next_page_token = response.get('nextPageToken')
    more_pages = True

    while more_pages:
        if next_page_token is None:
            more_pages  = False
        else:
            request = youtube.playlistItems().list(
                        part="contentDetails",
                        playlistId = id,
                        maxResults = 50,            # For taking More Data
                        pageToken = next_page_token ) 
                        
            response = request.execute()

            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            next_page_token = response.get('nextPageToken')
    return video_ids

