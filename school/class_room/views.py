from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import Filter_By_Examnumber
from administration.models import school_recordsJ,school_recordsS
# Create your views here.
def Exam_number(request):
	forms = Filter_By_Examnumber()
	return render(request,'examnumber.html', {"form":forms })
def login(response ,Examnumber):
	if response.method== "GET":
		forms = Filter_By_Examnumber(response.POST)
		# if form.is_valid():
		form1 = school_recordsJ.objects.get(Examnumber=Examnumber)
		form2 = school_recordsS.objects.get(Examnumber=Examnumber)  
		if forms == form1:
			return render(response,'class_list.html')
		elif form == form2:
			return render(response,'class_list.html')
		else:
			pass
		# else:
		# 	pass
	else:
		return render(response,'examnumber.html')




