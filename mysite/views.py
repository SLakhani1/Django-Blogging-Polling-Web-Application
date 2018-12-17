from django.shortcuts import render

def options_list(request):
    return render(request,'mysite/options_list.html',context=None)