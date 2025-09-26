# converter/views.py
from django.shortcuts import render
from .forms import ImageUploadForm
from PIL import Image
import pytesseract
def extract_text(request):
    html_text = ""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.open(request.FILES['image'])
            hocr_output = pytesseract.image_to_pdf_or_hocr(image, extension='hocr')
            html_text = hocr_output.decode('utf-8')
    else:
        form = ImageUploadForm()
    return render(request, 'converter/index.html', {'form': form, 'html_text': html_text})
'''
def extract_text(request):
    text = ''
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['image'])
            text = pytesseract.image_to_string(img)
    else:
        form = ImageUploadForm()
    return render(request, 'converter/index.html', {'form': form, 'text': text})
    return render(request, 'converter/format_preserve.html', {'form': form, 'html_text': html_text})

'''