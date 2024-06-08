import pytesseract

def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    from PIL import Image

# Open the image file
    image = Image.open("C:\\Users\\sharm\\OneDrive\\Pictures\\Screenshots\\test2.png")

# Perform OCR using PyTesseract
    text = pytesseract.image_to_string(image)

# Print the extracted text
    print(text)

main()