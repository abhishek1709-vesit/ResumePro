from PyPDF2 import PdfReader

def extractTextFromFile(file):
    try:
        reader = PdfReader(file)
        if(len(reader.pages)>0):
            page = reader.pages[0]
            return page.extract_text().strip()
        return "No text in the uploaded pdf"
    except Exception as e:
        return f"Error processing PDF: {e}"

