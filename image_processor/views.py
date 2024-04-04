import io
from PIL import Image
import numpy as np
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from image_processor.models import ImageModel

@csrf_exempt
def get_image_frames(request):
    if request.method == 'GET':
        depth_min = int(request.GET.get('depth_min'))
        depth_max = int(request.GET.get('depth_max'))
        
        pixel_values = ImageModel.objects.filter(depth__gte=depth_min, depth__lte=depth_max).values_list('pixel_values', flat=True)
        
        pixels = [pixel for sublist in pixel_values for pixel in sublist]
        
        total_pixels = len(pixels)
        if total_pixels % (200*3) != 0:
            remainder = total_pixels % (200*3)
            if remainder > 0:
                pixels = pixels[:-remainder]
            else:
                pixels.extend([0] * ((200*3) - total_pixels))
        
        pixels_array = np.array(pixels, dtype=np.uint8).reshape(-1, 200, 3)
        
        image = Image.fromarray(pixels_array)
        
        width_percent = (150 / float(image.size[0]))
        height_size = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((150, height_size), Image.ADAPTIVE)

        byte_stream = io.BytesIO()
        image.save(byte_stream, format='PNG')
        byte_stream.seek(0)

        return HttpResponse(byte_stream.getvalue(), content_type='image/png')
    else:
        return HttpResponse(status=405)  # Method Not Allowed
