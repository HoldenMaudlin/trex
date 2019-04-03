from django.shortcuts import render
from .forms import EmailForm
from .models import Emails
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    if request.method == 'POST': # If the form has been submitted...
        email_class = EmailForm(request.POST) # A form bound to the POST data
        if email_class.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            user_email = request.POST.get('contact_email', '')
            email_object = Emails(user_email=user_email)
            email_object.save()
            return redirect('/')
    else:
        email_class = EmailForm(auto_id=False)
    template = 'index/index.html'
    emails = Emails.objects.all()
    context = {
        'email_form': email_class,
        'emails': emails
    }
    return render(request, template, context)