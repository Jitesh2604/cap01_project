# With the the help of this code you can download any video or any audio from youtube

# Imprort content from youtube with the help of pytube

from pytube import YouTube

url = "https://www.youtube.com/watch?v=7BXJIjfJCsA"
my_video = YouTube(url)

print("********************Video Thumbnail*********************")
print(my_video.title)

print("********************Video Thumbnail*********************")
print(my_video.thumbnail_url)

# for all formates
videos = my_video.streams.all()
all_fromate_list = list(enumerate(videos))
for fromate in all_fromate_list:
    print(fromate)
strm = int(input("Enter index: "))
videos[strm].download()
print("Download Secussfully")  


