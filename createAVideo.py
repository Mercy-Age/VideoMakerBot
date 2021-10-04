from moviepy.editor import *
import pygame

audio = 'Audio/2.mp3'
img = 'Memes/1.jpg'

pygame.display.set_caption('Hello World!')

videoclip = ImageClip(img).set_duration(4)
audioclip = AudioFileClip('Audio/2.mp3')
videoclip.audio = audioclip
videoclip.preview()

pygame.quit()