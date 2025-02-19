from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
import datetime
import razorpay

# Create your
# views here.
def index(re):
    return render(re,'index.html')

def registration(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['cid']
        c = request.POST['phoneno']
        d = request.POST['email']
        e = request.POST['uname']
        f = request.POST['password']

        try:

            data=colreg.objects.create(name=a, collegeid=b, phoneno=c, email=d, username=e,password=f)
            print(data)
            data.save()
            messages.success(request, "Registration success")
        except:
            messages.success(request, "Username already exists")
            return redirect(registration)

        return redirect(login)
    else:
        return render(request, 'college-reg.html')


def companyreg(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['compid']
        c = request.POST['phoneno']
        d = request.POST['email']
        e = request.POST['lisence']
        f = request.POST['uname']
        g = request.POST['password']
        h = request.POST['addr']
        try:

            data=compreg.objects.create(name=a, compid=b, phoneno=c, email=d,lisence=e, username=f,password=g,addr=h,status='pending')
            print(data)
            data.save()
            messages.success(request, "Registration success")
        except:
            messages.success(request, "Already exists")
            return redirect(companyreg)

        return redirect(login)
    else:
        return render(request, 'company-reg.html')



def login(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        try:
            data=colreg.objects.get(username=username)
            if data.password==password:
                request.session['user']=username
                messages.success(request, "login success")

                return redirect(services)
            else:
                messages.error(request, "password incorrect")
                return redirect(login)
                # return HttpResponse("password incorrect")
        except Exception:
            try:
                data = compreg.objects.get(username=username)
                if data.password==password :
                    if data.status=="active":

                        request.session['com'] = username
                        messages.success(request, "login success")

                        return redirect(companyservices)
                    else:
                        messages.error(request, "waiting for approval")
                        return redirect(login)

                else:
                    messages.error(request, "password incorrect")
                    return redirect(login)
            except Exception:
                try:
                    # data = travelreg.objects.get(username=username)
                    if data.password == password:
                        if data.status=="active":
                            request.session['travel'] = username
                            messages.success(request, "login success")

                            return redirect(services)
                        else:
                            messages.error(request, "waiting for approval")
                            return redirect(login)
                    else:
                        messages.error(request, "password incorrect")
                        return redirect(login)
                except Exception:
                    if username=='Gilcy' and password=='gilcy':
                        request.session['admin']=username
                        messages.success(request, "login success")
                        return redirect(adminhome)
                    else:
                        messages.info(request, "username incorrect")
                        return redirect(login)
    else:

        return render(request,"login.html")


def services(re):          # college services
    if 'user'in re.session:
        user1=re.session['user']
        u=colreg.objects.get(username=re.session['user'])
        c=compreg.objects.filter(status='active')
        # t=travelreg.objects.filter(status='active')
        data=Reviews.objects.all()
        return render(re, "services.html",{'user':u,'comp':c,'data':data,'user1':user1})
    # return HttpResponse("not have value")
    # return HttpResponse("not have value")
def collegedepartment(request):
    return render(request,"college-dept.html")

def companyservices(request):
    return render(request, "company-services.html")

def uprofile(request):
    if 'user' in request.session:
        user=colreg.objects.get(username=request.session['user'])
        return render(request, "uprofile.html",{'user':user})

def edituser(req,id2):
    if req.method == 'POST':
        username = req.POST['username']
        user_email = req.POST['email']
        password = req.POST['password']
        mobile = req.POST['mobile']

        try:
            profimg = req.FILES['profile']
            colreg.objects.filter(pk=id2).update(username=username,email=user_email,password=password,
                                                  phoneno=mobile,profile=profimg)
        except:
            colreg.objects.filter(pk=id2).update(username=username,email=user_email,password=password,
                                                  phoneno=mobile)

        messages.success(req, "successfully updated")
        return redirect(uprofile)
    else:
        data =colreg.objects.get(pk=id2)
        return render(req, 'edituser.html', {'data':data})


def adminhome(request):
    return render(request, "admin-home.html")
def admincoldet(request):
    data=colreg.objects.all()
    return render(request, "admin-coldet.html",{'data':data})

def admincompdet(request):
    data=compreg.objects.all()
    return render(request, "admin-compdet.html",{'data':data})

# def admintravdet(request):
#     data=travelreg.objects.all()
#     return render(request, "admin-travdet.html",{'data':data})

def companypend(re):
    data=compreg.objects.filter(status="pending")
    return render(re, "company-pend.html",{'data':data})

def pending1(re,id1):
    compreg.objects.filter(pk=id1).update(status='active')
    return redirect(companypend)


# def travelpend(re):
#     data=travelreg.objects.filter(status="pending")
#     return render(re, "travel-pend.html",{'data':data})

# def pending2(re,id2):
#     travelreg.objects.filter(pk=id2).update(status='active')
#     return redirect(travelpend)


def logout(re):
    if '' in re.session:
        re.session.flush()
    return redirect(login)

# def compabout(re):
#     if re.method=='POST':
#         a=re.POST['']
#         b=re.POST['']
#         c=re.POST['']
#         d=re.POST['']
#         e=re.POST['']
#         f=re.POST['']
#         data=.objects.create(=a,=b,=c,=d,=e,=f,
#                                     mname=.objects.get(username=re.session['music']))
#         data.save()
#         messages.success(re,'successfully added')
#         return redirect(profile1)

def compcoldet(request):
    data=collegedept.objects.all()
    return render(request, "compviewcoldet.html",{'data':data})
def fill(request):
    data1=collegedept.objects.filter(coldepartment='bsccs')
    data2=collegedept.objects.filter(coldepartment='bca')
    data3=collegedept.objects.filter(coldepartment='bcom')
    data4=collegedept.objects.filter(coldepartment='history')
    data5=collegedept.objects.filter(coldepartment='science')
    return render(request, "compviewcoldet.html", {'data1': data1,'data2': data2,'data3': data3,'data4': data4,'data5': data5})

def compaddprojects(request):
    if request.method == 'POST':
        f = compreg.objects.get(username=request.session['com'])
        collegename = request.POST['collegename']
        department= request.POST['department']
        date = request.POST['date']
        projectdescr = request.POST['projectdescr']
        projectimg= request.FILES['projectimg']

        data = comppro.objects.create(collegename=collegename, department=department, date=date, projectdescr=projectdescr, projectimg=projectimg, cname=f)
        data.save()
        messages.success(request, "successfully added")

    return render(request, 'compaddprojects.html')

def colviewivcomp(request):
    data = compreg.objects.all()
    return render(request, "colviewivcomp.html", {'data': data})


def packagedet(request):
    return render(request,"packagedet.html")



def compprofile(request):
    if 'com' in request.session:
        user=compreg.objects.get(username=request.session['com'])
        data = cabout.objects.filter(cname=user)
        data1=comppro.objects.filter(cname=user)
        return render(request, "compprofile.html",{'user':user,'data':data,'data1':data1})
# def compprofile(request):
#     return render(request, "compprofile.html")


# def travprofile(request):
#     if 'com' in request.session:
#         user=travelreg.objects.get(username=request.session['com'])
#         data = cabout.objects.filter(cname=user)
#         data1=comppro.objects.filter(cname=user)
#         return render(request, "travprofile.html",{'user':user,'data':data,'data1':data1})

def compabout(re):
    if re.method=='POST':
        a=re.POST['fprice']
        b=re.POST['location']
        c=re.POST['achievements']
        d=re.POST['disc']
        # e=re.POST['special']
        # f=re.POST['experience']
        data=cabout.objects.create(fprice=a,native=b,achievements=c,disc=d,
                                    cname=compreg.objects.get(username=re.session['com']))
        data.save()
        messages.success(re,'successfully added')
        return redirect(compprofile)
def edititem(req,id3):
    if req.method == 'POST':
        name = req.POST['name']
        username = req.POST['username']
        phoneno = req.POST['phoneno']
        email = req.POST['email']
        try:
          profile=req.FILES['profile']
          compreg.objects.filter(pk=id3).update(name=name, username=username, phoneno=phoneno, email=email,profile=profile)
        except:
          compreg.objects.filter(pk=id3).update(name=name,username=username,phoneno=phoneno,email=email)
        messages.success(req, "successfully updated")
        return redirect(compprofile)

def editdm(re,dd):
    if re.method == 'POST':
        a = re.POST['fprice']
        b = re.POST['location']
        c = re.POST['achievements']
        d = re.POST['disc']
        cabout.objects.filter(pk=dd).update(fprice=a, native=b, achievements=c, disc=d,cname=compreg.objects.get(username=re.session['com']))
        messages.success(re, "successfully updated")
        return redirect(compprofile)

# def edititem1(req,id5):
#     if req.method == 'POST':
#         name1 = req.POST['name']
#         username1 = req.POST['username']
#         phoneno = req.POST['phoneno']
#         email1 = req.POST['email']
#         try:
#           profile1=req.FILES['profile']
#           travelreg.objects.filter(pk=id5).update(name=name1, username=username1, phoneno=phoneno, email=email1,
#                                                   profile=profile1)
#         except:
#           travelreg.objects.filter(pk=id5).update(name=name1,username=username1,phoneno=phoneno,email=email1)
#         messages.success(req, "successfully updated")
#         return redirect(profile2)
def colviewcomdetails(request,dp9):
    user = compreg.objects.get(pk=dp9)

    data3 = cabout.objects.filter(cname=user)
    data4 = comppro.objects.filter(cname=user)
    # return render(request, "colviewcomdetails.html")
    return render(request, "colviewcomdetails.html",{'user':user,'data3':data3,'data4':data4})
# def compbooking(re,bok):
#     data=compreg.objects.get(pk=bok)
#     data2=cabout.objects.filter(cname=data)
#     print(data2)
#     return render(re,'selectdepart.html',{'data':data,'data2':data2})
def selectdepart(request,bk):
    data=compreg.objects.get(pk=bk)
    data2=cabout.objects.filter(cname=data)
    return render(request,"selectdepart.html",{'data':data,'data2':data2})
def bookingdet(re,bok):
    if re.method == 'POST':
        a = colreg.objects.get(username=re.session['user'])
        b = re.POST['coldepartment']
        c = re.POST['noofstudents']
        time = re.POST['time']
        e= re.POST['setTodaysDate']
        e = datetime.datetime.now()
        f=re.POST['fprice']
        data = collegedept.objects.create(name=a, coldepartment=b, noofstudents=c,time=time,fprice=f,
                                          cname=compreg.objects.get(pk=bok),datetime=e,status='pending')
        data.save()
        messages.success(re, "successfully booked")
        return redirect(colviewivcomp)


def book(re):
    user=colreg.objects.get(username=re.session['user'])
    comp=collegedept.objects.filter(status='active',name=user,cname__isnull=False)
    return render(re,'bookingdet.html',{"comp":comp})


# # def compcoldet(request):
#     data=collegedept.objects.all()
#     return render(request, "compviewcoldet.html",{'data':data})

def compcoldet(re):
    f=compreg.objects.get(username=re.session['com'])
    data=collegedept.objects.filter(cname=f,status='pending')
    # da=collegedept.objects.filter(name=f,status='active')
    # d=collegedept.objects.filter(name=f,status='reject')
    return render(re,'compviewcoldet.html',{'data':data})

def accept(req,k):
    collegedept.objects.filter(pk=k).update(status='active')
    return redirect(acc)

def acc(re):
    f = compreg.objects.get(username=re.session['com'])
    data = collegedept.objects.filter(cname=f, status='active')
    print(data)
    return render(re,'accept.html',{'data':data})

def reject(req,bk):
    collegedept.objects.filter(pk=bk).update(status='reject')
    return redirect(rej)
    # return render(req, 'reject.html')
def rej(re):
    f = compreg.objects.get(username=re.session['com'])
    data = collegedept.objects.filter(cname=f, status='reject')
    print(data)
    return render(re,'reject.html',{'data':data})

def payment(request, a, bid):
    amount = 5000
    a1 = int(a) * 100
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    collegedept.objects.filter(pk=bid).update(paid='Paid')
    return render(request, "payment.html", {'total': a1})

def success(request):
    user = colreg.objects.get(username=request.session['user'])
    data=collegedept.objects.filter(name=user,paid='Paid',cname__isnull=False)
    return render(request,'success.html',{'data':data})

def paid(re):
    user = compreg.objects.get(username=re.session['com'])
    data = collegedept.objects.filter(cname=user, paid='Paid')
    return render(re, 'paid.html', {'data': data})


def addreviews(re):
    if 'user' in re.session:
        if re.method=='POST':
            review = re.POST['feedback']
            comname = re.POST['comname']
            user = colreg.objects.get(username=re.session['user'])
            feedback=Reviews.objects.create(user=user,review=review,comname=comname)
            feedback.save()
            return render(re,'index.html')
        else:
            return render(index)
    else:
        return render(login)



# def bookingdet(re):
#     user=colreg.objects.get(username=re.session['user'])
#     comp=collegedept.objects.filter(status='active',user=user)
#     # data1=selectdepart.objects.filter(status='reject',user=user,name_isnull=false)
#
#     return render(re,'bookingdet.html',{'comp':comp,})
def contact(re):
    if re.method=='POST':
        name=re.POST['name']
        email=re.POST['email']
        message=re.POST['message']
        data = contactus.objects.create(name=name, email=email,message=message)
        data.save()
        messages.success(re, 'successfully added')
        return redirect(contact)
    else:
        return render(re,'contact.html')
def conhome(re):
    data =contactus.objects.all()
    return render(re, 'conhome.html',{'data':data})

def delete(re,id1):
    data=comppro.objects.get(pk=id1)
    data.delete()
    messages.success(re,"successfully deleted")
    return redirect(compprofile)


