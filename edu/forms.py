from django import forms

class ContactForm(forms.Form):
    INTEREST_CHOICES = (
        ('Utah Nalaxone', 'Utah Nalaxone'),
        ('Substance Use Disorder Support Groups', 'Substance Use Disorder Support Groups'),
        ('Mental Health Support Groups', 'Mental Health Support Groups'),
        ('Emotional Wellness Activities', 'Emotional Wellness Activities'),
        ('Virtual Sponsorships', 'Virtual Sponsorships'),
    )
    your_name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Email')
    interests = forms.MultipleChoiceField(choices=INTEREST_CHOICES, widget=forms.CheckboxSelectMultiple)
    message = forms.CharField(label='What would you like us to know?', widget=forms.Textarea)