from django import forms
from .validators import validate_url,validate_dot_com

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label="",
                          validators=[validate_url],
                          widget=forms.TextInput(attrs={'placeholder': 'http://example.com',
                                                        'class': 'form-control',}))


    '''
    def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        url = cleaned_data.get('url')
        url_validator = URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError("Invalid URL")
        return url
    
    def clean_url(self):
        url = self.cleaned_data.get('url')
        if 'http' in url:
            return url
        return 'http://' + url      '''