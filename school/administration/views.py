from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import school_recordsJ,school_recordsS

# Create your views here.
def Admission_office(request):
    school_records1=school_recordsJ.objects.all()
    school_records2=school_recordsS.objects.all()
    work = {
        'school_recordsJ':school_records1,
        'school_recordsS':school_records2,
        }
  
    return render(request,"Admission_office.html",work)
def welcome(response):
    return render(response,"home_page.html")





     
