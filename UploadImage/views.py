from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def upload_image(request):
    image = request.FILES['image']
    imagename = '%s/%s'%(settings.MEDIA_ROOT, image.name)
    with open(imagename, 'wb')as i:
        for t in image.chunks():
            i.write(t)
    Image.objects.create(im = image)
    ret ={'status':1}
    return JsonResponse(ret)
