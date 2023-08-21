from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'cv/index.html', context=context)

def educationOne(request):
    context = {
        'title': 'University'
    }
    return render(request, 'cv/education-1.html', context=context)

def educationTwo(request):
    context = {
        'title': 'MBA'
    }
    return render(request, 'cv/education-2.html', context=context)

def educationThree(request):
    context = {
        'title': 'Training Courses'
    }
    return render(request, 'cv/education-3.html', context=context)

def educationFour(request):
    context = {
        'title': 'IT Skills'
    }
    return render(request, 'cv/education-4.html', context=context)

def assignmentsLT(request):
    context = {
        'title': 'Long-Term Assignment'
    }
    return render(request, 'cv/assignments.html', context=context)

def assignmentsST(request):
    context = {
        'title': 'Short-Term Assignment'
    }
    return render(request, 'cv/assignments_st.html', context=context)