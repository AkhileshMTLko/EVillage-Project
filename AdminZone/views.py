from django.shortcuts import render,HttpResponse
from general.models import ContactModel,loginModel


# Create your views here.
def dashboard(request):
    if request.session.has_key("aid"):
     return render(request,"AdminZone/dash.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login/'</script>")

def responsemgmt(request):
    if request.session.has_key("aid"):
     return render(request,"AdminZone/responsemgmt.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login/'</script>")
def enquirymgmt(request):
    if request.session.has_key("aid"):
     data=ContactModel.objects.all()
     return render(request,"AdminZone/enquirymgmt.html",{"data":data})
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login/'</script>")

def feedbackmgmt(request):
    if request.session.has_key("aid"):
        return render(request, "AdminZone/feedbackmgmt.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login/'</script>")

def dynamicupdations(request):
    if request.session.has_key("aid"):
        return render(request, "AdminZone/dynamicupdations.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login/'</script>")

def registrationmgmt(request):
    if request.session.has_key("aid"):
        return render(request, "AdminZone/registrationmgmt.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login/'</script>")

def settingsmgmt(request):
    if request.session.has_key("aid"):
        return render(request, "AdminZone/settings.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login/'</script>")

def changepassword(request):
    if request.session.has_key("aid"):
        return render(request, "AdminZone/changepassword.html")
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login/'</script>")

def addscheme(request):
    if request.session.has_key("aid"):
        return render(request, "AdminZone/addscheme.html")

    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login/'</script>")


def logoutData(request):
    del request.session["aid"]
    return HttpResponse("<script>alert('Logged Out');window.location.href='/login/'</script>")

def delData(request,id):
    data=ContactModel.objects.get(id=id)
    data.delete()
    return HttpResponse("<script>alert('Record deleted');window.location.href='/enquirymgmt/'</script>")

def chageData(request):
    if request.session.has_key("aid"):
        if request.method=="POST":
            npass=request.POST["npass"]
            cpass=request.POST["cpass"]
            if npass==cpass:
                email=request.session["aid"]
                data=loginModel.objects.get(aid=email)
                data.passwd=npass
                data.save()
                return HttpResponse("<script>alert('Password changed');window.location.href='/login/'</script>")
            else:
                return HttpResponse("<script>alert('Plz confirm password');window.location.href='/chagepassword/'</script>")

    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login/'</script>")