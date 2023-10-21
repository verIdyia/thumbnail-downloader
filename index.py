from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
from googleapiclient.discovery import build
import requests
import os
import re
import concurrent.futures
import webbrowser


class YouTubeThumbnailDownloader:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Thumbnail Downloader")
        master.geometry("300x300")

        self.label = Label(master, text="Enter Channel ID:")
        self.label.pack()
        self.channel_entry = Entry(master)
        self.channel_entry.pack()
        self.channel_entry.insert(0, 'UCj38fEefpih2o1aHH886Z1g')  # 초기 값 설정 헤징 유튜브 채널

        self.label2 = Label(master, text="Enter YouTube API Key:")
        self.label2.pack()
        self.api_entry = Entry(master)
        self.api_entry.pack()

        self.download_button = Button(master, text="Download Thumbnails", command=self.download_all_thumbnails)
        self.download_button.pack()

        self.api_button = Button(master, text="Get YouTube API Key", command=self.open_api_page)
        self.api_button.pack()

        self.total_videos_text = StringVar()
        self.total_videos_label = Label(master, textvariable=self.total_videos_text)
        self.total_videos_label.pack()

    def open_api_page(self):
        webbrowser.open("https://cloud.google.com/apis?hl=ko")
        
    #특수문자 제거 함수
    def sanitize_filename(self, s):
        s = s.replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', s)
        
    #썸네일 다운로드 함수
    def download_thumbnail(self, video_id, filename):
        thumbnail_options = [
            'maxresdefault.jpg',
            'hqdefault.jpg',
            'default.jpg',
            '0.jpg'
        ]
        # 다운로드 폴더 설정 폴더이름 변경 가능
        directory = 'download'
        os.makedirs(directory, exist_ok=True)

        for option in thumbnail_options:
            url = f"http://img.youtube.com/vi/{video_id}/{option}"
            response = requests.get(url)
            if response.status_code == 200 and len(response.content) > 2000:
                filepath = os.path.join(directory, f"{filename}.jpg")
                with open(filepath, 'wb') as out_file:
                    out_file.write(response.content)
                break
                
    # 비디오 제목을 얻는 함수
    def get_video_title(self, video_id):
        request = self.youtube.videos().list(
            part="snippet",
            id=video_id
        )
        response = request.execute()
        title = response['items'][0]['snippet']['title']
        return title
        
    # 채널의 모든 비디오 ID를 얻는 함수
    def get_all_video_ids(self, channel_id):
        video_ids = []
        page_token = None
        uploads_playlist_id = channel_id.replace('UC', 'UU')

        while True:
            request = self.youtube.playlistItems().list(
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

    #메인함수
    def download_all_thumbnails(self):
        channel_id = self.channel_entry.get()
        api_key = self.api_entry.get()
        self.youtube = build('youtube', 'v3', developerKey=api_key)

        video_ids = self.get_all_video_ids(channel_id)
        total_videos = len(video_ids)
        self.total_videos_text.set(f"Total videos: {total_videos}")

        if total_videos == 0:
            messagebox.showinfo("Info", "No videos found.")
            return
        # 사용자에게 다운로드 여부를 확
        choice = messagebox.askyesno("Question", "Do you want to download thumbnails for all videos?")
        if choice:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = []
                for i, video_id in enumerate(video_ids, start=1):
                    title = self.get_video_title(video_id)
                    sanitized_title = self.sanitize_filename(title)
                    print(f"Scheduling download for video {i}/{total_videos}")
                    futures.append(executor.submit(self.download_thumbnail, video_id, sanitized_title))
                concurrent.futures.wait(futures)

            messagebox.showinfo("Info", "Thumbnails download completed.")
        else:
            messagebox.showinfo("Info", "Thumbnails download canceled.")

# Tkinter 앱 실행
root = Tk()
app = YouTubeThumbnailDownloader(root)
root.mainloop()
