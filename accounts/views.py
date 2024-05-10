from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user_name = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, user_name= user_name,password=password)
            user.phone_number = phone_number
            user.save()
            
            current_site = get_current_site(request)
            email_subject = 'Por favor activa tu cuenta'
            body = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),    
            })
            to_email = email
            send_email = EmailMessage(email_subject, body, to=[to_email])
            send_email.send()
            
            messages.success(request,'Se registro el usuario exitosamente')
            return redirect('register')
            
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context) 

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Las credenciales son incorrectas')
            return redirect('login')
        

    return render(request, 'accounts/login.html') 

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Has cerrado sesión')
    
    return redirect('login')
    
    