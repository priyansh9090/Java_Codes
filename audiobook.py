import pyttsx3
import PyPDF2

book = open('D:\From DELL\programming\BOOK\Cormen_Algorithms_3rd.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(86,100):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
 