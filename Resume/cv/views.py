from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'cv/index.html', context)


def educationOne(request):
    context = {
        'title': 'University'
    }
    return render(request, 'cv/education-1.html', context)


def educationTwo(request):
    context = {
        'title': 'MBA'
    }
    return render(request, 'cv/education-2.html', context)


def educationThree(request):
    context = {
        'title': 'Training Courses'
    }
    return render(request, 'cv/education-3.html', context)


def educationFour(request):
    context = {
        'title': 'IT Skills'
    }
    return render(request, 'cv/education-4.html', context)


def assignmentsLT(request):
    context = {
        'title': 'Long-Term Assignment'
    }
    return render(request, 'cv/assignments.html', context)


def assignmentsST(request):
    context = {
        'title': 'Short-Term Assignment'
    }
    return render(request, 'cv/assignments_st.html', context)


def portfolio(request):
    context = {
        'title': 'Portfolio'
    }
    return render(request, 'cv/portfolio.html', context)


def portfolio_createx(request):
    context = {
        'title': 'Createx Sample'
    }
    return render(request, 'cv/portfolio_createx.html', context)


def portfolio_finsweet(request):
    context = {
        'title': 'Finsweet Sample'
    }
    return render(request, 'cv/portfolio_finsweet.html', context)