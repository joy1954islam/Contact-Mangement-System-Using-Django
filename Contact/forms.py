from django import forms

from Contact.models import Contact


class ContactForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    # or
    # publication_date = forms.CharField(widget=forms.widgets.DateInput(attrs={"type": "date"}))
    #
    # publication_date = forms.DateField(
    # label='What is your publication date?',
    # # change the range of the years from 1980 to currentYear
    # widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year))
    # )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Contact
        fields = [
            'name','nickname','phone_number','email','dob','gender','bio','profile_image',
        ]