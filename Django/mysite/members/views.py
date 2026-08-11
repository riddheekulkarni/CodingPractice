from django.shortcuts import render
from .models import Member

def members(request):
    mymembers=Member.objects.all().values()
    content={
        'mymembers':mymembers,
    }
    return render(request, 'all_members.html',content)

def details(request,id):
    mymember=Member.objects.get(id=id)
    content={
        'mymember':mymember,
    }
    return render(request,'details.html',content)

def main(request):
    return render(request,'main.html')

def testing(request):
    mydata = Member.objects.all().order_by('firstname','-id').values()
    content={
        'mymembers':mydata,
    }
    return render(request,'template.html',content)