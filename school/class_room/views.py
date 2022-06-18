from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import Filter_By_Examnumber
from administration.models import school_recordsJ,school_recordsS
# Create your views here.

def Exam_number(request):
	forms = Filter_By_Examnumber()
	return render(request,'examnumber.html', {"form":forms })


def login_forms(request):
	if request.method == "POST":
		form = Filter_By_Examnumber(request.POST)
		if form.is_valid():
			the_book = school_recordsJ.objects.get(Examnumber=form.cleaned_data["code"])
			the_book1 = school_recordsS.objects.get(Examnumber=form.cleaned_data["code"])
			return render("clas_list.html", { "the_book": the_book,"the_book1": the_book1 })
			
		else:
			
			form = Filter_By_Examnumber()
	return render(request, "examnumber.html",{"form":form })