from django.shortcuts import render, HttpResponse, redirect
from .models import Class,Student, Subject, Attendance
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def classes(request):
    sclass = Class.objects.all()
    return render(request,'classes.html', {'sclass': sclass})

def classDetails(request, classid):
    if request.method == 'POST':
        name = request.POST.get('name')
        uid = request.POST.get('UID')
        newStd = Student.objects.create(name = name,uid = uid)
        scls = Class.objects.get(id = classid)
        # print(scls)
        newStd.sclass.add(scls)
        newStd.save()
        
        print(newStd.sclass.get(id = classid))
        
        # print(str(newStd.sclass.all()))
        # print(newStd)

        subjects = Subject.objects.filter(sclass = classid)
        # print(subjects)
        for sub in subjects:
            att = Attendance.objects.create(subject=sub, student=newStd)
            # att.save()
            att.save()
        allobj = Attendance.objects.filter(student = newStd)
        print(allobj)


    data = Student.objects.filter(sclass = classid)
    return render(request,'addstd.html',{'stdata': data})


def getatten(request):
    atten = Attendance.objects.all()
    lis = [att.student for att in atten]
    return HttpResponse(atten)

def loginfun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request, user)
            return redirect('class/')
        else:
            print('INVALID USER LOGIN')
            return redirect('login/')
    return render(request, 'index1.html')

def classcard(request):
    return render(request, 'classCard4.html')