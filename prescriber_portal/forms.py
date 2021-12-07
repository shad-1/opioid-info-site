from django import forms
from .models import PdDrug, PdPrescriber
from django.forms import ModelForm


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

CREDENTIALS = (
('','Select Credential'),
('ACNP','A.C.N.P.'),
('ACNPBC','A.C.N.P.-B.C.'),
('AGACNP','A.G.A.C.N.P.'),
('ANP','A.N.P.'),
('ANPBC','A.N.P.-B.C.'),
('ANPC','A.N.P.-C.'),
('APN','A.P.N.'),
('APNC','A.P.N.-C.'),
('APNP','A.P.N.P.'),
('APRN','A.P.R.N.'),
('APRNBC','A.P.R.N.-B.C.'),
('ARNP','A.R.N.P.'),
('ARNPBC','A.R.N.P.-B.C.'),
('ARNPC','A.R.N.P.-C.'),
('BS','B.S.'),
('BSN','B.S.N.'),
('CANP','C.A.N.P.'),
('CCNS','C.C.N.S.'),
('CCRN','C.C.R.N.'),
('CFNP','C.F.N.P.'),
('CNM','C.N.M.'),
('CNNP','C.N.N.P.'),
('CNP','C.N.P.'),
('CNS','C.N.S.'),
('CRN','C.R.N.'),
('CRNA','C.R.N.A.'),
('CRNP','C.R.N.P.'),
('CS','C.S.'),
('DCNP','D.C.N.P.'),
('DDS','D.D.S.'),
('DMD','D.M.D.'),
('DNP','D.N.P.'),
('DPM','D.P.M.'),
('FAAFP','F.A.A.F.P.'),
('FACA','F.A.C.A.'),
('FACC','F.A.C.C.'),
('FACE','F.A.C.E.'),
('FACG','F.A.C.G.'),
('FACP','F.A.C.P.'),
('FACS','F.A.C.S.'),
('FCCP','F.C.C.P.'),
('FNP','F.N.P.'),
('FNPBC','F.N.P.-B.C.'),
('FNPC','F.N.P.-C.'),
('FPMHNP','F.P.M.H.N.P.'),
('FSCAI','F.S.C.A.I.'),
('FSVM','F.S.V.M.'),
('GNP','G.N.P.'),
('GNPBC','G.N.P.-B.C.'),
('LACC','L.A.C.C.'),
('LP','L.P.'),
('MA','M.A.'),
('MB','M.B.'),
('MBA','M.B.A.'),
('MBBCH','M.B.B.C.H.'),
('MBBS','M.B.B.S.'),
('MD','M.D.'),
('MHS','M.H.S.'),
('MMS','M.M.S.'),
('MPAS','M.P.A.S.'),
('MPH','M.P.H.'),
('MRCP','M.R.C.P.'),
('MS','M.S.'),
('MSHS','M.S.H.S.'),
('MSN','M.S.N.'),
('NASPE','N.A.S.P.E.'),
('ND','N.D.'),
('NP','N.P.'),
('NPP','N.P.P.'),
('OD','O.D.'),
('PA','P.A.'),
('PAC','P.A.C.'),
('PC','P.C.'),
('PharmD','Pharm.D.'),
('PhD','Ph.D.'),
('PMHNP','P.M.H.N.P.'),
('PMHNPBC','P.M.H.N.P.-B.C.'),
('PMHNPC','P.M.H.N.P.-C.'),
('PSYNP','P.S.Y.N.P.'),
('PT','P.T.'),
('RN','R.N.'),
('RNCS','R.N.C.S.'),
('RPAC','R.P.A.C.'),
('RPH','R.P.H.'),
('VMD','V.M.D.'),
('WHNP','W.H.N.P.'),
)

