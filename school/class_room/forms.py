from django import forms

class Filter_By_Examnumber(forms.Form):
	code = forms.IntegerField(label='examnumber',max_value='999999999999',min_value='001')


