from googleapiclient.discovery import build
import requests
import os
import re
import time
import concurrent.futures

#기본 설정
channel_id = "UCj38fEefpih2o1aHH886Z1g" #헤징 유튜브 https://www.youtube.com/@hejin0_0 유튜브 채널 정보탭에 들어가서 공유 누르면 채널 ID 확인 가능 
api_key = 'Youtube Data API v3' # https://cloud.google.com/apis?hl=ko 여기서 Youtube Data API v3 키 생성
youtube = build('youtube', 'v3', developerKey=api_key)

#특수문자 처리 함수
def sanitize_filename(s):
    s = s.replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)

# 썸네일 다운로드 함수, 고화질->저화질 순으로 파일이 있는지 없는지 확인하고 다운로드 실행 폴더 안에 download라는 폴더 생성한 뒤 다운로드
def download_thumbnail(video_id, filename):
    thumbnail_options = [
        'maxresdefault.jpg',
        'hqdefault.jpg',
        'default.jpg',
        '0.jpg'
    ]
    directory = 'download' #다운로드 폴더 이름 변경 가능
    os.makedirs(directory, exist_ok=True)

    for option in thumbnail_options:
        url = f"http://img.youtube.com/vi/{video_id}/{option}"
        response = requests.get(url)
        if response.status_code == 200 and len(response.content) > 2000:
            filepath = os.path.join(directory, f"{filename}.jpg")
            with open(filepath, 'wb') as out_file:
                out_file.write(response.content)
            break

# 썸네일 파일 이름을 동영상 제목으로 저장
def get_video_title(video_id):
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    title = response['items'][0]['snippet']['title']
    return title

# 메인 함수
def download_all_thumbnails(channel_id):
    video_ids = get_all_video_ids(channel_id)
    total_videos = len(video_ids)
    print(f"Total videos: {total_videos}")

    if total_videos == 0:
        print("No videos found.")
        return

    choice = input("Do you want to download thumbnails for all videos? (y/n): ")
    if choice.lower() != 'y':
        print("Thumbnails download canceled.")
        return

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i, video_id in enumerate(video_ids, start=1):
            title = get_video_title(video_id)
            sanitized_title = sanitize_filename(title)
            print(f"Scheduling download for video {i}/{total_videos}")
            futures.append(executor.submit(download_thumbnail, video_id, sanitized_title))
        concurrent.futures.wait(futures)

    print("Thumbnails download completed.")

# 채널에서 영상 목록 받아오는 함수
def get_all_video_ids(channel_id):
    video_ids = []
    page_token = None
    uploads_playlist_id = channel_id.replace('UC', 'UU')

    while True:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=page_token
        )
        response = request.execute()
        video_ids.extend([item['contentDetails']['videoId'] for item in response['items']])
        page_token = response.get('nextPageToken')
        if not page_token:
            break

    return video_ids

download_all_thumbnails(channel_id)
