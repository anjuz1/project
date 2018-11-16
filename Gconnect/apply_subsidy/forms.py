from django import forms
from . import models


CHOICE_SOC = (
    ('----', '----'),
    ('General', 'General'),
    ('SC', 'SC'),
    ('ST', 'ST'),)

CHOICE_YES = (
    ('Yes', 'Yes'),
    ('No', 'No'),)


CHOICE_APL = (('----', '----'),
              ('APL', 'APL'),
              ('BPL', 'BPL'))
CHOICE_CONSIDERATION = (
    ('Widow', 'Widow'),
    ('Dependent', 'Dependent'),
    ('Handicapped', 'Handicapped'),
    ('not married women', 'not married women'),
    ('lifelong patient', 'lifelong patient'),
    ('lived in collany', 'lived in collany'),
    ('small farmer', 'small farmer'),
    ('none', 'none'))
CHOICE_HOUSE = (('----', '----'),
                ('Thatch house', 'Thatch house'),
                ('Roofing tile house', 'Roofing tile house'),
                ('modern house', 'modern house')
                )




class ApplySubForms(forms.ModelForm):
    social_cat = forms.ChoiceField(choices=CHOICE_SOC)
    prev_subsidy = forms.ChoiceField(choices=CHOICE_YES)
    apl_bpl = forms.ChoiceField(choices=CHOICE_APL)
    #special1_consideration = forms.ChoiceField(choices=CHOICE_CONSIDERATION, widget=forms.CheckboxSelectMultiple())
    house_typ = forms.ChoiceField(choices=CHOICE_HOUSE)
    mental_physical_challenge = forms.ChoiceField(choices=CHOICE_YES)

    class Meta:
        model = models.ApplySubsidy
        fields = ['sub_typ', 'applicant_name', 'Address_hname', 'Address_po', 'Address_road', 'mob', 'ward_hno_old', 'ward_hno_new', 'land_area', 'survey_no','ration_card_no', 'adhar_card_no', 'voter_id', 'first_elig', 'sec_elig','third_elig', 'first_prio', 'sec_prio', 'third_prio', 'fourth_prio', 'fifth_prio']
        #, 'spcl_cons']
