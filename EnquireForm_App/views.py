
from django.shortcuts import render
from django.http import HttpResponse

from .models import EnquireData
from .forms import EnquiryForm

def EnquiryView(request):
    if request.method=='POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name','')
            email = form.cleaned_data.get('email','')
            mobile = form.cleaned_data.get('mobile','')

            course = form.cleaned_data.get('course','')
            location = form.cleaned_data.get('location','')
            start_date = form.cleaned_data.get('start_date','')
            gender = form.cleaned_data.get('gender','')

            data = EnquireData(
                name=name, email=email, mobile=mobile,
                course=course, location=location,
                start_date=start_date, gender=gender
            )
            data.save()
            return HttpResponse('form data saved')
        else:
            return HttpResponse('Form not valid')
    else:
        form = EnquiryForm()
        return render(request,'enquireform.html',{'form':form})

