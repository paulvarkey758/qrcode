from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from time import sleep
from .models import Mymodel
from django.core.files import File
from pathlib import Path
import os

# Create your views here.
def mainfun(request):
    return render(request,"index.html")

def getData(request):
    data=request.GET['mdata']
    print(data)
    s=Mymodel.objects.get(pk=data)
    return render(request,"show.html",{'s':s})


def mainForm(request):
    if request.method=="POST":
        id=request.POST['id']
        name=request.POST['name']
        url=f"http://127.0.0.1:8000/getdata?mdata={id}"
        image=qrcode.make(url)
        image.save("alu/qr.jpg")
        sleep(2)
        cur_d=os.path.dirname(__file__)
        n_path=os.path.join(cur_d,"qr.jpg")
        path=Path(n_path)
        pic=path.open(mode='rb')
        print(path.name)
        myPic=File(pic,name=f"qr{id}.jpg")
        newItem=Mymodel(id=id,name=name,qrCode=myPic)
        newItem.save()
        return HttpResponse("item saved")
    else:    
        return render(request,"main.html")    
