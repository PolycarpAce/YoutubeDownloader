from pytube import YouTube

url = input("Enter the url of the video ")
yt = YouTube(url)

#Return us all the available formates for the video
formats = yt.streams.all()

#list of all formarts available
video = list(enumerate(formats)) 

for i in video:
	print(i)

#give user option to selct the formart they want
option = int(input("choose the formart"))


download = formats[option]
dl.download()


print ("Video downloaded Succesfuly")




