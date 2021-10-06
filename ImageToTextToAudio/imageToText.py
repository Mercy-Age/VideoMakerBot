import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def get_text(path: str):
	#take the text from the image
	str_list = pytesseract.image_to_string(path).split('\n')
	
	#remove the '♀' symbol and the '\n ' that pytesseract create
	#also remove '.' couse its slow the audio and I dont like it
	str_list.pop()
	str_list = list(filter((' ').__ne__, str_list))
	str_list = list(filter(('.').__ne__, str_list))

	
	# remove duplicate \n couse its slow the text to audio
	str_list = remove_duplicate_br(str_list)
	str_list = ' '.join(str_list)
	
	return str_list

def remove_duplicate_br(str_list: list):
	new_list = list()
	last_elemnt_is_char = False
	for i in str_list:
		if i == '':
			if last_elemnt_is_char:
				new_list.append('\n')
				last_elemnt_is_char = False
		else:
			last_elemnt_is_char = True
			new_list.append(i)
	return new_list

#this function is purly for testing you can change it freely
def main():
	str_list = get_text('3.jpg')
	print(str_list)


if __name__ == '__main__':
	main()