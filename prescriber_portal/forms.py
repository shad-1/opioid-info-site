from django import forms
from .models import PdDrug, PdPrescriber

STATES = (
    ('', 'Select State'),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

RESULT_SET_CHOICES = (
(10, 10),
(25, 25),
(50, 50),
(100, 100),
('ALL', 'All'),
)

PRESCRIBER_SORT_CHOICES = (
    ('', 'Select'), ('F_NAME', 'First Name A-Z'), ('~F_NAME', 'First Name Z-A'), ('L_NAME', 'Last Name A-Z'), ('~L_NAME', 'Last Name Z-A'), ('TOTAL_PRESCRIPTIONS', 'Total Prescriptions (Low - High)'), ('~TOTAL_PRESCRIPTIONS', 'Total Prescriptions (High - Low)')
    )

DRUG_SORT_CHOICES = (
    ('', 'Select'), ('DRUG_NAME', 'Drug Name A-Z'), ('~DRUG_NAME', 'Drug Name Z-A'),
)
class DrugForm(forms.Form):
    drugname = forms.CharField(label='Drug Name', max_length=100, required=False)
    isopioid = forms.NullBooleanField(label='Is this an Opioid?', required=False)
    result_size = forms.ChoiceField(label='Result rows', choices=RESULT_SET_CHOICES, required=False, initial=25)
    order_by = forms.ChoiceField(label='Order by', choices=DRUG_SORT_CHOICES, required=False)

class PrescriberForm(forms.Form):
    GENDERS = (('U', 'Unspecified') , ('F', 'Female') , ('M', 'Male'))

    prescriber_name = forms.CharField(label='Prescriber name', max_length=100, required=False)
    gender = forms.ChoiceField(choices=GENDERS, required=False)
    state = forms.ChoiceField(choices=STATES, required=False)
    #TODO: Specialty
    isopioidprescriber = forms.NullBooleanField(label="Prescribes Opioids?", required=False)
    total_prescriptions = forms.IntegerField(label="Total Prescriptions Written", required=False)
    result_size = forms.ChoiceField(label='Result rows', choices=RESULT_SET_CHOICES, required=False, initial=25)
    order_by = forms.ChoiceField(label='Sort Order', choices=PRESCRIBER_SORT_CHOICES, required=False, initial='')