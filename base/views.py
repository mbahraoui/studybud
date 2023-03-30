from django.shortcuts import render

from .models import Room
# Create your views here.

# rooms=[
#     {'id':1,'name':'python'},
#     {'id':2,'name':'javascript'},
#     {'id':3,'name':'c++'},
# ]

def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,id):
    room=Room.objects.get(id=id)
    context={'room':room}
    return render(request,'base/room.html',context)
