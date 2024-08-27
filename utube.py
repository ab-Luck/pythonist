#to work with python pytube library to access youtube to make your life easier
#u can download thousands of videos from youtube with this code
from pytube import YouTube
#from math import ceil
# Rest of your code in pytube/streams.py
#link='https://youtu.be/XLqmL9cPN1E?si=87URT0NzZfqOA4Ph'
#link1='https://youtu.be/f1h6NZYem0o?si=7h43C6V0nFyapTZ_'
#link2='https://youtu.be/qFkNATtc3mc?si=zTkc4kwK0Cn8qzxI'

#lis=[link]
#for i in lis:
yt=YouTube("https://www.youtube.com/watch?v=uRfr5tz97xU")

yd=yt.streams.get_highest_resolution()


print(f'video title {yt.title}')
print(f'views : {yt.views}')
print(f'author: {yt.author}')
print(yt.description)
print('downloading......')

if yd.download():
    print('u can enjoy your video')
else:
    print('its restricted')    