from django.http import HttpResponse
from django.shortcuts import redirect 


def authuser(view_func):
    def warpper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashh')
        else:
            return view_func(request, *args, **kwargs)
    return warpper_func
    

def allow(allows=[]):
    def decrator(view):
        def warpper(request, *args, **kwargs):
            grope = None
            if request.user.groups.exists():
                grope = request.user.groups.all()[0].name
                if grope in allows:
                    return view(request, *args, **kwargs)
                else :
                    return HttpResponse('you dont have any permeation to this page')
            else:
                return HttpResponse('you dont have any permeation to this page')
        return warpper
    return decrator

# def goup(view):
