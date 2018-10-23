# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import FormularioLogin,UserForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.views import login
from .models import User

from django.core.mail import send_mail
from django.conf import settings
from sparkpost import SparkPost
import os


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url =  reverse_lazy("admin:index")

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

class CrearUsuario(TemplateView):
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            username = request.POST.get('username')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            userd = User.objects.filter(username = username)

            if not userd.exists():
                user = User(
                    username = username,
                    email = email,
                    first_name = first_name,
                    last_name = last_name,
                    is_active = False
                )
                user.set_password(username)
                user.save()

                sp = SparkPost()
                from_email = 'test@' + os.environ.get('SPARKPOST_SANDBOX_DOMAIN')

                response = sp.transmission.send(
                    recipients = ['openmindsan@gmail.com'],
                    html = '<p>Hola</>',
                    from_email = from_email,
                    subject = 'Holaaaaaaaaa'
                )
                print(response)
                """
                asunto = 'Registro de usuario'
                mensaje_email = 'Su usuario ha sido creado, la activación del mismo no durará más de 24 horas Su contraseña es'
                email_from = settings.EMAIL_HOST_USER
                email_to = [email]

                print(email_to)

                send_mail(asunto,mensaje_email,email_from,['openmindsan@gmail.com'],fail_silently = False)
                """
                message = "Success"

            else:
                message = "El usuario ya existe"

            return HttpResponse(message)
        return render(request,'login.html')
