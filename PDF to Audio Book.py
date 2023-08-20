import pyttsx3
import PyPDF2

# Open the PDF file in binary mode
book = open('mybook.pdf', 'rb')  # Replace 'mybook.pdf' with the path to your PDF file

# Initialize the TTS engine
play = pyttsx3.init()

# Read the PDF using PyPDF2
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.numPages

print('Playing Audio Book')

# Iterate through all pages and extract text
for num in range(0, num_pages):
    page = pdf_reader.getPage(num)
    data = page.extractText()

    # Use the TTS engine to read the extracted text
    play.say(data)
    play.runAndWait()

# Close the PDF file
book.close()