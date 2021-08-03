from pytube import YouTube

myVideo = YouTube("https://youtu.be/vvpb8IdDZZI")

print("\n")
print("*****************title*******************")

#get video title
#print("video Title :" +myVideo.title)

#get thumbnail image
print("\n")
print("*****************Thumnail Image*******************")

#print(myVideo.thumbnail_url)

#get all Streams

print("\n")
print("*****************Video Streams*******************")

#print(myVideo.streams.all)

print("\n")
print("*****************Download Video*******************")
print("*****************Wait until Downloadis complete*******************")

#download video
myVideo.streams.first().download()

print("Video is Downloaded")

print("\n")
print("*****************Video Subtitle*******************")

caption = myVideo.captions.get_by_language_code('en')

print("Video English Subtitle : ")
print(caption.generate_srt_captions())



