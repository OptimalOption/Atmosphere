from django.shortcuts import render
from django.core.mail import send_mail
from .models import *


def feedback(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'subject': subject,
            'email': email,
            'message': message
        }
        message = '''
        {}

        От кого: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['vladislavdonov98@gmail.com'])


def main(request):
    feedback(request)
    slider = Slider.objects.order_by('-id')
    return render(request, 'main/index.html', {'slider': slider})


def about(request):
    feedback(request)
    return render(request, 'main/about.html')


def directorate(request):
    feedback(request)
    employee = Employee.objects.all()
    return render(request, 'main/directorate.html', {"employee": employee})


def news(request):
    feedback(request)
    posts = Post.objects.order_by('-created_at', '-id')
    return render(request, 'main/news.html', {"posts": posts})


def licenses(request):
    feedback(request)
    return render(request, 'main/licenses.html')


def training(request):
    feedback(request)
    return render(request, 'main/training.html')


def services(request):
    feedback(request)
    return render(request, 'main/services.html')


def contacts(request):
    feedback(request)
    return render(request, 'main/contacts.html')


def vacancies(request):
    feedback(request)
    vacancies = Vacancies.objects.order_by('-id')
    return render(request, 'main/vacancies.html', {"vacancies": vacancies})


def air(request):
    feedback(request)
    return render(request, 'main/air.html')


def environment(request):
    feedback(request)
    return render(request, 'main/environment.html')


def control(request):
    feedback(request)
    return render(request, 'main/control.html')
