import os
import pikepdf
from pdf2image import convert_from_path

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DELL\application\novelHack\backend\flask-api\tesseract-ocr-w64-setup-5.4.0.20240606.exe'

# Directories for input files and output OCR text files
base_dir = r"C:\Users\DELL\application\novelHack\backend\flask-api\pdf_files"  # Update with your path
output_dir = r"C:\Users\DELL\application\novelHack\backend\flask-api\pdf_to_md"  # Update with your path

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

import fitz  # PyMuPDF
from PIL import Image
import io

def pdf_to_text_with_pymupdf(pdf_path):
    extracted_text = ""
    
    # Open the PDF with PyMuPDF
    pdf_document = fitz.open(pdf_path)
    
    # Loop through each page
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        
        # Render page to an image
        pix = page.get_pixmap()
        image = Image.open(io.BytesIO(pix.tobytes()))
        
        # Perform OCR on the image
        ocr_text = pytesseract.image_to_string(image)
        extracted_text += f"\n--- Page {page_num + 1} OCR Text ---\n{ocr_text}"
    
    return extracted_text

# Process each PDF file
for file_name in os.listdir(base_dir):
    file_path = os.path.join(base_dir, file_name)
    if file_name.endswith('.pdf'):
        # Convert PDF to text using OCR
        text_content = pdf_to_text_with_pymupdf(file_path)
        
        # Save the extracted text to a .txt file
        output_path = os.path.join(output_dir, file_name + ".txt")
        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.write(text_content)

        print(f"Processed {file_name}, saved output to {output_path}")

print("All PDF files have been processed.")
