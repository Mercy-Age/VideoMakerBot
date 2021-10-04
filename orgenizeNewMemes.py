from ImageToTextToAudio import GetText, CreateAudio
import os

def orgenizeFile(file, num):
	text = GetText(f'NewMemes/{file}')
	CreateAudio(text, f'Audio/{num}.mp3')

	os.rename(f'NewMemes/{file}', f'Memes/{num}.jpg')

def main():
	files = os.listdir('NewMemes')
	number = open('NewMemes/number of past memes.txt', 'r+')
	num = int(number.read())

	for file in files:
		if 'jpg' in file:
			num += 1
			orgenizeFile(file, num)
	
	number.seek(0)
	number.write(str(num))
	number.close()



if __name__ == '__main__':
	main()