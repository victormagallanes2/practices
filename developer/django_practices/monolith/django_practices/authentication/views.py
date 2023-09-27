from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import FormView, RedirectView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect
from .forms import ChangePasswordForm


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "authentication/login.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = '/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class AdminPasswordReset(UpdateView):
    template_name = 'authentication/admin_password_change.html'
    form_class = ChangePasswordForm
    model = User
    fields = ['password']
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_id = User.objects.get(pk=self.kwargs.get('pk'))
            if(user_id):
                user_id.password = make_password(form.cleaned_data['password'])
                user_id.save()
                messages.success(request, 'Password Updated!')
            else:
                messages.error(request, "User doesn't exists")
            return redirect('index')

        return render(request, self.template_name, {'form': form})