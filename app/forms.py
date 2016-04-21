from django import forms
from app.models import RoomImage

class UploadImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = RoomImage
        fields = ('image', )
