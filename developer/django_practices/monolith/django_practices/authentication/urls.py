from django.conf.urls import url
from django.urls import path
from .views import LoginView
from .views import LogoutView
from .views import AdminPasswordReset
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
               url(r'^login/$', LoginView.as_view(), name='view_login'),
               url(r'^logout/$', LogoutView.as_view(), name='view_logout'),

               # Metodo 1 cambio de contraseña por email
               # vista para ingresar email
               url(r'^reset/password/reset/$', PasswordResetView.as_view(template_name='usercustom/password_reset_form.html', email_template_name='usercustom/password_reset_email.html'), name='password_reset'),
               # vista para mostrar mensaje de correo enviado y para mostrar el contenido del correo
		       url(r'^reset/password/reset/done/$', PasswordResetDoneView.as_view(template_name='usercustom/password_reset_done.html'), name='password_reset_done'),
		       # vista para mostrar el formulario de nueva contraseña
		       url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(template_name='usercustom/password_reset_confirm.html'), name='password_reset_confirm'),
		       # vista para mostrar mensaje de cambio de contraseña satisfactorio
	    	   url(r'^reset/done/$', PasswordResetCompleteView.as_view(template_name='usercustom/password_reset_complete.html'), name='password_reset_complete'),

               # Metodo 2 cambio de contraseña directo sin enviar email
	    	   # formulario de nueva contraseña
	    	   # Nota: solo puede cambiar contraseña para el usuario logeado
               url(r'^change/password/(?P<pk>[0-9]+)/$', PasswordChangeView.as_view(template_name='usercustom/password_change.html', success_url='/'), name='change_password'),
               # formulario de nueva contraseña para que el admin cambie contraseñas de otros usuarios
               path('admin/change/password/<int:pk>', AdminPasswordReset.as_view(), name='admin_change_password')
               ]