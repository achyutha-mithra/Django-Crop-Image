from django import forms
from .models import Image_Upload


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image_Upload
        fields = ['array', 'name', 'hotel_Main_Img']
