from django.shortcuts import render

# Create your views here.

rooms=[
    {'id':1,'name':'python'},
    {'id':2,'name':'javascript'},
    {'id':3,'name':'c++'},
]

def home(request):
    context={'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,id):
    room=None
    for i in rooms:
        if i['id']==int(id):
            room=i
    print(room)
    context={'room':room}
    return render(request,'base/room.html',context)
