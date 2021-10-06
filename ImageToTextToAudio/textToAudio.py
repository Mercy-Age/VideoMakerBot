import pyttsx3

def create_audio(text: str, save_path: str):
	# Initialize the converter
	converter = pyttsx3.init()

	# Sets speed percent 
	# Can be more than 100
	converter.setProperty('rate', 170)
	# Set volume 0-1
	converter.setProperty('volume', 1)
	# Set voice
	converter.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')

	#save file and enter the text
	converter.save_to_file(text, save_path)
	
	converter.runAndWait()


#this function is purly for testing you can change it freely
def main():
	text =  'When you borrow a pen from your friend \n then you see it’s the same pen you lost recently.'
	create_audio(text, '')


if __name__ == '__main__':
	main()