from pytube import YouTube

def download_youtube_video(url):
  try:
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    print("Video downloaded successfully!")
  except:
    print("An error occurred.")

# Example usage:
download_youtube_video("https://www.youtube.com/watch?v=uRfr5tz97xU")