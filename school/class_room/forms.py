from django import forms
from administration.models import school_recordsJ,school_recordsS

class Filter_By_Examnumber(forms.Form):
	code = forms.CharField(max_length='12')
	def clean_code(self):
		try:
			code= int(self.cleaned_data["code"])
		except:
			code = None
		# try:
			if code and school_recordsJ.objects.filter(Examnumber=code).count():
				return code 
			# else:
			# 	raise forms.ValidationError("Please enter a valid book ID number.")
		# except:	
			elif code and school_recordsJ.objects.filter(Examnumber=code).count():
				return code
			else:
				raise forms.ValidationError("Please enter a valid book ID number.")


