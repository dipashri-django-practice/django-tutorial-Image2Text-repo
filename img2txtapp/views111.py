from django.shortcuts import render
from .forms import ImageUploadForm
import pytesseract
import cv2
import numpy as np
from PIL import Image
import tempfile

def preprocess_image(pil_image):
    # Convert to NumPy array (OpenCV compatible)
    image = np.array(pil_image)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Apply bilateral filter (noise reduction while preserving edges)
    blur = cv2.bilateralFilter(gray, 11, 17, 17)

    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    return thresh
def save_temp_image(image_array):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    cv2.imwrite(temp_file.name, image_array)
    return temp_file.name


def extract_text(request):
    html_text = ""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pil_image = Image.open(request.FILES['image']).convert('RGB')
            preprocessed_img = preprocess_image(pil_image)

            # Save temporary image for Tesseract
            with tempfile.NamedTemporaryFile(suffix='.png') as temp_img:
                temp_path = save_temp_image(preprocessed_img)

                #cv2.imwrite(temp_img.name, preprocessed_img)
                hocr_output = pytesseract.image_to_pdf_or_hocr(
                    temp_path,
                    extension='hocr',
                    config='--oem 3 --psm 6'
                )
                html_text = hocr_output.decode('utf-8')
    else:
        form = ImageUploadForm()

    return render(request, 'converter/index.html', {
        'form': form,
        'html_text': html_text,
    })