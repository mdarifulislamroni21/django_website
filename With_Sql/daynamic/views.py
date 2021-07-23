from django.shortcuts import render
from daynamic import form_connect
# Create your views here.
def registration_form(request):
    load_form=form_connect.registration_connect()
    passdata={
    'registration':load_form,
    }
    if request.method == 'POST':
        load_form=form_connect.registration_connect(request.POST)
        if load_form.is_valid():
            load_form.save(commit=True)
    return render (request,'pages/registrationform.html',context=passdata)
