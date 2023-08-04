from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'cv/home.html', context=context)

def educationOne(request):
    context = {
        'title': 'University'
    }
    return render(request, 'cv/education-1.html', context=context)