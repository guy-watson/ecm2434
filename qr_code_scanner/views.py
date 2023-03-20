import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from django.shortcuts import render, redirect

def scan_qr(request):
    if request.method == 'POST':
        # Read the image from the POST request
        image = cv2.imdecode(np.fromstring(request.FILES['image'].read(), np.uint8), cv2.IMREAD_COLOR)

        # Decode the QR code
        decoded_objects = pyzbar.decode(image)

        # Extract the data from the QR code
        if len(decoded_objects) > 0:
            data = decoded_objects[0].data.decode('utf-8')
            # Redirect to the specified URL with the QR code data as a query parameter
            return redirect(data)
        else:
            data = 'No QR code detected'

    # Render the initial form
    return render(request, 'qr_code_scanner.html')