SPECIALITY = (
('','Select Speciality'),
('Allergy/Immunology','Allergy/Immunology'),
('Anesthesiology','Anesthesiology'),
('Cardiac Electrophysiology','Cardiac Electrophysiology'),
('Cardiac Surgery','Cardiac Surgery'),
('Cardiology','Cardiology'),
('Certified Clinical Nurse Specialist','Certified Clinical Nurse Specialist'),
('Certified Nurse Midwife','Certified Nurse Midwife'),
('Clinic/Center','Clinic/Center'),
('Colorectal Surgery (formerly proctology)','Colorectal Surgery (formerly proctology)'),
('Community Health Worker','Community Health Worker'),
('Critical Care (Intensivists)','Critical Care (Intensivists)'),
('CRNA','CRNA'),
('Dentist','Dentist'),
('Dermatology','Dermatology'),
('Diagnostic Radiology','Diagnostic Radiology'),
('Emergency Medicine','Emergency Medicine'),
('Endocrinology','Endocrinology'),
('Family Medicine','Family Medicine'),
('Family Practice','Family Practice'),
('Gastroenterology','Gastroenterology'),
('General Acute Care Hospital','General Acute Care Hospital'),
('General Practice','General Practice'),
('General Surgery','General Surgery'),
('Geriatric Medicine','Geriatric Medicine'),
('Geriatric Psychiatry','Geriatric Psychiatry'),
('Gynecological/Oncology','Gynecological/Oncology'),
('Health Maintenance Organization','Health Maintenance Organization'),
('Hematology','Hematology'),
('Hematology/Oncology','Hematology/Oncology'),
('Hospice and Palliative Care','Hospice and Palliative Care'),
('Hospitalist','Hospitalist'),
('Infectious Disease','Infectious Disease'),
('Internal Medicine','Internal Medicine'),
('Interventional Pain Management','Interventional Pain Management'),
('Interventional Radiology','Interventional Radiology'),
('Legal Medicine','Legal Medicine'),
('Maxillofacial Surgery','Maxillofacial Surgery'),
('Medical Oncology','Medical Oncology'),
('Multispecialty Clinic/Group Practice','Multispecialty Clinic/Group Practice'),
('Nephrology','Nephrology'),
('Neurology','Neurology'),
('Neuropsychiatry','Neuropsychiatry'),
('Neurosurgery','Neurosurgery'),
('Nuclear Medicine','Nuclear Medicine'),
('Nurse Practitioner','Nurse Practitioner'),
('Obstetrics/Gynecology','Obstetrics/Gynecology'),
('Ophthalmology','Ophthalmology'),
('Optometry','Optometry'),
('Oral Surgery (dentists only)','Oral Surgery (dentists only)'),
('Orthopedic Surgery','Orthopedic Surgery'),
('Osteopathic Manipulative Medicine','Osteopathic Manipulative Medicine'),
('Otolaryngology','Otolaryngology'),
('Pain Management','Pain Management'),
('Pediatric Medicine','Pediatric Medicine'),
('Pharmacist','Pharmacist'),
('Physical Medicine and Rehabilitation','Physical Medicine and Rehabilitation'),
('Physician Assistant','Physician Assistant'),
('Plastic and Reconstructive Surgery','Plastic and Reconstructive Surgery'),
('Podiatry','Podiatry'),
('Preventive Medicine','Preventive Medicine'),
('Psychiatry','Psychiatry'),
('Psychiatry & Neurology','Psychiatry & Neurology'),
('Psychologist (billing independently)','Psychologist (billing independently)'),
('Pulmonary Disease','Pulmonary Disease'),
('Radiation Oncology','Radiation Oncology'),
('Registered Nurse','Registered Nurse'),
('Rheumatology','Rheumatology'),
('Specialist','Specialist'),
('Sports Medicine','Sports Medicine'),
('Student in an Organized Health Care Education/Training Program','Student in an Organized Health Care Education/Training Program'),
('Surgical Oncology','Surgical Oncology'),
('Thoracic Surgery','Thoracic Surgery'),
('Unknown Physician Specialty Code','Unknown Physician Specialty Code'),
('Urology','Urology'),
('Vascular Surgery','Vascular Surgery')
)

GENDERS = (('U', 'Unspecified') , ('F', 'Female') , ('M', 'Male'))

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
    
    prescriber_name = forms.CharField(label='Prescriber name', max_length=100, required=False)
    gender = forms.ChoiceField(choices=GENDERS, required=False)
    state = forms.ChoiceField(choices=STATES, required=False)
    specialty = forms.ChoiceField(choices=SPECIALITY, required=False)
    isopioidprescriber = forms.NullBooleanField(label="Prescribes Opioids?", required=False)
    total_prescriptions = forms.IntegerField(label="Total Prescriptions Written", required=False)
    result_size = forms.ChoiceField(label='Result rows', choices=RESULT_SET_CHOICES, required=False, initial=25)
    order_by = forms.ChoiceField(label='Sort Order', choices=PRESCRIBER_SORT_CHOICES, required=False, initial='')

class TotPrescPredForm(forms.Form):
    state = forms.ChoiceField(choices=STATES)
    gender = forms.ChoiceField(choices=GENDERS)
    isopioidprescriber = forms.NullBooleanField(label="Prescribes Opioids?")
    credential = forms.ChoiceField(choices=CREDENTIALS)
    specialty = forms.ChoiceField(choices=SPECIALITY)
    order_by = forms.ChoiceField(label='Sort Order', choices=PRESCRIBER_SORT_CHOICES, required=False, initial='')

class PredPrescOp(forms.Form):
    state = forms.ChoiceField(choices=STATES)
    gender = forms.ChoiceField(choices=GENDERS)
    totalprescriptions = forms.IntegerField()
    specialty = forms.ChoiceField(choices=SPECIALITY)

class PrescriberCrud(forms.Form):
    fname = forms.CharField(label='First Name', max_length=100, required=True)
    lname = forms.CharField(label='Last Name', max_length=100, required=True)
    gender = forms.ChoiceField(choices=GENDERS, required=True)
    state = forms.ChoiceField(choices=STATES, required=True)
    specialty = forms.ChoiceField(choices=SPECIALITY, required=True)
    isopioidprescriber = forms.NullBooleanField(label="Prescribes Opioids", required=True)
    totalprescriptions = forms.IntegerField(label="Total Prescriptions Written", required=True)

    