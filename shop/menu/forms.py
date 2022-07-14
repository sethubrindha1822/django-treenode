from django.forms import ModelForm
from .models import soap,paste


class soapform(ModelForm):

    class Meta:
        model = soap
        fields = ('sname','sprice','sdes')

class pasteform(ModelForm):
    class Meta:
        model = paste
        fields = ('sname','sprice','sdes')


