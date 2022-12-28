# Сначала ты учишься загружать видео с ютуба, а потом делаешь свои софты для выгрузки хентая в огромных количествах. Народная мудрость. И точка.
#
# Чтобы всё работало --> pip install pytube

from pytube import YouTube

link = input("Enter the link of youtube video:  ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download("Downloads\python")
print("Download completed!!")