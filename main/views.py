from django.shortcuts import render
from .models import ContactMessage


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        interest = request.POST.get('interest')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            interest=interest,
            message=message
        )

        return render(request, 'main/home.html', {
            'success': 'Your enquiry has been submitted successfully!'
        })

    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def courses(request):
    return render(request, 'main/courses.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        interest = request.POST.get('interest')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            interest=interest,
            message=message
        )

        return render(request, 'main/contact.html', {
            'success': 'Your enquiry has been submitted successfully!'
        })

    return render(request, 'main/contact.html')
# Create your views here.
