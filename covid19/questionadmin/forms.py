from django import forms

class ScaleForm(forms.Form):
    CHOICES = [
            (0, 'None'),
            (1, 'Mild'),
            (2, 'Moderate'),
            (3, 'Severe'),
            ]
    scale = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

class QuestionnaireForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(QuestionnaireForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')
