import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def GetText(path):
	return pytesseract.image_to_string(path)
