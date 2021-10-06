from moviepy.editor import *
import os

def create_video(file_name: str, save_path: str):
	audio = 'Audio/'+file_name+'.mp3'
	img = 'Memes/'+file_name+'.jpg'

	#create video
	videoclip = ImageClip(img).set_duration(10)
	videoclip = videoclip.set_fps(60)
	#create audio
	audioclip = AudioFileClip(audio)

	#combine the audio with the video
	videoclip.audio = audioclip
	#save
	videoclip.write_videofile('MemeVideo/'+file_name+'.mp4')

	#delete the original files couse we dont need them anymore
	os.remove(audio)
	os.remove(img)

def main():
	files = os.listdir('Memes')

	for file in files:
		#I want the name of the file without the ending
		file_name = file.replace('.jpg','')
		create_video(file_name, '')

if __name__ == '__main__':
	main()