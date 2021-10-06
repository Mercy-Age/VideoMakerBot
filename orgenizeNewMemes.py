from ImageToTextToAudio import get_text, create_audio
import os

def orgenize_file(file, num):
	text = get_text(f'NewMemes/{file}')
	create_audio(text, f'Audio/{num}.mp3')

	os.rename(f'NewMemes/{file}', f'Memes/{num}.jpg')

def main():
	files = os.listdir('NewMemes')
	number = open('NewMemes/number of past memes.txt', 'r+')
	num = int(number.read())

	for file in files:
		if 'jpg' in file:
			num += 1
			orgenize_file(file, num)
	
	number.seek(0)
	number.write(str(num))
	number.close()



if __name__ == '__main__':
	main()