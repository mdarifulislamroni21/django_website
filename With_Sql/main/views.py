from django.shortcuts import render
from django.http import HttpResponse
from main.models import registration
from main  import buy_product_form
from main.models import registration,user_details
from django.db.models import Avg
from daynamic import form_connect
from main import buy_product_form
# Create your views here.
def home(request):
    load_details=registration.objects.order_by('frist_name')
    passdetails={'user_details':load_details}
    return render (request,'pages/home.html',context=passdetails)
def about(request):
    return render (request,'pages/about.html')
def contact(request):
    return render (request,'pages/contact.html')
def user(request):
    load_user=registration.objects.order_by('user_name')
    passuser={'users':load_user,}
    return render (request,'pages/user.html',context=passuser)
def buyproduct(request):
    load_buyform=buy_product_form.user_details_connect()
    passbuyform={'buyproduct':load_buyform,}
    if request.method =='POST':
        create_newbuy=buy_product_form.user_details_connect(request.POST)
        if create_newbuy.is_valid():
            create_newbuy.save(commit=True)
    return render (request,'pages/buyproduct.html',context=passbuyform)
def user_def(request,regid):
    loaaduser_data=registration.objects.get(pk=regid)
    details_data=user_details.objects.filter(user_id=regid)
    # totalavg=user_details.objects.filter(user_id=regid).aggregate(Avg('colum num'))
    passcontext={'user_data':loaaduser_data,'user_datasss':details_data,}
    return render(request,'pages/user_details.html',context=passcontext)
def edid_user(request,priid):
    all_data_load=registration.objects.get(pk=priid)
    load_form=form_connect.registration_connect(instance=all_data_load)
    passalldata={'edid_user':load_form,'user_id':priid}
    if request.method == 'POST':
        create_new=form_connect.registration_connect(request.POST,instance=all_data_load)
        if create_new.is_valid():
            create_new.save(commit=True)
            return user_def(request,priid)
    return render (request,'pages/edid_user.html',context=passalldata)
def edid_product(request,product_id):
    product_form=user_details.objects.get(pk=product_id)
    with_data=buy_product_form.user_details_connect(instance=product_form)

    allpass={'edid_product':with_data,'product_id':product_id}
    if request.method == 'POST':
        product_form=buy_product_form.user_details_connect(request.POST,instance=product_form)
        if product_form.is_valid():
            product_form.save(commit=True)
            allpass.update({'success':'Yout Product Details Update Successfull'})
    return render (request,'pages/edid_product.html',context=allpass)
def delete_product(request,product_pk):
    delete_product=user_details.objects.get(pk=product_pk).delete()

    passamassage={'delete_success':"Delete Product Success "}
    return render (request,'pages/delete.html',context=passamassage)
def delete_user(request,userid):
    user_delete=registration.objects.get(pk=userid).delete()
    passmassage={'delete_success':"User Delete Successfull"}
    return render(request,'pages/user_delete.html',context=passmassage)
