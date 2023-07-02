from django.shortcuts import render, HttpResponse
from .models import Class,Student, Subject, Attendance
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
    return render(request, 'index1.html')