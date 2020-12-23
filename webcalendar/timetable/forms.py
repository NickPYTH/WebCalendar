from django import forms
 
class CaseForm(forms.Form):
    case_start = forms.TimeField()
    case_end = forms.TimeField()
    case = forms.CharField(max_length=50)
    case_description = forms.CharField(required=False)