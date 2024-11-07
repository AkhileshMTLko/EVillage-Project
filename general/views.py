from django.shortcuts import render,HttpResponse
from general.models import ContactModel,loginModel
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
import  random
def index(request):
    return render(request, 'proj.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request,"registration.html")

def photo(request):
    return render(request,"photo.html")

def schemes(request):
    return render(request,"schemes.html")

def links(request):
    return render(request,"links.html")

def bhulekha(request):
    return render(request,"bhulekha.html")

def manrega(request):
    return render(request,"manrega.html")

def schloorships(request):
    return render(request,"schloorships.html")

def login(request):
    return render(request,"login.html")

def contact(request):
    return render(request,"contact.html")

def contactData(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        mob=request.POST['mob']
        query=request.POST['query']
        data=ContactModel(name=name,email=email,mobile=mob,query=query)
        data.save()
        return HttpResponse("<script>alert('Your contact data is saved successfully');window.location.href='/contact/'</script>")
    else:
        return HttpResponse("<script>alert('Your contact data is not saved ');window.location.href='/contact/'</script>")



def loginData(request):
 try:
    if request.method == "POST":
        adminid=request.POST['adminid']
        passwd=request.POST['passwd']
        lg=loginModel.objects.get(aid=adminid)
        if lg.aid==adminid and lg.passwd==passwd:
            request.session['aid']=adminid
            return HttpResponse("<script>alert('Login successfully');window.location.href='/dash/'</script>")
        else:
            return HttpResponse("<script>alert('invalid admin id or password');window.location.href='/login/'</script>")

 except loginModel.DoesNotExist:
   return HttpResponse("<script>alert('Invalid admin id or password');window.location.href='/login/'</script>")


def forget(request):
    return render(request,"forget.html")

def otp(request):
    return render(request,"otp.html")

def newpass(request):
    return render(request,"newpass.html")

def forgetData(request):
 try:
    if request.method == "POST":
        adminid=request.POST['adminid']
        data=loginModel.objects.get(aid=adminid)
        if data.aid==adminid:
            x1 = int(random.random() * 12)
            x2 = int(random.random() * 14)
            x3 = int(random.random() * 16)
            x4 = int(random.random() * 12)
            code=str(x1) + str(x2) + str(x3) + str(x4)
            send_mail(subject="OTP Verification from E-Village Portal",
                      message="Your OTP code is "+code+" Regards E-Village Portal",
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[adminid],
                      fail_silently=False)
            request.session['code']=code
            request.session['adminid']=adminid
            return HttpResponse("<script>alert('Your OTP is sent on "+adminid
                                +" email address .Kindly check it');window.location.href='/otp/'</script>")

        else:
            return HttpResponse("<script>alert('This Email ID is not registered');window.location.href='/forget/'</script>")

 except loginModel.DoesNotExist:
     return HttpResponse("<script>alert('This Email ID is not registered');window.location.href='/forget/'</script>")



def otpData(request):
    if request.method == "POST":
        otp=request.POST['otp']
        code=request.session['code']
        if otp==code:
            request.session['adminid']=request.session['adminid']
            return HttpResponse("<script>window.location.href='/newpass/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid OTP');window.location.href='/forget/'</script>")