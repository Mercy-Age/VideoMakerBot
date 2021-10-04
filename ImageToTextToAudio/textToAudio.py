from gtts import gTTS

def CreateAudio(text, save_path):
	language = 'en'
	myobj = gTTS(text=text, lang=language, slow=True) 
	myobj.save(save_path)