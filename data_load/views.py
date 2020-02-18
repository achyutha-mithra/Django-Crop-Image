from django.shortcuts import render, redirect
from django.contrib import messages

from django.views import generic
import json
from ast import literal_eval
import base64
import xml.etree.cElementTree as et
# from data_load.services import get_photos_by_group_id, download_images, create_table, insert_into_db
from rest_framework.decorators import action, permission_classes, authentication_classes
from django.contrib.auth.decorators import login_required
from .models import Image_Upload
from .forms import ImageForm
from django.http import HttpResponse
from .services import crop_and_save


def image_view(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            print(form.data)
            img = crop_and_save(
                form.data["array"], request.FILES["hotel_Main_Img"])
            original_file = "media/pics/"+str(request.FILES["hotel_Main_Img"])
            return render(request, 'response.html', {'crp_image': img, 'img': original_file})
    else:
        form = Image_Upload()
    return render(request, 'image.html', {'form': form})
